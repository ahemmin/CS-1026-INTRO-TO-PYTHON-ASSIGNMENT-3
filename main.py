from sentiment_analysis import compute_tweets

Tweets_File=input("Please input the name of a tweets file: ")
Keywords_File=input("Please input the name of the file containing your keywords: ")

Processing= compute_tweets(Tweets_File,Keywords_File)
print("Output directly from compute_tweets: ",Processing)









