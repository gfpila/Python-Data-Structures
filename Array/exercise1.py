"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

#LIST
monthlyExpenses = [2200, 2350, 2600, 2130, 2190]

#1
febJanurayDifference = monthlyExpenses[1] - monthlyExpenses[0]
print(f"The difference between February and Januray expenses was {febJanurayDifference}.")

#2
firstQuarterExpense = 0
for expense in monthlyExpenses[0:3]:
    firstQuarterExpense = expense + firstQuarterExpense
print(f"I spent {firstQuarterExpense} in the first quarter of the year.")

#3
if 2000 in monthlyExpenses:
    print("I spent exactly 2000 in a month!")
else:
    print("I did not spent exactly 2000 in a month!")

#4
monthlyExpenses.append(1980)
print(f"My expenses in June was {monthlyExpenses[5]}.")

#5
print(f"I spent {monthlyExpenses[3]} in April but i returned an item for 200 so i actually spent:", end=' ')
monthlyExpenses[3] = monthlyExpenses[3] - 200
print(f"{monthlyExpenses[3]}")