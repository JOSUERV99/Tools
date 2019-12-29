from sys import argv
import subprocess

#The program can replies himself, any times
times = 10

script = argv  
script_name = str(script[0])

for i in range(0, times):
    dir = 'dir'+str(i)
    subprocess.call(['mkdir', dir])
    subprocess.call(['cp', script_name, dir])
print("Success")