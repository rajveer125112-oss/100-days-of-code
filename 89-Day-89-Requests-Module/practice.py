import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com/tutorial/cpp-stl"
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())

for heading in soup.find_all("h3"):
  print(heading.text)

url1="https://jsonplaceholder.typicode.com/posts" #Target Url for fake testing an API (JSONplaceholder)

data={                                            #Payload : Actual data that I'll send to server
  "title":"Rajveer",
  "body":"Programmer",
  "userID":26

}

headers={                                         #Setting the data format, here it's in json so we set to UTF-8 and Servers often check 'Content-type' header to know how to parse the data
    'Content-type': 'application/json; charset=UTF-8'
}

response=requests.post(url1,headers=headers,json=data)   #Posting using requests, using headers as mentioned above, using data as json so that data will get converted into json string

print(response.text)

#If a API is built to expect json we have to use json else it would might not be possible for servers to parse the data as they expect it to be of json format