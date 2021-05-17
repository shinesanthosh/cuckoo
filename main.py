import tweepy
import logging
import time

from config import create_api
from conversation import getThread


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, twitter_handle, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        # if tweet.in_reply_to_status_id is not None:
        #     continue
        if tweet.user.screen_name != twitter_handle:
            continue

        print(f"{tweet.user.screen_name} mwntioned you in {tweet.text}")
        thread = getThread(tweet.id)
        if thread["meta"]["result_count"] == 0:
            print("Can't find a thread associated with this tweet\n---------------\n")
            continue

        print("\n\nThe thread is following: \n")
        for i in thread["data"]:
            print(f"{i['text']}\n\n")

    return new_since_id


def main():
    t_handle = ""
    api = create_api()
    since_id = 1
    since_id = check_mentions(api, t_handle, since_id)


if __name__ == "__main__":
    main()
