import re
import pandas
def preprocess(data):
    pattern ="\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\S{2}\s-\s"
    message=re.split(pattern,data)[1:]
    dates=re.findall(pattern,data)
    df=pd.DataFrame({"message":message,"date":dates})
    user=[]
    message=[]
    for mess in df["message"]:
        data=re.split('([\w\W]+?):\s',mess)
        if data[1]:
            user.append(data[1])
            message.append(data[2])
        else:
            user.append("group_notification")
            message.append(data[0])
    df["message"]=message
    df["user"]=user
    year=[]
    for i in df['date']:
        if i[1]=='/':
            if i[3]=='/':
                year.append('20'+i[4:6])
            else:
                year.append('20'+i[5:7])
        else:
            if i[4]=='/'and i[2]=='/':
                year.append('20'+i[5:7])
            else:
                year.append('20'+i[6:8])
    df['year']=year
    month=[]
    for i in df['date']:
        if i[2]=='/':
            month.append(i[0:2])
        else:
            month.append(i[0:1])
    df['month']=month
    hours=[]
    minutes=[]
    unit=[]
    for i in df['date']:
            hours.append(i[-11:-9])
            minutes.append(i[-8:-6])
            unit.append(i[-5:-3])
    df["hours"]=hours
    df["minutes"]=minutes
    df["unit"]=unit
    date=[]
    for i in df['date']:
        if i[2]=='/':
            if i[5]=='/':
                date.append(i[3:5])
            else:
                date.append(i[3:4])
        else:
            if i[4]=='/':
                date.append(i[2:4])
            else:
                date.append(i[2:3])
    df['date']=date
    return df
