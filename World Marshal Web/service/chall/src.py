#!/usr/local/bin/python

import sys
import numpy as np
from sknetwork.ranking import PageRank

SIZE = 200
TARGETIDX = 174

adjacency = np.loadtxt('webpages.txt', delimiter=",")

print("You successfully gained access to the World Marshal Web GOOGL webpage ranking server. You want to get ropllc.com to the top, but don't want to raise any suspicion, so you can only query the system a maximum of 5 times.\n\n")

print(r"""
 _______    ______   ______   _______    __          
/______/\  /_____/\ /_____/\ /______/\  /_/\         
\::::__\/__\:::_ \ \\:::_ \ \\::::__\/__\:\ \        
 \:\ /____/\\:\ \ \ \\:\ \ \ \\:\ /____/\\:\ \       
  \:\\_  _\/ \:\ \ \ \\:\ \ \ \\:\\_  _\/ \:\ \____  
   \:\_\ \ \  \:\_\ \ \\:\_\ \ \\:\_\ \ \  \:\/___/\ 
    \_____\/   \_____\/ \_____\/ \_____\/   \_____\/ 
                                                     
""")

print("\nWelcome USER:ROPLLCSPY to the GOOGL webpage ranking server!\nEach valid query will flip a link between 2 websites.\n\t - If a link exists, it will be deleted.\n\t - If a link doesn't exist, it will be created.\n")

sys.stdout.flush()

for _ in range(5):
  sel = input('\nWould you like to edit a link? (Y/N)').upper()
  sys.stdout.flush()
  if sel=='N':
    break
  elif sel == 'Y':
    try:
      row = int(input('From: '))
      sys.stdout.flush()
      col = int(input('To: '))
      sys.stdout.flush()
    except:
      print('Your query has been rejected.')
      continue

    if row>=0 and row<SIZE and col>=0 and col<SIZE:
      adjacency[row][col] = -(adjacency[row][col]-1)
      print('Success.')
    else:
      print('Your query has been rejected.')

  else:
    print('Your query has been rejected.')

pagerank = PageRank()
scores = pagerank.fit_predict(adjacency)

scores_sorted = sorted(zip(list(range(SIZE)), scores), key= lambda x: x[1], reverse=True)
idx_sorted,_ = zip(*scores_sorted)
print('RANKING FOR ropllc.com: {}'.format(idx_sorted.index(TARGETIDX)+1))

if np.argmax(scores) == TARGETIDX:
  print(open('flag.txt','r').read())

sys.stdout.flush()