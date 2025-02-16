#Nested List & Misc

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#This will print row wise data. all the extra tikram used here is for printing each row in seperate line.
#For more read the Generator Function PDF
print(*(row for row in matrix), sep="\n")


print("\n\n")
'''
    Transpose of a Matrix
Next print is equlivalent to:


transposed = []  # This will store the final result
for i in range(4):  # i goes from 0 to 3
    new_row = []  # This will store one column of the new matrix
    for row in matrix:  # Go through each row in the original matrix
        new_row.append(row[i])  # Take the i-th element from the row
    transposed.append(new_row)  # Add this new "row" (column) to transposed


'''
print(*[[row[i] for row in matrix] for i in range(4)], sep="\n")  #See, here the loop values are seperated using [] and structure is like this bodypart --> inner loop --> outer loop

print("\n\n")
transposed = []  # This will store the final result
for i in range(4):  # i goes from 0 to 3
    new_row = []  # This will store one column of the new matrix
    for row in matrix:  # Go through each row in the original matrix
        new_row.append(row[i])  # Take the i-th element from the row
    transposed.append(new_row)  # Add this new "row" (column) to transposed
print(*transposed, sep='\n')