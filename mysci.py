# Read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}
# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float}

print(datafile.readline())
print(datafile.readline())
print(datafile.readline())
print(datafile.readline())

datafile.close()
