import requests
from send_email import send_email

api_key = "7a90230871614d94acae52a2bc13172c"

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-29&sortBy=publishedAt&apiKey" \
      "=7a90230871614d94acae52a2bc13172c"

# Make request
request = requests.get(url)
content = request.json()

# Access article's title, author, ID and description.
body = ""
for article in content["articles"]:
    if article is not None:
        body = body + article['title'] + "\n" + article['description'] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
