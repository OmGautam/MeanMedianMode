import csv
from collections import Counter

with open('SOCR-HeightWeight.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    newNum = fileData[i][1]
    newData.append(float(newNum))
n = len(newData)
total = 0
for x in newData:
    total +=x
mean = total/n
print("Mean is: " + str(mean))

newData.sort()
if n%2 == 0:
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1+m2)/2
else:
    median = newData[n//2]

print("Median is: " + str(median))

data = Counter(newData)
r = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurance in data.items():
    if(50<float(height)<60):
        r["50-60"] += occurance
    elif(60<float(height)<70):
        r["60-70"] += occurance
    elif(70<float(height)<80):
        r["70-80"] += occurance

modeRange, modeOccurance = 0, 0

for range,occurance in r.items():
    if(occurance>modeOccurance):
        modeRange, modeOccurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance
mode = float((modeRange[0]+modeRange[1])/2)
print(f"Mode is: {mode}")