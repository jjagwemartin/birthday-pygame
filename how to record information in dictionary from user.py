#how to get information from a person
info={}
info['name']=input('what is your name : ')
print('now we need your location, if u come from hostel/hall type H and if from home type HH')
x=input('which is which H or HH? : ')
if x=='H':
    #print('Now on the hostel information  you type the hostel name and rm number with a space in between')
    info['Hostel/Hall']=input('which hostel? : ')
    info['room']=input('which room? : ')
else :
        print('ooh you come from home')
        info['location']=input('where is your home located? : ')
info['age']=input('how old are u? : ')
info['former school']=input('your former sec. school plz? : ')
d=input('if on government type G and on private type PS : ')
if d=='PS':
    print('what where you doing as others were seriously crashing UACE ????')
else:
    print('congs, hard work pays now feel the govnment benefits')
info['Admission type']=d
print(info)
print('thank u, till next tym')
