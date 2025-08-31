import numpy as np
from sknetwork.ranking import PageRank

SIZE = 200
adjacency = np.loadtxt('webpages.txt', delimiter=",")

#run pagerank
pagerank = PageRank()
scores = pagerank.fit_predict(adjacency)

# sort scores and find the index of rank 189 
# note that rank is 1-indexed but scores_sorted is 0-indexed
scores_sorted = sorted(zip(list(range(SIZE)), scores), key= lambda x: x[1], reverse=True)
targetidx = scores_sorted[188][0]

# print ropllc.com info
print('ropllc.com INDEX = {}'.format(targetidx))
print('ropllc.com OUTLINKS = {}'.format(np.where(adjacency[targetidx] == 1)[0]))
print('ropllc.com INLINKS = {}'.format(np.where(adjacency[:,targetidx] == 1)[0]))

# compare with other webpages
rowsum = np.sum(adjacency,axis=1).tolist()
colsum = np.sum(adjacency, axis=0).tolist()
print('Average INLINKS = {}'.format(np.average(colsum)))
print('Any Deadends/Spider Traps? = '.format(any(i<=1 for i in rowsum)))