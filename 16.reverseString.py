def  rev_str(str1):
    if len(str1)==0:
        return str1
    else:
        return str1[::-1]
    
str1=input("enter a string=")
print("reversed string is=",rev_str(str1))