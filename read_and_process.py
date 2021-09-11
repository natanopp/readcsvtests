## read_csv experiment
## method 2: read-and-process

# imports
import time
import pandas as pd
pd.set_option('display.width', None) # to see all columns

print('Method 2: Starting Experiment')
# timer starts
start = time.time()

# set column names
cols = ['Region', 'Country', 'Item Type', 'Sales Channel',
         'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Total Revenue']
# date parser
from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y')

# read data file
df = pd.read_csv('dataset/1500000SalesRecords.csv', nrows=1000000, usecols=cols,
                 dtype={'Order ID': str},
                 parse_dates=['Order Date', 'Ship Date'], date_parser=dateparse)

# display information
print('Show Infos:')
df.info()
print('')
print('Show Top Three Rows')
print(df.head(3))

# timer ends
end = time.time()
print('\nExperiment Completed\nTotal Time: {:.2f} seconds'.format(end-start))
