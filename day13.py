#PANDAS
import pandas as pd
# df = pd.Series([10,20,30])
# print(df)
# print(df[0])

#dict
# dict = {"name": ["dheeraj","kunal","praveen","anjali","abhishek singh"],
#         "age" : [20,21,22,23,24],
#         "salary" : [{"In hand":"1500","ctc":"1.2lpa"},{"In hand":"2000","ctc":"2.2lpa"},
#                     {"In hand":"2500","ctc":"3.2lpa"},{"In hand":"3300","ctc":"3.2lpa"},
#                     {"In hand":"4000","ctc":"4.2lpa"},]}
# df = pd.DataFrame(dict)
# print(df)     



#dict2
# dict = {"name":["dheeraj","kunal","praveen","anjali","abhishek singh"],
#         "age":[20,21,22,23,30],
#         "salary":[15000,20000,25000,30000,35000]
#         }
# df = pd.DataFrame(dict)
# print(df)





#csv
# from google.colab import drive
# drive.mount('/content/drive')
# url = '/content/drive/MyDrive/file1.csv'
# df = pd.read_csv(url)


import pandas as pd
df = pd.read_csv("file1.csv")
print(df.head())

#json