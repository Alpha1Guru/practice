from logging.handlers import WatchedFileHandler


print("key [x] to stop");

num = input("num: ");
ansnum=0;
while num != "x":
    num= int(num);
    ansnum+= num;
    num = input("num: ");
print("The sum of numbers is: %i"%(ansnum));