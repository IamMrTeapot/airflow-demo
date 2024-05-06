import requests as re

apiKey = "e2e6b3497dcecdbe37963b1bca44b726"
query = "engineering"

url = f"https://api.elsevier.com/content/search/scopus?query={query}&apiKey={apiKey}"


result = []

def scrape(url):
    response = re.get(url)

    print(response.headers.get("X-RateLimit-Remaining"))

    for i in response.json()["search-results"]["entry"]:
        for j in i["link"]:
            if(j["@ref"] == "self"):
                result.append(j["@href"].split("/")[-1])

    for i in response.json()["search-results"]["link"]:
        if(i["@ref"] == "next"):
            return i["@href"]
    return None

limit = 3

while(url):
    limit -= 1
    if(limit == 0):
        break
    url = scrape(url)
    # save result to file and reset result
    with open("/opt/airflow/scripts/scopus_search.txt", "a") as f:
        for i in result:
            f.write(i + "\n")
    result = []