import time
password=1234
Balance=20000
print("welcome to pentagon ATM")
print("insert your card ")
print("1.yes 2.no")
card=int(input())
if card==1:
    print("select your language")
    print("1.English 2.telugu 3.kannada")
    lang=int(input())
    if lang==1:
        print("enter your pin")
        pin=int(input())
        if pin==password:
            print("select the option")
            print("1.Balance 2.withdrawl")
            opt=int(input())
            if opt==1:
                print("your available balance is",Balance)
            elif opt==2:
                print("enter the amount")
                amt=int(input())
                if amt<=Balance:
                    print("transaction started")
                    print("transaction is processing")
                    time.sleep(4)
                    print("please collect your cash")
                    time.sleep(4)
                    print("do you want to check your balance")
                    print("1.yes 2.no")
                    choice=int(input())
                    if choice==1:
                        print("your balance is",Balance-amt)
                        print("thank visit again")
                    else:
                        print("thank you visit again")
                else:
                    print("invalid amount")
            else:
                print("select the option")
        else:
             print("wrong pin")
    else:
         print("please select only english")
else:
    print("please insert card properly")



