import calendar
import datetime as dt
T = 2
ls = ['Sun 10 May 2015 13:54:36 -0700',
      'Sun 10 May 2015 13:54:36 -0000',
      'Sat 02 May 2015 19:54:36 +0530',
      'Fri 01 May 2015 13:54:36 -0000']

def time_delta(t1, t2):
    tl1 = t1.split(); tl2 = t2.split()
    dt1 = dt.datetime(int(tl1[3]), list(calendar.month_abbr).index(tl1[2]), int(tl1[1]), int(tl1[4][0:2]), int(tl1[4][3:5]), int(tl1[4][6:8]))
    td1 = dt.timedelta(days=0, hours=int(tl1[5][0]+tl1[5][1:3]), minutes=int(tl1[5][0]+tl1[5][3:5]))
    dt2 = dt.datetime(int(tl2[3]), list(calendar.month_abbr).index(tl2[2]), int(tl2[1]), int(tl2[4][0:2]), int(tl2[4][3:5]), int(tl2[4][6:8]))
    td2 = dt.timedelta(days=0, hours=int(tl2[5][0]+tl2[5][1:3]), minutes=int(tl2[5][0]+tl2[5][3:5]))
    date1 = dt1-td1    
    date2 = dt2-td2
    print(int(abs((date2-date1).total_seconds())))
    

for t_itr in range(T):
        t1 = ls[t_itr*T]
        t2 = ls[t_itr*T+1]

        time_delta(t1, t2)