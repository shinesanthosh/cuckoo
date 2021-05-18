# CUCKOO 🐦

## Cuckoo the twitter bot

Ever wished about a bot which can save a twitter thread for you after having an interesting debate on twitter?🤔

Well, cuckoo can help you.😉

Mention her in the thread which you want to save, comeback and log in to the cuckoo console with your twitter id, you can simply download the thread. 😀

## Deployed code

> Cuckoo is currently not hosted anywhere

## Deploying cuckoo

- Cuckoo is built using python and tweepy
- Install the required packages and run thread_fetch.py
- Make sure you have twitter developer account
- Make sure to set the [environment variables](/#Environment)
- thread_fetch also has a function writeThread, which can be called by passing in the twitter handle, it'll write the thread to a text file

### Environment

- The following environment variables must be set beforehand if you want to run cuckoo on your machine:
  - API_KEY : Your twitter dev account api key
  - API_SECRET: Your twitter dev account api secret
  - BEARER_TOKEN: Your BearerToken
  - ACCESS_TOKEN: Your app's access token
  - ACCESS_TOKEN_SECRET: Your app's access token secret

## Commiting to the repo

Do you love this project?

You think it has some bugs and know how to fix it?

Or, you think this can be improved?

You're always welcome to fork, commit and send a pull request

Any pull request, which helps to:

- Fix bugs
- Add more features

will be merged after reviews and conflict inspection from other contributors
