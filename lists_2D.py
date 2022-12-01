l1 = [[5, 7, 8],
      [3, 5, 6],
      [4, 2, 1],
      [1,0]]
"""
print(l1)
l1_0 = l1[0]
print(l1_0)
print(l1_0[2])
print(l1[0][2])

output = []
Secound option found on internet i prefer mine tho ^^
    # go through each row in square
    for row in l1:

        # variable to store row total
        total = 0

        # go through each item in row and add to total
        for item in row:
            total += item

        # append the row's total to the output list
        output.append(total)

    # return the output list
    print(output)
    """
print('---------------------------')
print('Question 1:')
print('Sum of all rows:')
summ=[sum(i) for i in l1]
print(summ)
print('---------------------------')
print('Question 2:')
print('Sum of all columns:')
summ=[]
for i in range(len(l1)):
      for j in range(len(l1[i])):
            if(len(summ)<j+1):
                  summ.append(0)
            summ[j]+=l1[i][j]   
print(summ)
"""
secound possible solution if matrices is a square matrice
print('option 2 :')
col_totals = [ sum(x) for x in zip(*l1) ]
print (col_totals)
"""
print('---------------------------')
print('Question 3:')
summ=[sum(i) for i in l1]
soum=sum(summ)
print(f'Sum of all elements in l1: {soum}')
print('---------------------------')


#TODO sum all rows in l1 as a list of values
#TODO sum all columns in l1 as a list of values
#TODO sum all elements of l1
print('----------------')
lst1 = []
for row in l1:
      if (sum(row)):
            lst1.append(sum(row))
print('Sum of all rows in l1:',lst1)
list1 = l1[0]
list2 = l1[1]
list3 = l1[2]
zipped = zip(list1,list2,list3) #Iterating over the columns of the sublists.
print(type(zipped))
print(zipped) #Holding an iterator object
#print(list(zipped))
lst2 = []
for col in zipped:
      if (sum(col)):
            lst2.append(sum(col))
print('Sum of all columns in l1:',lst2)
#smart way(quicker):
rows_sum = [sum(row) for row in l1]
print('Sum of all rows in l1:', rows_sum)
columns_sum = [sum(col) for col in zip(*l1)]
print('Sum of all columns in l1:',columns_sum)
#Sum all elements of l1:
list4 = lst1
total = sum(list4)
print('Sum of all elements in l1:',total)