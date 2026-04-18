student_name = str(input("Enter your Name: "))
weekly_budget = int(input("Enter weekly budget: ")) 

list_expenses = [
    [1,"Food & Drinks: Lunch, snacks, coffee"], 
    [2,"Transportaton: Bus, jeepney, ride-share"],
    [3,"Mobile/Internet: Load, data plan, Wifi top-up"],
    [4,"School Supplies: Notebook, pen, bond paper"],
    [5,"Entertainment: Games, movies, hangout"],

]

list_budget = []

# loops
for row in list_expenses:
    for element in row:
        print(element, end=" ")
        print()
      
for i in range(4):
    print("Order", i + 1)

    choice = int(input("Choose number (0 is skip) 0-5: "))
 
    if choice >= 1:
        print(choice)
        description = str(input("Description: "))
        amount = int(input("Amount: "))
        if amount >= weekly_budget * .25:
             list_budget.append([choice, description, True, amount])
             continue
        list_budget.append([choice, description, False,amount])
    elif choice == 0:
        print("Skipped")
        break


print("=" * 50)
print(f"{student_name} - Weekly Expense Log")
print("=" * 50)
print(f"Weekly Budget: P{weekly_budget}")
total = 0
for z in range(len(list_budget)):
    choice = list_budget[z][0]
    total +=  list_budget[z][3]
    amount_int = list_budget[z][3]
    high_expenses = ""
    if list_budget[z][2]: 
        high_expenses = "! High Expenses Alert!"
    print(f"[{choice}] {list_expenses[choice-1][1]} \n {list_budget[z][1]:<45} P{amount_int} {high_expenses}")
print("-" * 50)
remaining = weekly_budget - total
sub_total = remaining

if remaining >= 0: 
    print(f"Total:", total)
    print(f"Remaining: ", remaining)
    print("Budget Okay! Keep it up.")
else:
    print("Overspent! Reduce spending.!")