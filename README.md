![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# CUCKOO 🐦

## Cuckoo the twitter bot

Ever wished about a bot which can save a twitter thread for you after having an interesting debate on twitter?🤔

Well, cuckoo can help you.😉

Mention her in the thread which you want to save, She will DM you the thread, OR,comeback and log in to the cuckoo console with your twitter id, you can simply download the thread. 😀

## Team Members

1. Shine Santhosh | [GitHub](https://github.com/shinesanthosh) | [Twitter](https://twitter.com/shinesanthosh2)
2. JayaSurya Jayandan | [GitHub](https://github.com/Jay-2512) | [Twitter](https://twitter.com/jay_24__)
3. Aswin Anish | [GitHub](https://github.com/AswinAnish) | [Twitter](https://twitter.com/AswinAnish1)

## Team ID

```python
BFH/recyBx9eaZvAwGquP/2021
```

## Product walkthrough

[Product walkthrough](https://www.youtube.com/watch?v=GfvWctqfKwc)

## Deployed code (How to use)

✨ Cuckoo is currently hosted on repl.it

✨ Mention `@ShineSanthosh2` in any thread to get the thread as a DM

> The current refresh time is set to 1 minute. But the DM may take upto 5 Minutes to reach the end user

## The web console repo

> This repo holds the basic code for fetching threads and code to run the bot on repl.it. The web app/console is deployed uding flask and can be found at : [Cuckoo Web console](https://github.com/Jay-2512/cuckoo)

## Libraries used

- Tweepy - 3.10.0
- python-dotenv - 0.17.1
- replit - 3.1.0

> Check [requirements.txt](./blob/main/requirements.txt) for details

## Deploying cuckoo (How to configure)

- Cuckoo is built using python and tweepy
- Install the required packages and run main.py
- Make sure you have twitter developer account
- Make sure to set the [environment variables](#environment)
- The main function checks for mentions every minute
- The thread_fetch function can be used to import mentions and threads to other python files
- thread_fetch also has a function writeThread, which can be called by passing in the twitter handle, it'll write the thread to a text file

## How to run

- Install the requirements
- Set the [environment variables](#environment)
- Run main.py

## How it works

- The bot uses the mentions timeline endpoint provided by the twitter API to fetch mentions
- The conversation id is retrieved from the mentions
- Using the conversation id the thread is fetched
- Then the thread is sent through DM

### Environment

- The following environment variables must be set beforehand if you want to run cuckoo on your machine:
  - API_KEY : Your twitter dev account api key
  - API_SECRET: Your twitter dev account api secret
  - BEARER_TOKEN: Your BearerToken
  - ACCESS_TOKEN: Your app's access token
  - ACCESS_TOKEN_SECRET: Your app's access token secret
  - ID_OFFSET : Set a tweet id here, any mention before that will not be considered






















