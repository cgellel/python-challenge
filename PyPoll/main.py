# Create a path to the csv read it into a Pandas DataFrame

import pandas as pd
csv_path = "PyPoll/Resources/election_data.csv"
poll_df = pd.read_csv(csv_path)

#display first five rows

poll_df.head()

#display total number of votes cast

total_votes = len(poll_df.index)
print(total_votes)

# Display complete list of candidates who received votes

candidates_list = poll_df['Candidate'].unique()
candidates_list

# Total number of votes each candidate won

candidate_votes = poll_df['Candidate'].value_counts()
candidate_votes

# Percentage of votes each candidate won

candidate_percentage = 100. * poll_df['Candidate'].value_counts() / len(poll_df.index)
candidate_percentage = round(candidate_percentage, 2)
candidate_percentage

# Winner of the election based on popular vote.

most_votes = max(candidate_votes)
winner_index = list(candidate_votes).index(most_votes)
winner = candidate_votes.index[winner_index]
print(winner)

#print the analysis to the terminal and export a text file with the results

output = ("Election Results\n"
          "----------------------------\n"
          f"Total Votes: {total_votes}\n"
          "----------------------------\n"
          f"{candidate_percentage}\n"
          "----------------------------\n"
          f"Winner: {winner}\n"
          "----------------------------\n")

print(output)

#write text file with results

with open('ElectionResultsOutput.txt', 'w') as election:
    election.write(output)    