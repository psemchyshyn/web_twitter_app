'''
Palvo Semchyshyn
22.02.2020
'''


import time
import tweepy as tw


CONSUMER_KEY = 'eG16vH0njymriU5FGdhQiN0qS'
CONSUMER_SECRET = 'Mk2K5whzgmA9SoM4FJ13OZmZOJHgixyuCZsl2eELvnGA67kJa2'
ACCESS_TOKEN = '1230092016085848064-q3niy7e5uD9LBkzmEuOpop5RN3OxpF'
ACESS_TOKEN_SECRET = 'KyMKnE3aKfg4oxXiUnyssjbdWyXRrSOo30WzLRjH9Onup'


AUTH = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
API_OBJ = tw.API(AUTH, wait_on_rate_limit=True)


def getting_followers(user: str) -> dict:
    """
    A function input is a string of user name or
    id and the output is a dictionary of this
    user friends and their locations
    """
    followers = API_OBJ.followers(user)
    friends_dict = {}
    count = 0
    for friend in followers:
        if friend.location != "":
            friends_dict[friend.screen_name] = friend.location
            count += 1
        if count > 15:
            break
    return friends_dict


def check_user_name(user: str) -> bool:
    """
    A function for checking a validity of
    the name of twitter account
    """
    try:
        API_OBJ.followers(user)
        valid = True
    except tw.error.TweepError:
        valid = False
    return valid


def user_input() -> str:
    """
    A function for getting a user input
    """
    while True:
        user = input("Enter the user name or id: ")
        if check_user_name(user):
            break
        print("There is no such name or id")
    return user


def run_twitter_users(user: str) -> None:
    """
    A function for running the main
    logic of module.
    """
    print("Processing friends.....\n")
    time.sleep(1)
    friends = getting_followers(user)
    for friend in friends:
        print(f"{friend} - {friends.get(friend)}")


if __name__ == "__main__":
    USER = user_input()
    run_twitter_users(USER)
