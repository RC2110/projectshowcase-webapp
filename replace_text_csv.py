import csv
import pandas as pd
#
# data = pd.read_csv("data.csv", sep=';')
# print(data['url'])
#
# for i, rows in data.iterrows():
#     rows['url']=rows['url'].replace("https://pythonhow.com","https://github.com/RC2110?tab=repositories")
# print(data['url'])
# reading the CSV file
text = open("data.csv", "r")
# ls= [i for i in text]
# print(ls)
#
# #join() method combines all contents of
# # csvfile.csv and formed as a string
text = [''.join([i for i in text])]
text1 = ''.join([i for i in text]) # look at the difference
print(text)
print(text1)
#
# # search and replace the contents
# text = text.replace("https://pythonhow.com", "https://github.com/RC2110?tab=repositories")
# # print(text)
#
# # output.csv is the output file opened in write mode
# x = open("data1.csv",'w')

# all the replaced text is written in the output.csv file
# for i, rows in data.iterrows():
#     x.writelines(data)
# x.close()
#
#
# print(data1)