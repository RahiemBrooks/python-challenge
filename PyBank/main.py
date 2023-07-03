file = open ("./Resources/budget_data.csv")
header = file.readline()
count = 0
net_profit = 0
average_change = 0
max_increase_profit = 0
max_increase_profit_date = ""
max_decrease_profit = 0
max_decrease_profit_date = ""

for line in file:
    count = count + 1
    line = line.strip()
    line = line.split (",")
    profit = line [1]
    date = line [0]
    profit = int(profit)
    
    if count >=2:
        change_in_profit = profit - previous_profit
        average_change = average_change + change_in_profit
        if change_in_profit > max_increase_profit:
            max_increase_profit = change_in_profit
            max_increase_profit_date = date
        if change_in_profit < max_decrease_profit:
            max_decrease_profit = change_in_profit
            max_decrease_profit_date = date
    previous_profit = profit
    net_profit = net_profit + profit
    
file.close()

average_profit = net_profit/count
average_change = average_change/(count - 1)


text_out = "Financial Analysis\n\n"
text_out += "----------------------------\n\n"
text_out += f"Total Months: {count}\n\n"
text_out += f"Total: ${net_profit}\n\n"
text_out += f"Average Change: ${round(average_change,2)}\n\n"
text_out += f"Greatest Increase in Profits: {max_increase_profit_date} (${max_increase_profit})\n\n"
text_out += f"Greatest Decrease in Profits: {max_decrease_profit_date} (${max_decrease_profit})\n\n"

print(text_out)

output_file = open ("./analysis/budget_data_output.txt","w")
output_file.write(text_out)
output_file.close()
