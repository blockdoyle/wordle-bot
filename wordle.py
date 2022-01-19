import re

file = open("wordlist.txt")
wordlist = file.read().splitlines()
file.close()

pattern=input("Enter grep: ")

for word in wordlist:
    if re.search(pattern,word):
        print(word)