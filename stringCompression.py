"""
    String Compression
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabccccaaa would become a2b1c5a3.
    If the "compressed" string would not become smaller than the original string, your 
    method should return the original string. You can assume the string has only upper
    and lowercase letters.
"""
def string_compression(str1):
    result = []
    letterCount = 1
    for i in range(len(str1)-1):
        if str1[i] == str1[i+1]:
            letterCount += 1
        else:
            num = str(letterCount)
            charAndNum = str1[i].join(num)
            result.append(charAndNum)
    str2 = ''.join(result)
    if len(str2) < len(str1):
        return str1
    else:
        return str2

print string_compression("abcdefg")
print string_compression("aaaaaaa")