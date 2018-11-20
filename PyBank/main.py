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

highest = max(change_list)
index1 = change_list.index(highest)
highestmonth = budget_df.iloc[index1+1,0]

print(highest)
print(highestmonth)

#The greatest decrease in losses (date and amount) over the entire period

lowest = min(change_list)
index2 = change_list.index(lowest)
lowestmonth = budget_df.iloc[index2+1,0]

print(lowest)
print(lowestmonth)

#print the analysis to the terminal and export a text file with the results
output = ("Financial Analysis\n"
          "----------------------------\n"
          f"Total Months: {TotalMonths}\n"
          f"Total: ${Total}\n"
          f"Average Change: ${average}\n"
          f"Greatest Increase in Profits: {highestmonth}, ${highest}\n"
          f"Greatest Decrease in Profits: {lowestmonth}, ${lowest}"
         )
print(output)

#write text file with results
with open('FinancialAnalysisOutput.txt', 'w') as FAO:
    FAO.write(output)   