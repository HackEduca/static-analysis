# Zack Crenshaw

# Will run a batch of calls to run.py
# python3 batch.py (text file with commands)

# Structure of line of command file: (studio URL/ID),(grading script),(grade level), [--verbose]

import sys
from subprocess import call

def main():

    file = sys.argv[1].strip()

    print("Start batch of commands: \n")

    # iterate through folder
    with open(file,'r') as commands:
        next = commands.readline().split(',')
        for i in range (len(next)):
            next[i] = next[i].strip("\n ")
        while (len(next) > 1): # check for EOF
            # run the command
            if len(next) > 3: #if there is a verbose flag
                call(['python3','run.py',next[0],next[1],next[2],next[3]])
            else :  #if no verbose flag
                call(['python3','run.py',next[0],next[1],next[2]])
            next = commands.readline().strip().split(',')

    print("Finished batch.")


if __name__ == '__main__':
    main()