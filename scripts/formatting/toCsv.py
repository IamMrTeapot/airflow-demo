import pandas as pd
import json
import os

new_df = pd.DataFrame()

def read_and_append(file_name):  
    
    global new_df

    # for line in Lines:
    with open(file_name, encoding="utf8") as file:
        data = json.load(file)

    # form the data frame
    df = pd.DataFrame(data)

    id = df["abstracts-retrieval-response"]["coredata"]["dc:identifier"]

    title = ""
    if "dc:title" in df["abstracts-retrieval-response"]["coredata"] :
        title = df["abstracts-retrieval-response"]["coredata"]["dc:title"]
    elif "citation-title" in df["abstracts-retrieval-response"]["item"]["bibrecord"]["head"] :
        title = df["abstracts-retrieval-response"]["item"]["bibrecord"]["head"]["citation-title"]

    aggregation_type = df["abstracts-retrieval-response"]["coredata"]["prism:aggregationType"]
    subtype = df["abstracts-retrieval-response"]["coredata"]["subtypeDescription"]
    cited_by_cnt = df["abstracts-retrieval-response"]["coredata"]["citedby-count"]
    publication_name = df["abstracts-retrieval-response"]["coredata"]["prism:publicationName"]

    publisher = ""
    if "dc:publisher" in df["abstracts-retrieval-response"]["coredata"] :
        publisher = df["abstracts-retrieval-response"]["coredata"]["dc:publisher"]
    
    volume = ""
    if "prism:volum" in df["abstracts-retrieval-response"]["coredata"] :
        volume = df["abstracts-retrieval-response"]["coredata"]["prism:volume"]

    coverDate = df["abstracts-retrieval-response"]["coredata"]["prism:coverDate"]
    
    surname = ""
    if "ce:surname" in df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"] :
        surname = df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"]["ce:surname"]
    elif "ce:surname" in df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"][0]["preferred-name"] :
        surname = df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"][0]["preferred-name"]["ce:surname"]
    
    given_name = ""
    if "ce:given-name" in df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"] :
        given_name = df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"]["ce:given-name"]
    elif "ce:given-name" in df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"][0]["preferred-name"] :
        given_name = df["abstracts-retrieval-response"]["coredata"]["dc:creator"]["author"][0]["preferred-name"]["ce:given-name"]

    affiliation  = []
    for i, item in enumerate(df["abstracts-retrieval-response"]["affiliation"]):
        affiliation.append(item)

    # view data frame
    inserted_df = {'id': id, 
                'title': title, 
                'aggregation_type': aggregation_type, 
                'subtype': subtype, 
                'cited_by_cnt': cited_by_cnt,
                'publication_name': publication_name,
                'publisher': publisher,
                'volume': volume,
                'coverDate': coverDate,
                'surname': surname,
                'given_name': given_name,
                'affiliation': affiliation} 
    new_df = new_df._append(inserted_df, ignore_index = True)


def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        read_and_append(directory + "/" + file)


scrape_directory = "../scraping/result"
target_file = "../visualizing/data/scopusToCSV_FromScraping.csv"

list_files(scrape_directory)
new_df.to_csv(target_file, index=False)
