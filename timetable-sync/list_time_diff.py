#Import Packages
import pandas as pd

#Read CSV
df = pd.read_csv('./sample-timetable.csv')

#Convert Time Column to String in HH:MM Format
def strdatetime(x):
    sub = []
    substr = ""
    y = str(x)
    if len(y) == 3:
        for i in y:
            sub.append(i)
        sub.insert(0,'0')
        sub.insert(2,':')
    elif len(y) == 4:
        for i in y:
            sub.append(i)
        sub.insert(2,':')
    for i in sub:
        substr += i
    return substr
    
#Function to convert seconds to minutes
def seconds_to_minutes(x):
    y = x/60
    return int(y)

def list_of_time_diff(df):
    
    #Apply the above function to convert time column to string in HH:MM format
    df['Time'] = df['Time'].apply(strdatetime)

    #Convert to datetime type, in seconds
    df_time= pd.to_datetime(df['Time'],format= '%H:%M' ).diff().dt.seconds


    
    #Convert time to minutes, and put in list
    time_list = df_time.iloc[1:].apply(seconds_to_minutes).tolist()
    
    return time_list
  
list_of_time_diff(df)