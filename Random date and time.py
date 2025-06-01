import time
import random
def getrandomDate(startDate , endDate):
    print("Printing random date between ",startDate,"and",endDate)
    randomgenarator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startDate ,dateformat ))
    endtime = time.mktime(time.strptime(endDate ,dateformat ))
    randomtime = starttime +randomgenarator * (endtime - starttime)
    randomdate =  time.strftime(dateformat , time.localtime(randomtime))
    return randomdate
print("Random Date = ",getrandomDate("1/1/2016" , "12/12/2018"))