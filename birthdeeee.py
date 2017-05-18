#NAME:JJAGWE MARTIN BULEGA
#REG NO.:16/U/295
#STUDENT NUMBER:21600254
#COURSE:BIOMEDICAL ENGINEERING
# birthday-pygame
#a program that gets information from the user and generates his/her birthday information
#this code is programed from python version 3.6.0
import datetime
firstname=input('What is  your first name : ')
surname=input('What is your surname : ')
day=input('When is your birth day (1-31)? : ')
monthnumber=input('Its in which month (1-12)? : ')
age=input('How old will you be ? : ')
yob=2017-(int(age))
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthname=months[(int(monthnumber))-1]
days=['st','nd','rd']+(['th']*17)+['st','nd','rd']+(['th']*7) + ['st']
dayending=days[(int(day))-1]
h=datetime.date(int(yob),int(monthnumber),int(day))
print('your name is' ,firstname, ' ' ,surname, 'and you were born on' ,day+dayending, ' ' ,monthname, ' ' ,yob, 'the week day was a' ,h.strftime('%a'))


