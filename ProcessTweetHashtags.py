import json
from collections import Counter

#wordcount_tweet = {}

def afinn_dict():
    scores = {}
    afinnfile = open("AFINN-111.txt")
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def tweet_list():
    tweets = []
    for line in open('output.txt'):
        try:
            tweets.append(json.loads(line))
        except:
            pass
    print("Total number of objects collected :" +str(len(tweets)))
    return tweets

def tweets_hashtags(tweets):
    hashtags = []
    hashtagcount = 0
    tweetcount = 0
    for item in tweets:
        if 'text' in item:
            tweetcount += 1
            for hashtag in item['entities']['hashtags']:
                hashtags.append(hashtag['text'])
                hashtagcount += 1
    print("Total number of tweets are:" + str(tweetcount))
    print("Total number of tweets with hashtags are:" + str(hashtagcount))
    return hashtags

def toptenhashtags(hashtaglist):
    topten = {}
    print ("Top Ten hashtags are:\n")
    sortedhashtags = Counter(hashtaglist)
    for hashtags, count in sortedhashtags.most_common(10):
        topten[hashtags] = 0
        print(hashtags + " : " + str(count))
    return topten

def sentimentalanalysis(tweets, topten_hashtag, afinndata):
    #print (afinndata.keys())
    wordcount_tweet = topten_hashtag.copy()
    for item in tweets:
        if 'text' in item:
            for hashtag in item['entities']['hashtags']:
                hashtag_text = hashtag['text']
                if hashtag_text in topten_hashtag.keys():
                    text = item["text"].split()
                    for word in text:
                        word = word.rstrip('?:!.,;"!@')
                        word = word.replace("\n", "")
                        if not (word.encode('utf-8', 'ignore') == ""):
                            if word in afinndata.keys():
                                topten_hashtag[hashtag_text] = topten_hashtag[hashtag_text] + int(afinndata[word])
                            else:
                                topten_hashtag[hashtag_text] = topten_hashtag[hashtag_text]
    sum_val = 0
    for key in topten_hashtag:
        sum_val = topten_hashtag[key]

    for key in topten_hashtag:
        print(key, topten_hashtag[key]/sum_val)

    

def main():
    afinndata = afinn_dict()
    tweetdata = tweet_list()
    hashtag_list = tweets_hashtags(tweetdata)
    topten = toptenhashtags(hashtag_list)
    sentimentalanalysis(tweetdata, topten, afinndata)


if __name__ == '__main__':
    main()
