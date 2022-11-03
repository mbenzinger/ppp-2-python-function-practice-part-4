# step1
def max_num(num1, num2, num3):
    print(max([num1, num2, num3]))
max_num(5,6,7)

# step2
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
    return prod
print(mult_list([1,2,3,4]))

# step3
def rev_string(one_string):
    return one_string[::-1]
print(rev_string("JustOneString"))

# step4
def num_within(num1, range_start, range_end):
    return num1 in range(range_start, range_end+1)
print(num_within(4, 5, 5000))

# step5
#If I turned this in, it would only be due to copying the solution code, below.
#this is insane, and there's no way I could concieve this. I can't even read it.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)