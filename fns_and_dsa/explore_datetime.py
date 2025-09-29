import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)

def calculate_future_date():
    t_date = datetime.date.today()
    tdelta = datetime.timedelta(days=7)
    future_date = t_date + tdelta
    print(future_date)

display_current_datetime()  
calculate_future_date()  
    
    

#date = datetime.date(2025, 1 , 2)
#print (date)
#today = datetime.date.today()
#time = datetime.datetime.now()
#print(time)