import sys

str = sys.argv[1]

def palindromePermutation(str):
    print str
    odd_count = 0
    char_set = []
    for i in range(128):
        char_set.append(0)
    
    for char in str:
        char_set[ord(char)] += 1
    for i in char_set:
        if (i % 2) == 1:
            odd_count += 1
        if odd_count > 1:
            print "False: String is not a palindrome" 
            return False     
    print "oddcount is:", odd_count
    print "True: String is a palindrome" 
    return True

palindromePermutation(str)

