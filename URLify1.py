import sys 

def URLify():
    print "Enter a string"
    str = raw_input()
    strLen = len(str)
    print strLen
    strList = list(str)
    for char in range(strLen):
        if strList[char] == ' ':
            strList[char] = '%20'
    print strList
    strOut = ''.join(strList)
    print strOut
URLify()