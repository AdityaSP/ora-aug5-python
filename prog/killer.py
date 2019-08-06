import subprocess

output = subprocess.check_output("tasklist", shell=True).decode().split("\n")[3:-1]

pids = [line.split()[1] for line in output if 'MicrosoftEdge' in line]

for pid in pids:
    subprocess.call("taskkill /F /PID " + pid, shell=True)


#tasklist 

#VERSION 1
#import subprocess
#
#output = subprocess.check_output("tasklist", shell=True).decode()
##print(output[:200])
#
#output_lines = output.split("\n")[3:-1]
##print(output_lines[:5])
#
#
#edge = list(filter(lambda line: 'MicrosoftEdge' in line, output_lines))
##print(edge)
#edge = [line for line in output_lines if 'MicrosoftEdge' in line]
##print(edge)
#
#pids = list(map(lambda x : x.split()[1], edge))
##print(pids)
#pids = [ line.split()[1] for line in edge]
##print(pids)
#
#
#for pid in pids:
#    subprocess.call("taskkill /F /PID " + pid, shell=True)
#tasklist 
#ps -ef


#taskkill /PID <pid>
#kill -9 <pid>

