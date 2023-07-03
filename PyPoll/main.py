# create an empty dictionary
ballots = {}
total_votes = 0
# open file
with open("./Resources/election_data.csv", "r") as file:
    # read the header line
    header = file.readline()
    
    for line in file:
        line = line.strip()
        line = line.split (",")
       
        name = line[2]
        
        total_votes += 1
        if name in ballots:
            ballots[name] += 1
        
        else:
            ballots[name] = 1
        
text_out = "Election Results\n\n"
text_out += "-------------------------\n\n"
text_out += f"Total Votes: {total_votes}\n\n"
text_out += "-------------------------\n\n"


for name,votes in ballots.items():
    perc = votes/total_votes*100
    text_out += f"{name}: {round(perc,3)}% ({votes})\n\n"
text_out += "-------------------------\n\n"

votes_list = list(ballots.values())
candidates_list = list(ballots.keys())
highest_vote = max(votes_list)

v_index = votes_list.index(highest_vote)


winner = candidates_list[v_index]

text_out += f"Winner: {winner}\n\n"
text_out += "-------------------------\n\n"

print (text_out)

output_file = open ("./analysis/election_data.txt","w")
output_file.write(text_out)
output_file.close()
