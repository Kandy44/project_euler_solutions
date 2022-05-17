from datetime import datetime
from dateutil.relativedelta import relativedelta

def counting_sundays(min_year,max_year):
    res = 0
    cur_date = datetime(min_year,1,1)
    while True:
        if cur_date.year == max_year+1:
            break
        if cur_date.weekday() == 6:
            res += 1
        cur_date = cur_date + relativedelta(months=1)
    return res

def main():
    res = counting_sundays(1901,2000)
    print(f"The answer for problem 19 is: {res}")

main()