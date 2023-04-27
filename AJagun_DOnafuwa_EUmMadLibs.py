import random
#defining a function, the argument will be a placeholder related to the project (ML for MadLin), returning a line from the file
def randMad(MadLib):
    ML = open(MadLib).read().splitlines()
    return random.choice(ML)
#function that will take user input and insert it into the placeholders in the original file
def MadSentence():
    ninput = []
#this and subsequent input/print lines will take whatever input the user gives and append it
    print("Enter a(n) place:")
    MadLibplace = input()
    ninput.append(MadLibplace)
    print("Enter a(n) plural animal:")
    MadLibpan = input()
    ninput.append(MadLibpan)
    print("Enter a(n) adjective:")
    MadLibad = input()
    ninput.append(MadLibad)
    print("Enter a(n) verb:")
    MadLibverb = input()
    ninput.append(MadLibverb)
    print("Enter a(n) color:")
    MadLibcolor = input()
    ninput.append(MadLibcolor)
    print("Enter a(n) animal:")
    MadLiban = input()
    ninput.append(MadLiban)
    #MadLibrand = randMad("MadLib Sentences.txt")
    newMadLibrand = MadLibrand.replace("<place>", MadLibplace).replace("<animal>", MadLiban).replace("<plural animal>", MadLibpan).replace("<verb>", MadLibverb).replace("<color>", MadLibcolor).replace("<adjective>", MadLibad)
    print(newMadLibrand)

MadSentence()

