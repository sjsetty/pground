import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


r = requests.get("https://google.com")
print(r.status_code)
