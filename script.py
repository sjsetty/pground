import requests


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)
