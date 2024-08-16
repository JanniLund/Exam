

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
url = 'https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv'
df = pd.read_csv(url)

# To get a understanding of the dataFrame
print(df.head())
print()


# # 1: Total Sales per Store for the Year 2014: 
# print(f'\n{"-"*20} Total Sales per Store for the Year 2014 {"-"*20}')
# # Beginning by change the date form being a string to be a value
# df['Date'] = pd.to_datetime(df['Date'])
# # Make a variable, there we only looking a dataFrame for juni 2014 
# yearDate = df[(df['Date'] >= '2014-01-01') & (df['Date'] <= '2014-12-30')]
# # The totalSales for the stores 
# total_sales_2014 = yearDate.groupby('Store')['Sales'].sum().round(2)
# df.set_index('Store', inplace=True) 
# df.rename(columns= {"Sales": "total_sales_2014"})
# print(df)
# # I'm trying to make total_sales_2014 become a column with the write an error
# # After that I will make it only give stores (index) and total_sales_2014

# # 2. Store with the Most Consistent Sales:	
# print(f'\n{"-"*20} Store with the Most Consistent Sales:{"-"*20}')
# salesStd = df.groupby('Store')['Sales'].std()
# # Identify the store with the smallest standard deviation
# store = salesStd.sort_values(by=["Sales"], ascending = False)
# print(store.iloc[0]) #get only the lowest output
# # It is not printing 

# 5. Sales Distribution by Day of the Week:
print(f'\n{"-"*20} Sales Distribution by Day of the Week:{"-"*20}')
# Extract day of the week from the 'Date' column
df['DayOfWeek'] = df['Date'].dt.day_name()
# Calculate average sales for each day of the week
avgSales = df.groupby('DayOfWeek')['Sales'].mean()
# Plot average sales by day of the week
plt.figure()
avgSales.plot(kind='bar', color='green')
plt.title('Average Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.savefig('2024 5.png')





