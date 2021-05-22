# Import tweepy for retrieving mentions

import tweepy
import logging

# config file handles creation of api with api keys for tweepy
from config import create_api

# getThread in conversation returns the thread with the id of tweet where the bot is mentioned
from conversation import getThread


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# search_user returns username of a matching user id
def search_user(users, id):
    for i in users:
        if i["id"] == id:
            return i["username"]
    return ""


# This function uses tweepy to get mentioned tweets and then find thread from it
def check_mentions(api, twitter_handle, since_id):

    # output.txt is the file where the thread will be stored
    f = open("output.txt", "w", encoding="utf-8")

    logger.info("Retrieving mentions")
    new_since_id = since_id

    # mentions are retrieved from the mentions timeline of the twitter api using tweepy
    # for each mention we check for a thread i.e checks with its conversation id if it has any replies
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        # Every tweet object is a mention
        #  if the current tweet object doesn't have a username that is passed in while calling the function
        # the object is ignored
        if tweet.user.screen_name != twitter_handle:
            continue

        # Write to the file that the user mentioned the bot
        f.write(f"->{tweet.user.screen_name} mentioned the bot: {tweet.text}")

        # the getThread functions returns the thread object from the tweet id using the conversation id
        thread = getThread(tweet.id)

        # result_count in meta shows the number of replies the mention has got
        # If it's zero, there's no reply and there's no thread to save
        if thread["meta"]["result_count"] == 0:
            f.write(
                "-->Can't find a thread associated with this tweet\n---------------\n"
            )
            continue

        # If there is one or more replies, write it to the file
        f.write("\n\nThe thread is following: \n")

        # the thread details are stored in "data"
        for i in thread["data"]:

            # the "data" only has "tweet id", "tweet text", and "author id"
            # we have to find username by using the author id from the list "users" in "includes"
            un = search_user(thread["includes"]["users"], i["author_id"])

            # write username: tweet_text to the file
            f.write(f"-->{un} : {i['text']}\n\n")

        # Print a thread terminating indicator
        f.write("\n---------------\n")

    # close the file
    f.close()
    return new_since_id


# This is the function that must be imported by other modules to use it
def writeThread(t_handle):
    api = create_api()
    since_id = 1
    since_id = check_mentions(api, t_handle, since_id)


def main():
    t_handle = input("Enter your twitter handle: ")
    api = create_api()
    since_id = 1
    since_id = check_mentions(api, t_handle, since_id)


if __name__ == "__main__":
    main()
