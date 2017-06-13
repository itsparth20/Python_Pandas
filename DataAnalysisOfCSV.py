import pandas as pd
from datetime import datetime
from datetime import timedelta
from time import sleep

#Read the CSV file
df = pd.read_csv('Sample.csv')

#Create Dictionary 
dic = {'Initial':[],
         'Number':[],
         'Key':[],
         'EntryLocation':[],
         'EntryDate':[],
         'ExitLocation':[],
         'ExitDate':[]}

		 
#Convert String to datetme 
df['EntryDate'] = pd.to_datetime(df.EntryDate)
df['ExitDate'] = pd.to_datetime(df.ExitDate)

#Sort dataframe
df = df.sort_values(['Key', 'EntryDate'])

#Sets variable 
def setPrev(num, key, EL, ED, ExL, ExD):
    global prevNum
    global prevKey
    global prevEL
    global prevExL
    global prevED
    global prevExD
    prevNum = num
    prevKey = key
    prevEL = EL
    prevExL = ExL
    prevED = ED
    prevExD = ExD
    
#Get first row data from dataframe and set variables
row1 = df.iloc[0];
setPrev(row1['NUMBER'], row1['Key'], row1['EntryLocation'], row1['EntryDate'], row1['ExitLocation'], row1['ExitDate'])

#Store data to dictionary
def addIntoMap(prevNum, prevKey, prevEL, prevED, prevExL, prevExD):
    init = prevKey[:4]
    dic.get('Initial').append(init)
    dic.get('Number').append(prevNum)
    dic.get('Key').append(prevKey)
    dic.get('EntryLocation').append(prevEL)
    dic.get('EntryDate').append(prevED)
    dic.get('ExitLocation').append(prevExL)
    dic.get('ExitDate').append(prevExD)    

#iterate dataframe
for index, row in df.iterrows():
    
	#If key does not match then add previous data to dictionary
    if( prevKey != row['Key'] ):        
        addIntoMap(prevNum,prevKey,prevEL,prevED,prevExL,prevExD)
        setPrev(row['NUMBER'], row['Key'], row['EntryLocation'], row['EntryDate'], row['ExitLocation'], row['ExitDate'])      
		
    else:
		#if differnece between Current EntryDate and Previous ExitDate is less then or equal to one then change variable of exitDate
        diff = row['EntryDate'] - prevExD
        if ( diff.days <= 1):
            prevExL = row['ExitLocation']
            prevExD = row['ExitDate']
		#Else add data to Dictionary and set variables
        else:
            addIntoMap(prevNum,prevKey,prevEL,prevED,prevExL,prevExD)
            setPrev(row['NUMBER'], row['Key'], row['EntryLocation'], row['EntryDate'], row['ExitLocation'], row['ExitDate'])

#Add last row data to dictionary 			
addIntoMap(prevNum,prevKey,prevEL,prevED,prevExL,prevExD)

#Create our new data frame using dictionary and then create csv file using that new data frame
newDf = pd.DataFrame(dic)
newDf.set_index('Initial', inplace = True)
newDf.to_csv('output.csv')
