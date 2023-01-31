import requests
from send_email import send_email


topic = "tesla"
api_key = "7a90230871614d94acae52a2bc13172c"

# Ensure from date is current or a month behind
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-1-29&sortBy=publishedAt&apiKey" \
      "=7a90230871614d94acae52a2bc13172c&language=en"

# Make request
request = requests.get(url)
content = request.json()

# Access article's title, author, ID and description.
body = ""
for article in content["articles"][:20]:
    if article is not None:
        body = "Subject: Today's new by Herve" + "\n" + body + article['title'] + "\n" + \
               article['description'] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
