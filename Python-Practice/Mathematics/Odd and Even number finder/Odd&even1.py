#program to find the first ten odd and even integer
low = int(input("Enter lowest number:\n"));
high = int(input("enter highest number:\n"));
print('Odd numbers between %i and %i \n'%(low,high));
for num in range(low,high):
    if (num%2) != 0:
        print(num);
print('\n Even numbers between %i and %i \n'%(low,high));
for num in range(low,high):
    if (num%2) == 0:
        print(num);
        
