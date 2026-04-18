student_name = str(input("Enter your Name: "))
weekly_budget = int(input("Enter weekly budget: "))

list_expenses = [
    ["1.Food & Drinks:","Lunch, snacks, coffee"],
    ["2.Transportaton:", "Bus, jeepney, ride-share"],
    ["3.Mobile/Internet:", "Load, data plan, Wifi top-up"],
    ["4.School Supplies:", "Notebook, pen, bond paper"],
    ["5.Entertainment:", "Games, movies, hangout"],

]
for row in range(len(list_expenses)):
    for col in range(len(list_expenses[row])):
        print(list_expenses[row][col], end=" ")
        print()

       
# for row in list_expenses:
#     for element in row:
#         print(element, end=" ")
#         print()
choice = int(input("Choose number 1 - 5: "))       
total = 0
while True:
    total +=1
    if choice == 1:
            print("Lunch at the cafeteria")
            continue
    elif choice == 2:
            print("Transportation")
            continue
    elif choice == 3:
            print("Mobile Plan")
            continue
    elif choice == 4:
            print("School Supplies")
            continue
    elif choice == 5:
            print("Entertainment")
            continue
    elif choice == 0:
            print("0 to skip")
            break
    else:
        print("Invalid choice")
