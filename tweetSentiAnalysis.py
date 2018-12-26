__author__='Mohnish Mallya'
# Importing all necessary libraries
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import codecs
from string import punctuation

class twitterSentimentAnalysis():
    # Consumer key, consumer secret, access token and access secret
    # from twitter application
    ckey = 'ebZ49Qyoj8km7nzHWiUpqKT0J'
    csecret = 'JAmSaEGkvihIAC16eQDiKBKI6HeV06Mh41odphMfxv57R8MB6p'
    atoken = '934336838029910016-35V6eEx4ergfXPSiyISERQxtsbXhyxY'
    asecret = '9ZPZ7n4Cr3td9b5HulFZUql7xm2N0ZYpipfRJsC7uPojN'
	
    # OAuth Authentication
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Twitter API wrapper
    api = tweepy.API(auth)
	
    # Loading list of positive and negative words
    poswords = open("positive_words.txt").read()
    positive_words = poswords.split('\n')
    	
    negwords = open('negative_words.txt').read()
    negative_words = negwords.split('\n')
    	
    # Searches for 10 tweets containing the "Celebrity name"
	# and saves them to "tweets.txt" for sentiment analysis
    def tweetSearch(self, celebName):

        outFile = codecs.open("tweets.txt", 'w', "utf-8")
        results = self.api.search(q=celebName, lang="en", locale="en", count=10)
	
        for result in results:
            outFile.write(result.text + '\n')
            
        outFile.close()
	
    # Counts the total number of positive and negative words in tweets
    def posNegCount(self, tweet):

            pos = 0
            neg = 0

            for p in list(punctuation):
                tweet = tweet.replace(p, '')

            tweet = tweet.lower()
            words = tweet.split(' ')

            for word in words:
                if word in self.positive_words:
                    pos = pos + 1
                elif word in self.negative_words:
                    neg = neg + 1

            return pos, neg

    def tweetSentimentAnalysis(self):
                # Reads tweets from tweet.txt
                tweets = codecs.open("tweets.txt", 'r', "utf-8").read()
                tweets_list = tweets.split('\n')

                positive_count = 0
                negative_count = 0

            # Counts the number of positive and negative words in each and every tweet
            # and accordingly returns the nature of the sentiment
                for twt in tweets_list:
                    if(len(twt)):
                        p, n = self.posNegCount(twt)
                        positive_count += p
                        negative_count += n

                    if positive_count > negative_count:
                        return "POSITIVE"
                    elif positive_count < negative_count:
                        return "NEGATIVE"
                    else:
                        return "NEUTRAL"
