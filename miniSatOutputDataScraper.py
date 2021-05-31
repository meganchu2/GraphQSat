import os
import csv

inputdir = './data/uf100-430/minisat_results/'
outputfile = './data/uf100-430/uf100-430-minisat-data.tsv'

with open(outputfile, 'wt') as o:
    mat = ['file', 'Number of variables', 'Number of clauses', 'Parse time (s)', 'Simplification time (s)', 'restarts', 'conflicts', 'decisions', 'propagations', 'conflict literals', 'Memory used (MB)', 'CPU time (s)', 'Satisfiability']
    tsv_writer = csv.writer(o, delimiter='\t')
    tsv_writer.writerow(mat)
    for result in os.listdir(inputdir):
        if result.endswith(".txt"):
            with open(inputdir+result, "r") as f:
                print(result)
                data = [result]
                lines = [line.rstrip('\n') for line in f]
                #Num variables
                data.append(lines[4-1].split(':')[1].rstrip(' ').rstrip('\n'))
                #Num clauses
                data.append(lines[5-1].split(':')[1].rstrip(' ').rstrip('\n'))
                #Parse time
                data.append(lines[6-1].split(':')[1].split('s')[0].rstrip(' ').rstrip('\n'))
                
                #check for eliminated clauses line
                x = 1
                if lines[7-1].split(':')[0].split('|')[1] == '  Eliminated clauses':
                    x = 0       
                
                #Simp time
                data.append(lines[7-x].split(':')[1].split('s')[0].rstrip(' ').rstrip('\n'))
                
                y = 13
                while len(lines[y-x].split('=')) < 75:
                    y += 1
                y+=1
                #restarts
                data.append(lines[y-x].split(': ')[1].split(' ')[0])
                #conflicts
                data.append(lines[y+1-x].split(': ')[1].split(' ')[0])
                #decisions
                data.append(lines[y+2-x].split(': ')[1].split(' ')[0])
                #propagations
                data.append(lines[y+3-x].split(': ')[1].split(' ')[0])
                #conflict literals
                data.append(lines[y+4-x].split(': ')[1].split(' ')[0])
                #Memory used
                data.append(lines[y+5-x].split(': ')[1].split(' ')[0])
                #CPU time
                data.append(lines[y+6-x].split(': ')[1].split(' ')[0])
                #Satisfiability
                data.append(lines[y+8-x].rstrip(' ').rstrip('\n'))
                tsv_writer.writerow(data)