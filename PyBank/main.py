import os
import csv


x=0
csvpath = os.path.join('Resources','budget_data.csv')
dictBudget=dict()
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        dictBudget = {row[0]:float(row[1]) for row in csvreader}



numMonths = len(dictBudget)
numMonths

totAmount = sum(dictBudget.values())
totAmount

totAmount = sum(dictBudget.values())
totAmount

change=list(dictBudget.values())
listChange = list()
size=len(change)-1

listChange.append(0)
for x  in range(size):
    if x == size:
        break
    else:
        listChange.append(change[x+1]-change[x])


dictMonths = dictBudget.keys()

dictChange = dict(zip(dictMonths,listChange))

print ("Financial Analysis \n")
print("By Tadeo Aguilar \n")
print("------------------------------ \n")
print(f'Total Months: {numMonths} ')
print(f"Total:${totAmount}")
print(f"Average Change:{round(sum(listChange)/(len(listChange)-1),2)}")
print(f'Greatest Increase in Profits: {max(dictChange,key=dictChange.get)} (${dictChange[max(dictChange,key=dictChange.get)]})')
print(f'Greatest Decrease in Profits: {min(dictChange,key=dictChange.get)} (${dictChange[min(dictChange,key=dictChange.get)]})')


filepath = os.path.join('analysis','analysis.txt')
file=open(filepath,"w")
file.write("Financial Analysis \n")
file.write("By Tadeo Aguilar \n")
file.write("------------------------------ \n")
file.write(f'Total Months: {numMonths} \n')
file.write(f"Total:${totAmount}\n")
file.write(f"Average Change:{round(sum(listChange)/(len(listChange)-1),2)}\n")
file.write(f'Greatest Increase in Profits: {max(dictChange,key=dictChange.get)} (${dictChange[max(dictChange,key=dictChange.get)]})\n')
file.write(f'Greatest Decrease in Profits: {min(dictChange,key=dictChange.get)} (${dictChange[min(dictChange,key=dictChange.get)]})\n')
file.close()
print(f"File written to {filepath}")