# Required imports or library dependencies
import matplotlib.pyplot as plt
import operator
import re, sys, json
from tweet_sentiment import *
from collections import Counter

# Fill me.
# Details explained in class.
def gettopTenHashTags(tweets_file, n = 10):
    hashTagFreq = {}
    tweets_file = open(tweets_file)
    FileObject=open("hashtags.txt","w")
    
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        
        try:
           for hashtag in tweet_json['entities']['hashtags']:
               
               FileObject.write(hashtag['text']+'\n')
              
        except: pass
    FileObject.close()      
    top_Ten = re.findall(r'\w+', open('hashtags.txt').read().lower())
    ten_hashtags = Counter(top_Ten).most_common(n)
           
    print(ten_hashtags) 
        
    #dictionary = {}
    #with open('hashtags.txt','r') as f:
        #for line in f:
            #a,b = line.split()
            #dictionary[a] = int(b)


    return ten_hashtags

def plothashtagsBar(ten_hashtags):
    
    lists = sorted(ten_hashtags, key=operator.itemgetter(1), reverse=True)[0:10]

    terms, counts = zip(*lists)

    r = range(len(terms))

    plt.xticks(r, terms)

    plt.bar(r, counts, align='center')

    plt.show()
                  
        
           
   


        
if __name__ == '__main__':    
    ten_hashtags = gettopTenHashTags(sys.argv[1])
    plothashtagsBar(ten_hashtags)
       
    
    
    
