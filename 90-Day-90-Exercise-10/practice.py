import requests
news=input("Enter the news you want to know about =")
language=input("Enter the language you want to know the news in (en for english) =")
resp=requests.get("https://newsapi.org/v2/everything",params={"q":news,"apikey":"f48765137bcf4e09a45f7076a8b3e5ef","language":language})
a=resp.json()
#print(a)

for article in a["articles"][:5]:  
        print("Title:", article["title"])
        print("Content:",article["content"])
        print("Source:", article["source"]["name"])
        print("Published:", article["publishedAt"])
        print("URL:", article["url"])
        print("-" * 60)
