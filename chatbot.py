from datetime import datetime

curr = datetime.now()
name=str(input("Enter Your Name :"))
c=curr.hour
#current_time = c.strftime('%H:%M:%S')

if(c<12):
    print(f"Good Morning {name} !")
elif(c >= 12 and c < 18):
    print(f"Good Afternoon {name} !")
else :
    print(f"Good Evening {name} !")

print("Welcome to help centre")





def myorder():
    print("1.Current Products \n2.Previous Order \n3.Canceled Order")
    type_order=int(input("Enter Type of Order :"))
    if (type_order == 1):
        print("Lenskart Glasses")
    elif (type_order == 2):
        print("Samsung Galaxy Z fold 2")
    elif (type_order == 3):
        print("Bewakoof White Shirt")

def myaccount():
    print("Alright! i had be happy to help.What's going on with your account? \n1.Change the number \n2.Change my email")
    type_order = int(input("Enter your request :"))
    if (type_order == 1):
        print("which phone number do you need to change? \n1.Contact number for an order \n2.Register number for my account \n3.Ask another question" )
        ph_num=int(input("Enter your request :"))
        if(ph_num==1):
            ph1=int(input("Enter your new 10 digit number :"))
            print("Successfully changed  to",ph1)
        elif(ph_num==2):
            print("1.Go to the Flipkart website or app.\n2.Enter your mobile number on the login page. \n3.Enter the one-time password (OTP) sent to your phone. \n4.Verify your phone number")
        else:
            print("Ask another Question")
    elif (type_order == 2):
        print("which email do you need to change? \n1.Contact email for an order \n2.Change email for my account \n3.Ask another question")
        ph_num = int(input("Enter your request :"))
        if (ph_num == 1):
            ph1 = str(input("Enter your Email :"))
            print("Successfully changed  to", ph1)
        elif (ph_num == 2):
            print("Go to the Account section.\n2.Select Edit Profil.\n3.Enter your new email address.\n4.Tap Verify")
        else:
            print("Ask another Question")

def returns():
    print("Alright!What kind of Issue Are You Having With Return? \n1.Payment and refunds \n2.Issue with order")
    ch = int(input("Enter your request :"))
    if (ch == 1):
        print("1.Where i can get my refunds.")
        a = int(input("Enter your request :"))
        if(a==1):
            print("1.Cash on delivery.\n2.Prepaid.")
            b = int(input("Enter your request :"))
            if(b==1):
                print("(Amount less than 1000rs.)Refund will processed to upi account for which upi id that has been shared")
            elif(b==2):
                print("(Amount less than 1000rs.)Refund will processed to Card that has been shared")

    elif (ch == 2):
       issue=str(input("Enter issue with your order :"))
       print("Your issue has been recorded")



def payment():
    print("1.Where did i get refund.\n2.Amount debited but order is not confirmed")
    ch=int(input("Enter your request :"))

def somethingelse():
    text=input("Enter to search:")
    responses= []
    responses.append(text)
    print("your response have been recorded , our team will contact shortly")


def main():
    while True:
        print("1.My Orders \n2.My Account \n3.Return \n4.Payments \n5.Something else \n6.exit ")
        ch=int(input("Enter the Choice :"))
        if(ch==1):
            myorder()
        elif(ch==2):
            myaccount()
        elif(ch==3):
            returns()
        elif(ch==4):
            payment()
        elif(ch==5):
            somethingelse()
        elif (ch == 6):
            print("thanks for using bye see you next time")
            break;
        else:
            print("enter valid input")

main()