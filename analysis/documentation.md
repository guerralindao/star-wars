
# Star Wars Unlimited - Analysis

| Activity  | Author             | Description          |
|:---------:|:------------------:|:--------------------:|
| 19/5/2024 | Guerra, Mauro      | Get difference from requests     |
| 19/5/2024 | Guerra, Mauro      | Analysis about scrape data       |

Log analisys

# Api request like http request

How you can see below the request with api generate a json file with all information do you need it. (example_api_response_FULL.json)    

### Example API/HTTP request
https://admin.starwarsunlimited.com/api/cards?locale=it&orderBy[expansion][id]=asc&sort[0]=type.sortValue%3Aasc%2C%20expansion.sortValue%3Adesc%2CcardNumber%3Aasc%2C&filters[variantOf][id][$null]=true&pagination[page]=1&pagination[pageSize]=20

### You can see a little preview about structure and data on json response:

```json
{
    "data": [
        {
            "id": 7912,
            "attributes": {
                "cardNumber": 5,
                "title": "Hondo Ohnaka",
                "subtitle": "Questo Si Chiama Un Vero Affare",
                "cardCount": 262,
                "artist": "Aitor Prieto",
                "artFrontHorizontal": true,
                "artBackHorizontal": null,
                "hasFoil": false,
                "cost": 6,
                "hp": 7,
```

## Understand the request 

* We are using admin section to recover data (url below)

`https://admin.starwarsunlimited.com/api/cards?locale=it`

* It's possible to order by categories, for example an expansion

`&orderBy[expansion][id]=asc`

* It's possible to sorting the results

`&sort[0]=type.sortValue%3Aasc%2C%20expansion.sortValue%3Adesc%2CcardNumber%3Aasc%2C`

* It's possible to filters about some values. It will be censiti.

`&filters[variantOf][id][$null]=true`

* Number of page

`&pagination[page]=1`

* Number of results on page 

`&pagination[pageSize]=20`

### For example I will have all cards without any filters or sorting

This it will give you all cards (649 ?)

https://admin.starwarsunlimited.com/api/cards?locale=it&pagination[page]=1&pagination[pageSize]=20

