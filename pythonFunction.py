# Write a Python function called max_num()to find the maximum of three numbers
def max_num(a,b,c):
    max = [a,b,c]
    return max
print(max_num(23,24,3))
print(max_num(1,4,6))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    mult = 1
    for num in numbers:
        mult *= num
    return mult
list_num = [2,10,5,20]
mult = mult_list(list_num)
print(mult)
print(mult_list([1,5,10]))
print(mult_list([]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(rev_string):
    return rev_string[::-1]

print(rev_string('hello'))
print(rev_string('?desrever siht si'))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(beg, mid, end):
    return beg in range(mid, end+1)
    
print(num_within(2,1,5))
print(num_within(10,2,12))
print(num_within(20,22,23))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    if n <= 0:
        return
    triangle = [[1]]
    for i in range(1,n):
        row = triangle[-1]
        new_row =[1]
        for it in range (1,len(row)):
            new = row[it - 1]+ row[it]
            new_row.append(new)
        new_row.append(1)
        triangle.append(new_row)
    for rows in triangle:
        print(''.join(map(str, rows)).center(n *3))
pascal(5)
pascal(10)
    
