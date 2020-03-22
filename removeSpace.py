
import sys

def main(argv):
    
    i = 1
    while i < len(sys.argv):
        fnounsr = open(sys.argv[i],"r")
        
        #fverbsr = open("BAD-Verbs.txt","r")
        #fverbsw = open("BAD-Verbs.txt","w+")
        temp = fnounsr.read()
        temp = temp.replace(' ','')
        temp = temp.replace('\n','')
        fnounsr.close()
    
        fnounsw = open(sys.argv[i],"w+")
        fnounsw.write(temp)
        fnounsw.close()
        i=i+1

if __name__ == "__main__":
    main(sys.argv[1:])
