import re

pattern=r"[a-z]he" #but this has a problem it will search for any character that has he in the end even inside words

text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion
in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February.
It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached
its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph),
and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next 
couple of days due to wind shear, and became a post-tropical cyclone on 7 March
'''


m=re.search(pattern,text) #Only returns first match 
print(m)

l=re.finditer(pattern,text)

for match in l:
    print(match.span())

print(text[m.span()[0]:m.span()[1]])
print(m.group())

#Wr use boundary to get precise words in text

pattern2=r"\bthe\b"

n=re.search(pattern2,text)
print(n)

t=re.finditer(pattern2,text)

for match in t:
    print(match.span(),match.group())   #tells coordinates of each 'the' and print 'the' alongside it

k=re.search("^Cyclone",text)   #Only matches if its first word
print(k)
print(re.findall("^Cyclone",text)) #prints all "Cyclone" appearing as first word
print(k.span()) #Position of the word
print(text[k.span()[0]:k.span()[1]]) #Print the word

j=re.search("March$",text) #Only matches if its last word
print(j)
print(j.span()) #Position of the word
print(re.findall("March$",text))
print(text[j.span()[0]:j.span()[1]]) #Print the word

i=re.search("c.t","I had a cat who cut me everyday for not giving her snacks ,yet she was cute ")

i1=re.findall("c.t","I had a cat who cut me everyday for not giving her snacks ,yet she was cute ")
print(i1)

i2=re.finditer("c.t","I had a cat who cut me everyday for not giving her snacks ,yet she was cute ")
for match in i2:
    print(match.span(),match.group())

j1=re.findall("colou?r","Some people say it's color ,some says it's colour ,but it depends on which type of english you use.") #u is optional
print(j1)
j2=re.finditer("colou?r","Some people say it's color ,some says it's colour ,but it depends on which type of english you use.")

for match in j2:
    print(match.group(),match.span())

k1=re.findall("cat|dog", "I have a cat and a dog") #cat or dog
print(k1)
k2=re.finditer("cat|dog", "I have a cat and a dog")

for match in k2:
    print(match.group(),match.span())

#Like these there are alot of methods .......
