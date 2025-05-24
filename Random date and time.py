import time
import random
def getrandomDate(startdate , enddate):
    print("Printing random date between ",startdate,"and",enddate)
    randomgenarator = random.random()
    dateformat = ('%m / %d / %y')
    starttime = time.mktime(time.strptime(startDate ,dateformat ))
    endtime = time.mktime(time.strptime(endDate ,dateformat ))
    randomtime = starttime +randomgenarator * (endtime - starttime)
    randomdate =  time.strftime(dateformat , time.localtime(randomtime))
    return randomdate
print("Random Date = ",getrandomDate("1/1/2016 , 12/12/2018"))