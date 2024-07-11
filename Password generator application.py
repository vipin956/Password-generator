import string
import random

def passgen():
    s1 = string.ascii_lowercase  # to use the lowercase letters
    s2 = string.ascii_uppercase  # to use the uppercase letters
    s3 = string.digits           # to use the numbers
    s4 = string.punctuation      # to punctuate
    pass_length = int(input("enter the length of the password : \n")) #\n = new tab
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)  # to shuffle the list everytime while before running
    password = (" ".join(s[0:pass_length]))
    print(password)
    
passgen()    