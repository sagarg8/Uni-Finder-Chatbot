import json
import requests


def getUniData():
    #request uni data, write it to json, return data as a list of dictionaries
    link = 'https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json'
    response = requests.get(link)
    data = json.loads(response.text)
    
    # Serializing json
    # json_object = json.dumps(data, indent=2)
    # with open("uniCollection.json", 'w') as file:
    #     file.write(json_object)
    
    return data


def createCountryIndex(uni_list):
    country_index = {}
    uni_list_length = len(uni_list)
    for ix in range(uni_list_length):
        uni = uni_list[ix]
        country = uni["country"].lower()
        if country in country_index:
            country_index[country].append(ix)
        else:
            country_index[country] = [ix]
    
    return country_index


def createNameIndex(uni_list):
    name_index = {}
    uni_list_length = len(uni_list)
    for ix in range(uni_list_length):
        uni = uni_list[ix]
        name = uni["name"].lower()
        name_index[name] = ix

    return name_index


def setup():
    uniData = getUniData()
    country_index = createCountryIndex(uniData)
    name_index = createNameIndex(uniData)

    return uniData, country_index, name_index