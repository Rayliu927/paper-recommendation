from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# this is the paper written by author Jerzy Mycka
author = [(u'A SIMPLE OBSERVATION REGARDING ITERATIONS OF FINITE-VALUED POLYNOMIAL-TIME FUNCTIONS',), (u'What Lies Beyond the Mountains',), (u'Restricted Limits on Natural Functions with Arithmetical Graphs.',), (u'Real Recursive Functions and Baire Classes',), (u'The New Promise of Analog Computation',), (u'Infinite limits and R-recursive functions',), (u'The computational power of continuous dynamic systems',), (u'Classes of Markov-like k-ALGORITHMS',), (u'The P\u2260NP conjecture in the context of real and complex analysis',), (u'\xb5-recursion and infinite limits',), (u'Undecidability over Continuous Time',), (u'A foundation for real recursive function theory',), (u'Computability on reals, infinite limits and differential equations',), (u'A new conceptual framework for analog computation',), (u'Real recursive functions and their hierarchy',), (u'Analog computation beyond the Turing limit',), (u'The Euclid Abstract Machine.',), (u'Two hierarchies of R-recursive functions.',), (u'Mind and information processing: some considerations',), (u'The euclid abstract machine : Trisection of the angle and the halting problem',), (u'RECURSIVELY ENUMERABLE SETS AND WELL-ORDERING OF THEIR ENUMERATIONS',)]

# this is the result of secondary recommendation from recommend.py
# we are using content-related recommendation to rank these paper based on similarity score.
recom = [(u'Computable analysis: an introduction',), (u'Real recursive functions and real extensions of recursive functions',), (u'\xb5-recursion and infinite limits',), (u'Closed-form analytic maps in one and two dimensions can simulate universal Turing machines',), (u'Iteration, Inequalities, and Differentiability in Analog Computers',), (u'Continuous-time computation with restricted integration capabilities',)]

authorPaper = "".join([i[0] for i in author])
recomPaper = [i[0] for i in recom]
recomPaper.append(authorPaper)
# print(recomPaper)

count_matrix = CountVectorizer().fit_transform(recomPaper)
cosine_sim = cosine_similarity(count_matrix)
index = -1
similar_papers =  list(enumerate(cosine_sim[index]))
sorted_similar_papers = sorted(similar_papers,key=lambda x:x[1],reverse=True)[1:]

paper = [recomPaper[i[0]] for i in sorted_similar_papers]
print(paper)
