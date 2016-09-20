import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        print "Strings are not permutations of each other"
        return -1
        
    str1 = list(str1)
    str2 = list(str2)   
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                str2.remove(char2)
                break
        if len(str2) == 0:
            print "Strings are permutations"
            return 0
    else:
        print "Strings are not permutations of each other"
        return -1
               
checkPermutation(str1, str2)