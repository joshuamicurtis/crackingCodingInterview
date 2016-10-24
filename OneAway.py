"""
    One Away
    There are three types of edits that can be performed on strings: insert a 
    character, remove a character, or replace a character. Given two strings, 
    write a function to check if they are one edit(or zero edits) away.
"""
def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    # Make sure that if one string is longer it is str2
    if len(str1) > len(str2):
        str1, str2 = str2, str1 
    editCount = 0
    for i in range(len(str1)):
        if str1[i] != str2[i] and str1[i] != str2[i+1]:
            editCount += 1
        if editCount > 1:
            return False
    return True

print one_away("pale","ple")
print one_away("pales","pale")
print one_away("pale","bale")
print one_away("pale","bake")