import datetime
import json
import sys
import boto3

print('Input MealDate.\nyyyymmdd or Hit Enter to set today')
inputdata = input('>>> ')

if len(inputdata.rstrip()) == 0:
  mealdate = int('{0:%Y%m%d}'.format(datetime.datetime.now()))
elif len(inputdata.rstrip()) == 8:
  mealdate = int(inputdata)
else:
  print('Invalid MealDate!')
  sys.exit()

print('mealdate = ',mealdate)

mealdatestr = str(mealdate)
mealdatedt = datetime.datetime.strptime(mealdatestr,'%Y%m%d')

#print('mealdatestr = '+mealdatestr)

mealdatewday = mealdatedt.strftime('%a')

print('todaywday = '+mealdatewday)

mealtimelist = ['MOR','LUN','DIN']
#mealtime = 'MOR'

for mealtime in mealtimelist:
  print('MealTime is '+mealtime)
  print('Input MealMethod.\nCandidate:"Hom","Out","Onl","Nop","Buy"')
  mealmethod = input('>>> ')
  mealmethodcand = ['Hom','Out','Onl','Nop','Buy']
  
  if not any((s == mealmethod) for s in mealmethodcand):
    print('Invalid MealMethod!')
    sys.exit()
  
  dic = {}
  
  dic["MealTime"] = mealtime
  dic["Date"] = mealdate
  dic["Day_of_week"] = mealdatewday
  dic["MealMethod"] = mealmethod
  
  json_dict = json.dumps(dic)
  print(json_dict)
  
  bucket_name = "mealhistory"
  obj_name = "mealhistoryItem.mh"
  s3 = boto3.resource('s3')
  obj = s3.Object(bucket_name,obj_name)
  
  r = obj.put(Body = json_dict)

