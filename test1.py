import datetime 


def check_datetime():
    initinaldate =input("please enter start date in  1/12/2022  formate")
    initinaldate = datetime.datetime.strptime(initinaldate, "%d/%m/%Y")

    lastdate =input("please enter end date in  1/12/2022 formate")
    lastdate = datetime.datetime.strptime(lastdate, "%d/%m/%Y")

    user_date1 = input("please enter user_start date in  1/12/2022 formate")
    user_date1 = datetime.datetime.strptime(user_date1, "%d/%m/%Y")

    user_date2 = input("please enter user_end date in  1/12/2022 formate")
    user_date2 = datetime.datetime.strptime(user_date2, "%d/%m/%Y")
    time1 = input("please enter start time in 12:00 formate ")
    time1 = datetime.datetime.strptime(time1, "%H:%M")
    time2 = input("please enter end time in 12:00 formate ")
    time2 = datetime.datetime.strptime(time2, "%H:%M")

    user_time1 = input("please enter start user_time in 12:00 formate ")
    user_time1 = datetime.datetime.strptime(user_time1,"%H:%M")
    user_time2 = input("please enter end user_time in 12:00 formate ")
    user_time2 = datetime.datetime.strptime(user_time2,"%H:%M")


    if user_date1 > initinaldate and user_date2 < lastdate:
        if user_time1 >= time1 and user_time2 <= time2:
            return True
        else:
            return False    

        
    else:
        print(False) 


print(check_datetime())        
           



    