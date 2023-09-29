import random
import datetime
birthday=[]
i=0
while(i<50):
    year=random.randint(1993,2009)
   # print(year)
    if(year%4==0 and year%100!=0 or year%400==0):
      #  print("the year is a leap year")
        leap=1
    else:
       # print("the year is not a leap year")
        leap=0
    month=random.randint(1,12)
  #  print(month,"/")
    if (month==2):
        if (leap==1):
            day=random.randint(1,29)
           # print(day,"/")
        elif(leap==0):
            day=day=random.randint(1,28)
           # print(day,"/")
    elif(month%2==0 and month!=2):
        if(month<7):
            day=random.randint(1,30) #april june
           # print(day,"/")
        elif(month>7):
            day=random.randint(1,31) #august october december
          #  print(day,"/")
    elif(month%2!=0 and month!=2):
        if(month<7):
            day=random.randint(1,31) #january march may july
          #  print(day,"/")
        elif(month>7):
            day=random.randint(1,30) #september november
           # print(day,"/")
    else:
        print("invalid month")
    i+=1
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    birthday.append(day_of_year)
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i+=1