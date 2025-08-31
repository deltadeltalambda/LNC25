#! pip install -U redditwarp
import redditwarp
import redditwarp.SYNC
from itertools import islice

def getprefix(link, num): # returns first num letters of post ID
    return link.split('comments/')[1].split('/')[0][:num]

def findpost(subreddit, prefix):
    client = redditwarp.SYNC.Client()
    x = client.p.subreddit.pull.new(subreddit) #sort posts from new to old
    paginator = x.get_paginator()
    for page in islice(paginator, 100): #arbitrarily large value
        if getprefix(page[-1].permalink, len(prefix)) > prefix: # posts are made after target post
            continue
        for subm in page:
            if getprefix(subm.permalink, len(prefix)) < prefix: # post is made before target post
                return # end search
            elif getprefix(subm.permalink, len(prefix)) == prefix: # target post found
                print("{0.permalink} | {0.created_at}".format(subm))
              

# enter target subreddit and post ID prefix
findpost('bakingrecipes','1jxl')