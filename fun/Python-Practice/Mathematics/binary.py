

def binary():
    print("Welcome to base ten to binary converter");
    print("Type y to convert a base ten number and q to quit");
    while True:
        res=input("Your response: ");
        if res=='q':
            print('\nBye');
            break
        while (res != "y" and res != 'p'):
            print("Wrong input TRY AGAIN");
            res=input("Your response: ");
        if res =="y":
            ans=[];
            base_ten=int(input("Enter base_ten number: "));
            while base_ten < 1:
                print("Input an integer that is greater than zero!")
                base_ten = int(input("Enter base-ten number: "));
            while base_ten != 0:
                rem= base_ten % 2;
                ans.append(rem);
                base_ten = base_ten//2;
            count= len(ans);
            print("Your answer: ")
            while count!=0:
                count-=1;
                print("\t",ans[count]);
        print("Want to convert more numbers?");


binary()
