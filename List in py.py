
#        0    1   2   3   4
revenue=[50, 60, 70, 80, 90] # This is a list of revenue values for different months.
expenses=[10, 20, 30, 40, 50] # This is a list of expenses values for different months.
print(type(revenue)) # This will output the type of the variable 'revenue', which is <class 'list'> since it is assigned a list of integer values.
print(revenue) # This will output the value of the variable 'revenue', which is a list.
print(revenue[0]) # This will output the first element of the list 'revenue', which is 50.
print(revenue[-1]) # This will output the last element of the list 'revenue', which is 90.
print(revenue[1:4]) # This will output a slice of the list 'revenue', which is [60, 70, 80].
print(revenue[::2]) # This will output every second element of the list 'revenue', which is [50, 70, 90].
print(revenue[0:1:2]) # This will output the first element of the list 'revenue', which is [50].
print(len(revenue)) # This will output the length of the list 'revenue', which is 5 in this case.





# For loop to iterate through the list 'revenue' and print each element.
for rev in revenue:
    #print(revenue[0:1:2]) # This will output the first element of the list 'revenue', which is [50].
    print("Revenue:", rev)
margins=[]

for i in range(len(revenue)): # up to the length of the list 'revenue', which is 5 in this case.
    profit = revenue[i] - expenses[i] # This will calculate the profit for each month by subtracting the corresponding expense from the revenue.
    print("Profit:", profit)
    margin = profit * 100 / revenue[i] # This will calculate the margin for each month by dividing the profit by the revenue and multiplying by 100.    
    margins.append(margin)
    print(f"Margin:{i}:{margin:.2f}")
    print("Expenses:", expenses[i]) # This will output each element of the list 'expenses' using the index 'i'.
    print("Revenue:", revenue[i]) # This will output each element of the list 'revenue' using the index 'i'.
    print(margins) # This will output the list of margins calculated for each month.
    
    
    
    
    