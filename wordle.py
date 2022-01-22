import re, random

def OpenFile(file):
    f = open(file)
    return f.read().splitlines()

def CheckNonRepeating(word):
    holder = []
    for char in word:
        if char in holder:
            return False,"Word has repeating characters."
            break
        else:
            holder.append(char)
    return True

def MakeFiveCharWordlist(words):
    holder = []
    for word in words:
        if len(word) == 5:
            if CheckNonRepeating(word) == True:
                holder.append(word)
            else:
                pass
    return holder

def GetRandomNonRepeatingCharWord(words):
    return random.choice(words)

def RegularExpression(words):
    pattern = input("\nEnter RGEX: ")
    printWords = []
    for word in words:
        if re.search(pattern,word):
            printWords.append(word)
    return printWords

wordlist = OpenFile('wordlist.txt')
FiveCharWordlist = MakeFiveCharWordlist(wordlist)
FirstWord = GetRandomNonRepeatingCharWord(FiveCharWordlist)

print(f"Your first word is: {FirstWord}")
while True:
    regString = RegularExpression(FiveCharWordlist)
    for word in regString:
        print(word)