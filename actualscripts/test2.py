import requests

username = "niccdias"
password = "bM65lMa99ybZcd0r"

PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:222"

urlToGet = "http://ip-api.com/json"

proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_RACK_DNS)}

r = requests.get(urlToGet , proxies=proxy)

print(proxy)
print("Response:\n{}".format(r.text))