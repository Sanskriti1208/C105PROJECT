#importing necessary modules
import csv
import math

#storing data as array
with open('data.csv') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

#calculating mean for standard deviation
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean

#subtracting the mean from each data and the squaring it
squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

#adding all the data
sum = 0
for i in squared_list:
    sum += int(i)

#taking out the square root of the result
result = sum/(len(data)-1)
standard_deviation = math.sqrt(result)
print("The standard deviation of the given data is",standard_deviation)