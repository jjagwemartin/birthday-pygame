#NAME:JJAGWE MARTIN BULEGA
#REG NO.:16/U/295
#STUDENT NUMBER:21600254
#COURSE:BIOMEDICAL ENGINEERING
# birthday-pygame
#a program that gets information from the user and generates his/her birthday information
#this code is programed from python version 3.6.0
a=input('input your first name : ')
b=input('input your last name : ')
c=input('when is your birth day (1-31)? : ')
d=input('in which month (1-12)? : ')
e=input('how old are u going to be ? : ')
yob=2017-(int(e))
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
f=months[(int(d))-1]
days=['st','nd','rd','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','st','nd','rd','th','th','th','th','th','th','th','st']
g=days[(int(c))-1]

import datetime
h=datetime.date(int(yob),int(d),int(c))
print('your name is' ,a, ' ' ,b, 'and you were born on' ,c+g, ' ' ,f, ' ' ,yob, 'the week day was a' ,h.strftime('%a'))
