def string_rotation(s1, s2):
    if len(s1) != len(s2) and len(s1) > 0:
        return False
    s1 = s1+s1
    #print s1
    if s1.find(s2) != -1:
        return True
    
    """for i in range(len(s1)): 
        if s1[i] == s2[0]:
            rotationPoint = i
    for i in range(len(s2)):
        if s1[i + rotationPoint] != s2[i]:
            return False"""
    return False
    
    
s1 = "waterbottle"
s2 = "bottlewater"
#s3 = s1 + s1
#print s3.find(s2)
print string_rotation(s1, s2)