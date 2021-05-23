# CUCKOO 🐦

## Cuckoo the twitter bot

Ever wished about a bot which can save a twitter thread for you after having an interesting debate on twitter?🤔

Well, cuckoo can help you.😉

Mention her in the thread which you want to save, She will DM you the thread, OR,comeback and log in to the cuckoo console with your twitter id, you can simply download the thread. 😀

## Deployed code

✨ Cuckoo is currently hosted on repl.it

> The current refresh time is set to 1 minute. But the DM may take upto 5 Minutes to reach the end user

## The other repo

> This repo holds the basic code for fetching threads and code to un the bot on repl.it. The web app/console is deployed uding flask and can be found at : [Cuckoo Web console](https://github.com/Jay-2512/cuckoo)

## Deploying cuckoo

- Cuckoo is built using python and tweepy
- Install the required packages and run main.py
- Make sure you have twitter developer account
- Make sure to set the [environment variables](#environment)
- The main function checks for mentions every 1 minute
- The thread_fetch function can be used to import mentions and threads to other pyhpon files
- thread_fetch also has a function writeThread, which can be called by passing in the twitter handle, it'll write the thread to a text file

### Environment

- The following environment variables must be set beforehand if you want to run cuckoo on your machine:
  - API_KEY : Your twitter dev account api key
  - API_SECRET: Your twitter dev account api secret
  - BEARER_TOKEN: Your BearerToken
  - ACCESS_TOKEN: Your app's access token
  - ACCESS_TOKEN_SECRET: Your app's access token secret
  - ID_OFFSET : Set a tweet id here, anyt mention before that will not be considered

## Commiting to the repo

Do you love this project? 😄

You think it has some bugs and know how to fix it? 😮

Or, you think this can be improved? 🤔

You're always welcome to fork, commit and send a pull request 😊

Any pull request, which helps to:

- Fix bugs
- Add more features

will be merged after reviews and conflict inspection from other contributors
