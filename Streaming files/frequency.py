import matplotlib.pyplot as plt
import operator
import re, sys, json
from collections import Counter
from tweet_sentiment import *

# Fill the rest
# Details explained in class.
# Input: The downloaded tweets file
# Output: The freq dictionary {key: tweet terms, value: frequency as probability}
def frequency(tweets_file):
    freq = {}
    tweets_file = open(tweets_file)
    sum = 0.0
  
  

    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        tweet_terms = getENTweet(tweet_json)
   
       
        for term in tweet_terms:
            term = term.lower()
            try:
                freq[term] += 1
               
            except:
                freq[term] = 1
              
    for key in freq:
        sum = sum + freq[key]
    for key in freq:
        freq[key] = (freq[key]/sum)*10000
        print (key,freq[key])   

     
        
    return freq

def printFrequency(freqDict):
    for key in freqDict.keys():
        print("%s %.4f" % ( key, freqDict[key] ) )
def plotFrequencyBar(freqDict):

    lists = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)[0:10]
    terms, counts = zip(*lists)

    r = range(len(terms))

    plt.xticks(r, terms)

    plt.bar(r, counts, align='center')

    plt.show()
           

if __name__ == '__main__':
    printFrequency(frequency(sys.argv[1]))
    plotFrequencyBar(frequency(sys.argv[1]))
