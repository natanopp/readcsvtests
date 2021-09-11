## read_csv experiment
## method 1: read-then-process

# imports
import time
import pandas as pd
pd.set_option('display.width', None) # to see all columns

print('Method 1: Starting Experiment')
# timer starts
start = time.time()

# read data file
df = pd.read_csv('dataset/1500000SalesRecords.csv')

# processing data
# select top 1M
df = df.head(1000000)
# select some columns
df = df[['Region', 'Country', 'Item Type', 'Sales Channel',
         'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Total Revenue']]
# order ID casting
df['Order ID'] = df['Order ID'].astype(str)
# order date casting
df['Order Date'] = pd.to_datetime(df['Order Date'])
# ship date casting
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# display information
print('Show Infos:')
df.info()
print('')
print('Show Top Three Rows')
print(df.head(3))

# timer ends
end = time.time()
print('\nExperiment Completed\nTotal Time: {:.2f} seconds'.format(end-start))
