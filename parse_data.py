import json
import mysql.connector


# class for dblp papers
class Paper:
    def __init__(self):
        self.id = None
        self.title = None
        self.authors = []
        self.references = []

    def printPaper(self):
        print(self.id)
        print(self.title)
        print(self.authors)
        print(self.references)


# connect to database
try:
    cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='recommendation',
                                  auth_plugin='mysql_native_password')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print(err)

# return list of author names
def parseAuthor(authors):
    results = []
    for author in authors:
        results.append(author["name"])
    return results

# parse data from txt file
def parseData():
    filename = 'dblp_papers_v11.txt'
    data = []
    with open(filename) as f:
        for line in f:
            tmp = json.loads(line)
            paper = Paper()
            if "id" in tmp:
                paper.id = tmp["id"]
            if "title" in tmp:
                paper.title = tmp["title"]
            if "authors" in tmp:
                paper.authors = parseAuthor(tmp["authors"])
            if "references" in tmp:
                paper.references = tmp["references"]
            data.append(paper)
    return data


def storeAuthor(paper_id, authors):
    sql = "insert into recommendation.author (paper_id, author) values (%s, %s)"
    for author in authors:
        cursor.execute(sql, (paper_id, author))

def storeReferences(paper_id, references):
    sql = "insert into recommendation.references (paper_id, reference) values (%s, %s)"
    for reference in references:
        cursor.execute(sql, (paper_id, reference))

def storeData(data):
    print(len(data))
    count = 0
    for paper in data:
        count += 1
        print(count)
        paper_id = paper.id
        paper_title = paper.title
        authors = paper.authors
        references = paper.references
        storeAuthor(paper_id, authors)
        storeReferences(paper_id, references)
        # sql = "insert into recommendation.author (paper_id, author) values ('aaa', 'ray');"
        cursor.execute("insert into recommendation.paper (paper_id, title) values (%s, %s)", (paper_id, paper_title))


# if __name__ == '__main__':
# cursor.execute("select * from recommendation.author")
# print(cursor.fetchone())

data = parseData()
storeData(data)
cnx.commit()
cnx.close()
