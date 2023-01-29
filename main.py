import requests

api_key = "7a90230871614d94acae52a2bc13172c"

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-29&sortBy=publishedAt&apiKey" \
      "=7a90230871614d94acae52a2bc13172c"

# Make request
request = requests.get(url)
content = request.json()

# Access article's title, author, ID and description.

for article in content["articles"]:
    print(article)
    print(article['title'])
    print(article['author'])
