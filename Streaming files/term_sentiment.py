# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *
from collections import Counter
import cPickle as pickle


MAX_VALUE = 5

# Generate predicted Sentiment Dictionary from tweet score and unknown tweet terms.
# May want to use try except block
# The predSentDict updates automatically that is why we do not return anything.
# Fill the rest, details explained in class.
def genPredSentDict(score, numTerms, uTerms, predSentDict):    
    for uTerm in uTerms:
       
        if(uTerm not in predSentDict):
            predSentDict[uTerm] = [score,numTerms]
          
        elif(uTerm in predSentDict):
               
               old_score = predSentDict[uTerm][0]
               new_score = score + old_score
               old_terms = predSentDict[uTerm][1]
               new_terms = numTerms + old_terms
               predSentDict[uTerm] = [new_score,new_terms] 
            
        else: pass     
              
    return predSentDict


# Analyse The tweet
# Input: Tweet terms as list, and the sentiment dictionary - hashmap/map
# Output: tweet score, unknown terms as a set data structure.
# Fill the rest. 
# Details explained in class.

def tweetAnalysis(tweet_terms, sentDict):    
    tweet_score = 0
    unknown_terms = set()
      
    for term in tweet_terms:
        term = term.lower()
	tweet_score = tweet_score + sentDict.get(term, 0)
        if(term not in sentDict):
           unknown_terms.add(term)
  
    return tweet_score, unknown_terms


# Refine the new sentiment dicionary!
# Details explained in class.
# Update the new sentiment dictionary, therefore no explicit return
# Fill the rest.
def refinePredSentDict(newSentDict):

    for key in newSentDict.keys():
        newSentDict[key] =(newSentDict[key][0]/newSentDict[key][1])*5
  
    return newSentDict


def printSentDict(sentDict):
    for key in sentDict.keys():
        value = sentDict[key]
        print (key, value)
    
    FileObject = open("newSentDict.txt","w")
    FileObject.write(json.dumps(sentDict)+'\n')
    FileObject.close()
 


def initPredSentDict(sentDict, tweets_file):
    newSentDict = {}    
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)
    
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        tweet_terms = getENTweet(tweet_json)

        nTerms = len(tweet_terms)
        score, uTerms = tweetAnalysis(tweet_terms, sentDict)
        genPredSentDict(score, nTerms, uTerms, newSentDict)        
        
    return newSentDict



def getPredSentDict(sentDict, tweets_file):
    predDict = initPredSentDict(sentDict, tweets_file)
    refinePredSentDict(predDict)
    return predDict


if __name__ == '__main__':
    predDict = getPredSentDict(sys.argv[1], sys.argv[2])
    printSentDict(predDict)
    
