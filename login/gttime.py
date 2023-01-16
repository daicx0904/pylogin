import time
def gettime():
    timelist = str(time.asctime()).split(' ')
    dict1 = {
        'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12
    }
    month = dict1[timelist[1]]#month
    day = timelist[2]#day
    year = timelist[4]#year
    hms= timelist[3]
    return f"{hms} {month}/{day}/{year}"
print(gettime())