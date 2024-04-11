import requests

def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "My User Agent 1.0",
    }
    params = {
        "limit": 10,
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(None)
        else:
            print("An error occurred: ", e)

    except requests.exceptions.ConnectionError as e:
        print("Failed to connect to Reddit API: ", e)

    except requests.exceptions.Timeout as e:
        print("Request timed out: ", e)

    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)
