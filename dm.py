# This file sends dms to the user, the thread string, with the id

from dotenv import load_dotenv
from config import create_api

load_dotenv()

api = create_api()


def send_dem(id_str, thr_string):


    # Add some intro so that the user won't panic
    api.send_direct_message(id_str, "Hoi hoi \n I'm cuckoo the bot ")
    api.send_direct_message(
        id_str,
        "You're getting this message because you've mentioned me in a thread\nI've saved it for you, Here's it:",
    )

    # Send the thread string
    api.send_direct_message(id_str, thr_string)
