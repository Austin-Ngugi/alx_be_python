from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)

def calculate_future_date():
    tdelta = timedelta(days=7)
    future_date = date.today() + tdelta
    print(future_date)

display_current_datetime()  
calculate_future_date()  
    