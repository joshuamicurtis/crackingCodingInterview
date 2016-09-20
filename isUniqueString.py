import sys

str = sys.argv[1]

def isUnique(str):
    if len(str) > 128:
        print "String does not have all unique characters"
        return -1
    
    char_set = []
    for i in range(128):
        char_set.append(0)
    for char in str:
        if char_set[ord(char)] == 1:
            print "String does not have all unique characters"
            return -1
        char_set[ord(char)] = 1 
    print "String has all unique characters"
    return 1
    
        
isUnique(str)