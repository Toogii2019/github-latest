import sys
import requests

# Use Like python githubber.py JASchilz
# (or another user name)

def get_event_timestamp(username, event_num=1):
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = response.json()
    return events[0].get('created_at')

if __name__ == "__main__":
    help = 'Example: python main.py {username}'
    try:
        username = sys.argv[1]
    except IndexError:
        sys.exit(help)
    timestamp = get_event_timestamp(username, event_num=1)
    print(timestamp)


    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    print("COMPLETE THE TODOs")
    


