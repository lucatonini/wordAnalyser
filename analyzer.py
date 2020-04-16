
import re
import sys

def createSentences(text):
    #remove all new line characters
    #Split text into Sentences using ! , ? and . as an array of strings
    #return the array of springs
    text = text.replace('\n','')
    return  re.split('[!.?]',text)

def createWords(text):
    return re.split('[,.!]',text)

def main(argv):
    
    isNegativeSentence = False
    
    #open up files 
    fnouns = open("BAD-Nouns.txt","r")
    fverbs = open("BAD-Verbs.txt","r")
    fmessage = open("Message.txt","r")
    
    
    #Using createSentences function to return only sentences in the given text
    sent = createSentences(fmessage.read())
    bnouns = createWords(fnouns.read())
    bverbs = createWords(fverbs.read())
    #For to check all the words in a sentence
    for i in sent:
        temp = i.split(' ')
        print (temp)
        #print (words)
        for j in bnouns:
            #print ("\t" + j.lower())
            for x in temp:
                if j.lower() == x.lower():
                    if j != '':
                        print ("\"" + j + "\" is negative noun!")
                        isNegativeSentence = True
        for j in bverbs:
            for x in temp:
                if j.lower() == x.lower():
                    if j != '':
                        print ("\"" + j + "\" is a negative verb!")
                        isNegativeSentence = True
        
        if isNegativeSentence == True:
            print("This sentence is negative!")
        else:
            print("This sentence has no negative words in it!")
        isNegativeSentence = False
        
        #print ("This sentence is made of these words:")
        #print(temp)
        print("\n")
    
    
    

if __name__ == "__main__":
    main(sys.argv[1:])
