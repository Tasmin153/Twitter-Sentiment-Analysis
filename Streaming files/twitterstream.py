
import sys

import oauth2 as oauth

import urllib2 as urllib





# See assignment1.html instructions or

# README for how to get these credentials





# My personal Twitter app credentials

api_key = 'Q8Fts1iM3xF3VhPRASBLPRs6I'

api_secret = 'z30LyEcBbnppJLhafEIMjwdRTC4I0esRLel8xj39rKj5Gu7P0N'

access_token_key =  '2596310623-DH43xwiVWpOkZQIcX9M9jdiNxtSDjVWVAgyD1pH'

access_token_secret = '4rZ0l3osUPMzti03eFpTjXXIVQoHdBDcnxwqBqSfjkDoU'





_debug = 0





oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)

oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)









signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()





http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)

https_handler = urllib.HTTPSHandler(debuglevel=_debug)





'''

Construct, sign, and open a twitter request

using the hard-coded credentials above.

'''

def twitterreq(url, method, parameters):

  req = oauth.Request.from_consumer_and_token(oauth_consumer,

                                             token=oauth_token,

                                             http_method=http_method,

                                             http_url=url, 

                                             parameters=parameters)



  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)



  headers = req.to_header()



  if http_method == "POST":

    encoded_post_data = req.to_postdata()

  else:

    encoded_post_data = None

    url = req.to_url()



  opener = urllib.OpenerDirector()

  opener.add_handler(http_handler)

  opener.add_handler(https_handler)



  response = opener.open(url, encoded_post_data)



  return response



# Ubuntu terminal commands.

# For windows you have to figure it out.

#Example: python twitterstream.py (Calls the default "https://stream.twitter.com/1.1/statuses/sample.json")

#Example: python twitterstream.py "https://api.twitter.com/1.1/search/tweets.json?geocode=23.8103,90.4125,400km&lang=en&count=1000"

def fetchSampleTweets(url = "https://stream.twitter.com/1.1/statuses/sample.json"):  

  

  parameters = []

  response = twitterreq(url, "GET", parameters)
  FileObject=open("output.txt","w")

  for line in response:
   FileObject.write(line+'/n/n')
  print (line)
  FileObject.close()



if __name__ == '__main__':  

  if len(sys.argv) == 1: fetchSampleTweets()

  else: fetchSampleTweets(url)
