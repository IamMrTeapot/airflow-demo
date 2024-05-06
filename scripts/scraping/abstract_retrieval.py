# pip3 install xmltodict

import requests as re
import xmltodict
import json

apiKey = "e2e6b3497dcecdbe37963b1bca44b726"

scopus_id = open("scopus_search.txt", "r").read().split("\n")

for i in scopus_id:
    url = f"https://api.elsevier.com/content/abstract/scopus_id/{i}?apiKey={apiKey}"
    response = re.get(url)
    print(response.headers.get("X-RateLimit-Remaining"))
    result = xmltodict.parse(response.text)
    with open(f"result/{i}.json", "w") as f:
        json.dump(result, f, indent=4)