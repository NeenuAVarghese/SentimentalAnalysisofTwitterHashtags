import tweepy
import json
outputfile = open("output.txt", 'w')

class MyListner(tweepy.StreamListener):
    def on_data(self, data):
        outputfile.write(data)
    def on_error(self, status_code):
        print("Got an error, status code = "+str(status_code))
        return True
def main():
    listner = MyListner()
    auth = tweepy.OAuthHandler("dPuorZljnYcMs50675QQf9BwJ", "XkkvQqaLrQGypzrZyBwDLD3vk6dFW6coLq3N5TlJGGvsHIr7sD")
    auth.set_access_token("4675883312-5VnJsHjZSRPoEwJomzVSRUIh80RP235JXFpUQ0N", "RO3vySugemlqjF9xybsdzM3nN1w9upzA0kxJ5lq95jp9C")
    mystream = tweepy.streaming.Stream(auth, listner)
    mystream.sample()

    
if __name__ == '__main__':
    main()
    
