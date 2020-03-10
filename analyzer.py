
def main():
    #open up files 
    fnouns = open("BAD-Nouns.txt","r")
    fverbs = open("BAD-Verbs.txt","r")
    fmessage = open("Message.txt","r")
    
    #printing contenet of file
    if fmessage.mode == "r":
        contents = fmessage.read()
        print(contents)

        
if __name__ == "__main__":
    main()
