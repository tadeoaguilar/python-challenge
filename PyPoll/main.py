import os
import csv


header=True
csvpath = os.path.join('Resources','election_data.csv')
dictVotes=dict()
dictCandidates=dict()
x=0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        if header == True:
            header=False

        else:

            x=x+1
            if row[2] in dictCandidates:
                dictCandidates[row[2]] +=1
            else:
                dictCandidates[row[2]] =1



votes = x

filepath = os.path.join('analysis','analysis.txt')
file=open(filepath,"w")
print('Election Results')
print('by Tadeo Aguilar')
print('---------------------------------')
print(f"Total votes {votes}")
print('---------------------------------')
file.write('Election Results')
file.write('by Tadeo Aguilar')
file.write('---------------------------------')
file.write(f"Total votes {votes}")
file.write('---------------------------------')



for k,v in dictCandidates.items():
    print(f"{k}: {round((v/votes)*100,3)}%  ({v})")
    file.write(f"{k}: {round((v/votes)*100,3)}%  ({v})")
#print(dictCandidate)
print('---------------------------------')
print(f'Winner:{max(dictCandidates,key=dictCandidates.get)}' )
file.write('---------------------------------')
file.write(f'Winner:{max(dictCandidates,key=dictCandidates.get)}' )
file.close()
print(f"File written to {filepath}")