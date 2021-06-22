#creating new account id and password
import random
import re
#creating random account number
def acc_no():
    string=list("123456789098")
    random.shuffle(string)
    return ''.join(string)
def password(name,acc):
    string=list(acc)
    random.shuffle(string)
    pas=name+''.join(string)
    return pas
def username():
    string=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    random.shuffle(string)
    user=''.join(string)
    username=user[:11]
    return username
def validate(y):
    x=y
    symbol="[@#$%^&*()_+!;:,.<>?{}|~`]"
    if len(x)<10:
        return False
    if re.findall("[a-z]",x):
        if re.findall("[A-Z]",x):
            if re.findall("[0-9]",x):
                if re.findall(symbol,x):
                    return True
    return False
        
  
    



