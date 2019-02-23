# Anthony Davis Blockchain Assignment 2  (Feb. 19, 2019)

# Libraries used
import hashlib
import sys
import time

timeStart = time.time()
# Opening file that holds all the words we want to check
file = open("wordCheck.txt","r")
look = file.read()

# Storing words in file into array
arr = []
arr = look.split()

# Function for finding matched hashed word
def findMatch(x):
    count = 0
    for x in arr:
        daHash = hashlib.sha1(x)
        miHash = daHash.hexdigest()
        if ( miHash == firHash ):
            print("Found Hash Match")
            print("\tNumber of Attempts: " + str(count))
            print("\tMatch Word: " + x + "\n")
            break;
        count += 1
    return x

# Function for salted hashes
def findMatch2(y,w):
    mainHash = w
    concat = y
    count = 0
    for x in arr:
        addCheck = concat + x
        daHash = hashlib.sha1(addCheck)
        miHash = daHash.hexdigest()
        if ( miHash == mainHash ):
            print("Found Final Hash Match")
            print("\tNumber of Attempts: " + str(count))
            print("\tMatch Word: " + y + x + "\n")
            break;
        count += 1
    return x

# Checking parameters and given task for each
if ( len(sys.argv)<=1 or len(sys.argv)>3):
    print("Error: Give one or two parameters (not including filename)")
elif ( len(sys.argv) == 2):
    firHash = sys.argv[1]
    findMatch(firHash)
elif ( len(sys.argv) == 3):
    firHash = sys.argv[1]
    secHash = sys.argv[2]
    saltWord = findMatch(firHash)
    findMatch2(saltWord,secHash)
file.close()
timeEnd = time.time()
print("Program runtime is: " + str(timeEnd - timeStart) +"\n")
