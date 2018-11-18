# Create a path to the csv and read it into a Pandas DataFrame

import pandas as pd

budget_df = pd.read_csv('budget_data.csv')

budget_df.head()

# The total number of months included in the dataset

TotalMonths = len(budget_df.index)
print(TotalMonths)

# The total net amount of "Profit/Losses" over the entire period

Total = budget_df['Profit/Losses'].sum()
print(Total)

#The average change in "Profit/Losses" between months over the entire period

change_list = []
i=1
for row in range(0,len(budget_df["Profit/Losses"])-1):
   change = budget_df.iloc[i,1] - budget_df.iloc[i-1,1]
   change_list.append(change)
   i += 1

average = round(sum(change_list)/len(change_list),2)
average

#The greatest increase in profits (date and amount) over the entire period

greatest = max(change_list)
index1 = change_list.index(greatest)
month1 = budget_df.iloc[index1+1,0]

print(greatest)
print(month1)

#The greatest decrease in losses (date and amount) over the entire period

least = min(change_list)
index2 = change_list.index(least)
month2 = budget_df.iloc[index2+1,0]

print(least)
print(month2)

#print the analysis to the terminal and export a text file with the results
print('Financial Analysis')
print('----------------------------')
print('Total Months: {}'.format(TotalMonths))
print('Total: ${}'.format(Total))
print('Average Change: ${}'.format(average))
print('Greatest Increase in Profits: {}, ${}'.format(month1, greatest))
print('Greatest Decrease in Profits: {}, ${}'.format(month2, least))