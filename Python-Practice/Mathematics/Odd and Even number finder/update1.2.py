#program to find tne first ten odd and even integers.
from contextlib import nullcontext


print("Welcome to the odd and even number generator!!\n","What shall we do today?\n");

#FUNCTIONS DECLARED

#To check if the number the user inputed is truely higher or lower
def checker (low,high):
    if high >low:
        return True
    else:
        return False

#To generate odd numbers
def oddgen (low,high):
    for num in range(low,high):
        if (num%2)==0:
            print(num);

#To generate even numbers
def evengen(low,high):
    for num in range(low,high):
        if (num%2)== 0:
            print(num);

#THE MAIN CODE

while True:
    print("\tType: [o] to generate odd numbers\n\n\tOR Type: [e] to generate even numbers\n\n\tOR Type: [q] to quit\n");
    response =input("Your response: ");

    while response!="o" and response != "e" and response!="q":
        print("Not a valid response!!");
        response =input("Your response: ");
    if response == "q":
        print("Bye!");
        break
   
    if response=="e":
        low=int(input("\nEnter lowest number: "));
        high=int(input("\nEnter highest number: "));
        result=checker(low,high);
        while result == False:
            print("\nMisplacement of values! ");
            low=int(input("\nEnter lowest number: "));
            high=int(input("\nEnter highest number: "));
            result=checker(low,high);
        print("\nEven numbers between %i and %i are: \n"%(low,high));
        evengen(low,high)

    if response=="o":
        low=int(input("\nEnter lowest number: "));
        high=int(input("\nEnter highest number: "));
        result=checker(low,high);
        while result == False:
            print("\nMisplacement of values! ");
            low=int(input("\nEnter lowest number: "));
            high=int(input("\nEnter highest number: "));
            result=checker(low,high);
        print("\nOdd numbers between %i and %i are: \n"%(low,high));
        oddgen(low,high)

    print("\nDo you want to generate more numbers?");