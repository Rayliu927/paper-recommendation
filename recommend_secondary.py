import mysql.connector


# connect to database
try:
    cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='recommendation',
                                  auth_plugin='mysql_native_password')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print(err)

search_input = "Jerzy Mycka"

# get paper Ids by author name
def getPaperByAuthor(author):
    sql = "select paper_id from recommendation.author where author=" + "'" + author + "'"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

# get all reference Ids by paper Ids
def getReferenceByPaperId(paperIds, numReturn):
    res = []
    for id in paperIds:
        if len(res) > numReturn:
            break
        id = id[0]
        sql = "select reference from recommendation.references where paper_id=" + "'" + id + "'"
        cursor.execute(sql)
        tmp = cursor.fetchall()
        res.extend(tmp)
    return res

# get recommened paper title based on ids
def getPaperTitleById(paperIds):
    res = []
    for id in paperIds:
        id = id[0]
        sql = "select title from recommendation.paper where paper_id= " + "'" + id + "'"
        cursor.execute(sql)
        tmp = cursor.fetchone()
        res.append(tmp)
    return res



# based on author name, get recommendation candidate
paperIds = getPaperByAuthor(search_input)
referenceIds = getReferenceByPaperId(paperIds, 5)
secondaryReferenceIds = getReferenceByPaperId(referenceIds, 10)

# get recommended paper id
exsistReference = set(referenceIds)
recommendation  = []
for id in secondaryReferenceIds:
    if id not in exsistReference:
        recommendation.append(id)

# get recommended paper titles
recommendTitles = getPaperTitleById(recommendation)
authorPaper = getPaperTitleById(paperIds)

print(authorPaper)
print("a")
print(recommendTitles)















