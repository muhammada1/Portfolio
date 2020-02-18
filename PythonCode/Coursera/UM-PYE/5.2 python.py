5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

nlist = []
while True:
  num1 = input('number:')
    
  if num1 == 'done':
    break
  else:
    try:
      num = int(num1)
      nlist.append(num)
    except:
      print('Invalid input')
      continue
    
largest = max(nlist)
smallest = min(nlist)

print('Maximum is', largest)
print('Minimum is', smallest)
