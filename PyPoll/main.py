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
file.write('Election Results \n')
file.write('by Tadeo Aguilar\n')
file.write('---------------------------------\n')
file.write(f"Total votes {votes}")
file.write('---------------------------------\n')



for k,v in dictCandidates.items():
    print(f"{k}: {round((v/votes)*100,3)}%  ({v})")
    file.write(f"{k}: {round((v/votes)*100,3)}%  ({v})\n")
#print(dictCandidate)
print('---------------------------------')
print(f'Winner:{max(dictCandidates,key=dictCandidates.get)}' )
file.write('---------------------------------\n')
file.write(f'Winner:{max(dictCandidates,key=dictCandidates.get)}\n' )
file.close()
print(f"File written to {filepath}")