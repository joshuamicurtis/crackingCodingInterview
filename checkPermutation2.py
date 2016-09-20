import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        print "Strings are not permutations of each other"
        return -1
        
    str1 = list(str1)
    str2 = list(str2) 
    char_set = []
    
    for i in range(128):
        char_set.append(0)
    for char in str1:
        char_set[ord(char)] += 1
    for char in str2:
        char_set[ord(char)] -= 1
        if (char_set[ord(char)] < 0):
            print "Strings are not permutations of each other"
            return -1
    print "Strings are permutations"
    return 0

checkPermutation(str1, str2)