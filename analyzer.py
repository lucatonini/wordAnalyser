
import re
import sys

def createSentences(text):
    #remove all new line characters
    #Split text into Sentences using ! , ? and . as an array of strings
    #return the array of springs
    return  re.split('[!.?]',text)


def main(argv):

    
    
    #open up files 
    fnouns = open("BAD-Nouns.txt","r")
    fverbs = open("BAD-Verbs.txt","r")
    fmessage = open("Message.txt","r")
    
    #Using createSentences function to return only sentences in the given text
    sent = createSentences(fmessage.read())
    
    #For to check all the words in a sentence
    for i in sent:
        temp = i.split(' ')
        print ("This sentence is made of these words:")
        print(temp)
        print("\n")
    

    

if __name__ == "__main__":
    main(sys.argv[1:])
