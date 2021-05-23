# Import tweepy for retrieving mentions

import tweepy
import logging
import time
import os

# config file handles creation of api with api keys for tweepy
from config import create_api

# getThread in conversation returns the thread with the id of tweet where the bot is mentioned
from conversation import getThread, getConversationId

# this function will send dms
from dm import send_dem

# These functions acces the replit db
from db_handler import setid, getid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# search_user returns username of a matching user id
def search_user(users, id):
    for i in users:
        if i["id"] == id:
            return i["username"]
    return ""


# This function uses tweepy to get mentioned tweets and then find thread from it
def check_mentions(api, since_id):

    # this offset is used to prevent sending dms to very old mentions
    id_offset = int(os.getenv("ID_OFFSET"))

    logger.info("Retrieving mentions")
    new_since_id = since_id

    since_id = since_id if since_id > id_offset else id_offset

    # mentions are retrieved from the mentions timeline of the twitter api using tweepy
    # for each mention we check for a thread i.e checks with its conversation id if it has any replies
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, int(new_since_id))

        # Every tweet object is a mention

        # this string will hold the thread
        thr_string = ""

        # append the tweet where the user mwntioned the bot
        thr_string += f"->{tweet.user.screen_name} mentioned the bot: {tweet.text}"

        # the getThread functions returns the thread object from the tweet id using the conversation id
        thread = getThread(tweet.id)

        # result_count in meta shows the number of replies the mention has got
        # If it's zero, there's no reply and there's no thread to save
        if thread["meta"]["result_count"] == 0:

            thr_string += (
                "-->Can't find a thread associated with this tweet\n---------------\n"
            )
            continue

        # If there is one or more replies, append it to the string
        thr_string += "\n\nThe thread is following: \n"

        # add the first tweet which started the thread, to the string
        getStatus(api, [int(getConversationId(tweet.id))])

        # the thread details are stored in "data"
        for i in reversed(thread["data"]):

            # the "data" only has "tweet id", "tweet text", and "author id"
            # we have to find username by using the author id from the list "users" in "includes"
            un = search_user(thread["includes"]["users"], i["author_id"])

            # append username: tweet_text to the string
            thr_string += f"-->{un} : {i['text']}\n\n"
        # Print a thread terminating indicator
        thr_string += "\n---------------\n"

        # send the dm to the user
        send_dem(tweet.user.id_str, thr_string)

    return new_since_id


# This function returns a tweet from it's id
def getStatus(api, id):
    resp = api.statuses_lookup(id)
    return f"{resp[0].user.screen_name} : {resp[0].text}"


# The main function
def main():
    api = create_api()
    while True:

        # The last_id.txt will store the last mention id
        # so that even after a crash the bot won't send previosly sent messages again
        # with open("last_id.txt", "r") as f:
        #     since_id =

        since_id = int(getid())

        since_id = check_mentions(api, since_id)

        # with open("last_id.txt", "w") as f:
        #     f.write(str(since_id))
        setid(str(since_id))

        # Wait for 1 min before checking for next mention
        time.sleep(60)


if __name__ == "__main__":
    main()
