fat = float(input())
snf = float(input())
total_quantity = float(input())
cost_per_liter = round(((fat/100)*1*327)+((snf/100)*1*(2/3)*327),2)
total_cost = round(((fat/100)*total_quantity*327)+((snf/100)*total_quantity*(2/3)*327),2)
print("The cost of milk per liter is Rs:",cost_per_liter)
print("The total cost of milk is Rs:",total_cost)