import sys

def getInput():
    print "Enter a string"
    str = raw_input()
    strLen = len(str)
    print strLen
    strList = list(str)
    i = 0
    while i < strLen:
        if strList[i] == ' ':
            strList.extend([' ',' ',' '])
        i += 1
    return strList, strLen

def URLify(strList, strLen):
    spaceCount = 0
    for i in range(strLen):
        if strList[i] == ' ':
            spaceCount = spaceCount + 1
    
    index = strLen + spaceCount * 2
    while i >=0:
        if strList[i] == ' ':
            strList[index - 1] = '0'
            strList[index - 2] = '2'
            strList[index - 3] = '%'
            index = index - 3
        else:
            strList[index -1] = strList[i]
            index = index - 1
        i = i - 1

    print strList
    strOut = ''.join(strList)
    print strOut

strList, strLen = getInput()
URLify(strList, strLen)