import requests
import os
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")


def getConversationId(id):
    uri = "https://api.twitter.com/2/tweets?"

    params = {"ids": id, "tweet.fields": "conversation_id"}

    bearer_header = {
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer {}".format(bearer_token),
        "oauth_consumer_key": consumer_key,
    }
    resp = requests.get(uri, headers=bearer_header, params=params)
    return resp.json()["data"][0]["conversation_id"]


# Returns a conversation from the v2 enpoint  of type [<original_tweet_text>, <[replies]>]
def getConversation(conversation_id):
    uri = "https://api.twitter.com/2/tweets/search/recent?"

    params = {
        "query": f"conversation_id:{conversation_id}",
        "tweet.fields": "in_reply_to_user_id",
        "tweet.fields": "conversation_id",
    }

    bearer_header = {
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer {}".format(bearer_token),
        "oauth_consumer_key": consumer_key,
    }
    resp = requests.get(uri, headers=bearer_header, params=params)
    return resp.json()


def getThread(id):
    return getConversation(getConversationId(id))
