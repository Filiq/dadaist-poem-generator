import random
import os
import sys

def generatePoem():
    words = open("input.txt", "r", encoding="utf-8").read().replace(",", "", -1).replace(".", "", -1).replace("\n", " ", -1).replace("„", "", -1).replace("“", "", -1).replace('"', "", -1).strip().split(" ")

    random.shuffle(words)

    title = ""
    poem = ""
    lineLength = 5
    verseLength = 20


    for i, word in enumerate(words):
        if(i == 0):
            title = random.choice(words).capitalize() + " " + random.choice(words)
            poem += title
            poem += "\n\n"

        #poem += word + f"({i})"

        if(i % (verseLength) == 1 and i != 1):
            poem += word.capitalize()
            #print(i)
        else:
            if(i == 0):
                poem += word.capitalize() + " "
            else:
                poem += word
        
        if(i % lineLength == 0 and i % verseLength != 0 and i != 0):
            poem += ","

        if(i % verseLength != 0 and i % lineLength != 0 and i != 0):
            poem += " "

        if(i % verseLength == 0 and i != 0):
            poem += ".\n"
            
        if(i % lineLength == 0 and i != 0):
            poem += "\n"
 
    return "\n\n".join(poem.split("\n\n")[:-1]), title

for i in range(int(sys.argv[1]) if len(sys.argv) > 1 else 1):
    poem = generatePoem()

    os.path.exists("output") or os.mkdir("output")

    open("output/" + poem[1] + ".txt", "w", encoding="utf-8").write(poem[0])