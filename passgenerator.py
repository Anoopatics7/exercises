from hashlib import sha224
import string
import random

if __name__=='__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.punctuation
    s4=string.digits
    pass_Length= int(input("enter the length of the pass word required : "))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("your password is :")
    print("".join(s[0:pass_Length]))
