#this is a test with monthly data 202301 
 
import datatime
import pandas as pd

x = pd.to_datetime(currentMonth,format = '%Y%m')
print(currentMonth.strftime('%Y%m')) 
