"""
Program to display the Airtel Menu

Functional ussd codes:
*131#  > balance check
*185# or *165# > mobile money
*175# > internet
"""

ussd = input("USSD: ")

def ussd_code():

    # checking ussd code input by the user
    code = ussd_code

    #Airtime Balance
    if ussd == "*131#":
        return "\n\nUSSD\nAcct Bal is Ush 4344. Stay Alert Do not share Your Mobile Money pin.\n"


    #Mobile Money
    elif ussd == "*165#" or ussd == "*185#":
        print("\nAIRTEL MONEY\n\n1.Send Money\n2.Airtime/Bundles\n3.Withdraw Cash\n4.Pay Bills\n5.My Account\n0.Back\n")
        
        # User inputs desired options
        opt = int(input())

        #send money option
        if(opt == 1):
           
            print("1.Airtel or Other line \n2.Mtn Number\n")
            opt2 = int(input())

            # Send to Airtel or other line
            if opt2 == 1:
                number = input("Enter  Number: ")
                if((number[2] == "5" or number[2] == "0") and len(number) == 10):
                    amount = input('Enter Amount: ')
                    
                    # verifying amount being sent is greater than min amount >> 5000 SHS
                    if int(amount) > 500:
                        return f"\nYou have sent {amount} SHS to {number}. You new balance is {int(amount)-5000} SHS\n"
                    else:
                        return f"\n{amount} SHS is below the minimum amount of 5000 SHS. Please recharge.\n"
                    
                else:
                    return "\n Sorry You entered an invalid number.\n"
                
            #Send to Mtn Number
            else:
                number = input("Enter Mtn Number: ")
                if(number[2] == "7" and len(number) == 10):
                    return "Enter Amount: "
                    
                else:
                    return "\n Sorry number entered is not a valid mtn number, Try again."

        
        # Airtime/Bundles option
        elif(opt == 2):
           
            print("\n1.Buy Airtime \n2.Data Bundles\n3.Voice Bundles\n4.OTT Service Tax\n0.Back\n")
            opt2 = int(input())

            # buying airtime 
            if opt2 == 1:
                print(f'\n1.Buy for Self\n2.Buy for another Number\n')
                
                number = input()
                
                # Buying airtime for self
                if number == "1":
                    amount = input('\nEnter Amount: ')
                    pin = input("Enter pin: ") 
                    return f"\nYou have recieved airtime of {amount} and your new balance is Ushs 70,000."

                #Buying airtime for another airtel number
                elif number == "2":
                    number = input("\nEnter  Airtel Number: ")
                    if((number[2] == "5" or number[2] == "0") and len(number)==10):
                        amount = input('Enter Amount: ')
                        pin = input("Enter pin: ") 
                        return f"\nYou have bought airtime of {amount} for {number} and your new balance is Ushs 70,000."
                    else:
                        return f"\nYou entered an invalid Airtel Number Please try again."
                        
                else:
                    return "Invalid Option."

            # buying data bundle
            elif opt2 == 2:
                print(f'\n1.Buy for Self\n2.Buy for another Number\n')
                
                number = input()
                
                # Buying data for self
                if number == "1":
                    print(f'AVAILABLE BUNDLES')
                    print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
                    opt = input()

                    # daily bundles 
                    if opt == "1":
                        print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 1000 shs  and your new balance is 0Ushs and 100mbs.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 500 shs  and your new balance is 0Ushs and 50mbs.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 250 shs  and your new balance is 0Ushs and 15mbs.\n" 
                        else:
                            return f"\n Invalid Option."

                    # weekly bundles
                    elif opt == "2":
                        print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 2000 shs  and your new balance is 0Ushs and 500mbs.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 6000 shs  and your new balance is 0Ushs and 1GB.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 15000 shs  and your new balance is 0Ushs and 4GB.\n" 
                        else:
                            return f"\n Invalid Option."

                    # Monthly  Bundles
                    elif opt == "3":
                        print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 30,000 shs  and your new balance is 0Ushs and 9GB.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 40,000 shs  and your new balance is 0Ushs and 15GB.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 50,000 shs  and your new balance is 0Ushs and 20GB.\n" 
                        else:
                            return f"\n Invalid Option."

                    # ott service
                    elif opt == "4":
                        return f"\nService is Currently unavailable."
                    
                    # invalid option
                    else:
                        return f"\nInvalid Option."

                # buying data for another number
                elif number == "2":
                    airtel_number = input("\nEnter airtel number: ")
                    print(f'\nAVAILABLE BUNDLES')
                    print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
                    opt = input()

                    # daily bundles 
                    if opt == "1":
                        print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 1000 shs for {airtel_number}\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 500 shs  for {airtel_number}\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 250 shs  for {airtel_number}\n" 
                        else:
                            return f"\n Invalid Option."

                    # weekly bundles
                    elif opt == "2":
                        print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 2000 shs  for {airtel_number}\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 6000 shs  for {airtel_number}\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 15000 shs  for {airtel_number}\n" 
                        else:
                            return f"\n Invalid Option."

                    # Monthly  Bundles
                    elif opt == "3":
                        print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 30,000 shs for {airtel_number}\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 40,000 shs  for {airtel_number}\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 50,000 shs  for {airtel_number}\n" 
                        else:
                            return f"\n Invalid Option."

                    # ott service
                    else:
                        return f"\nService is Currently unavailable."


        # withdraw cash
        elif(opt == 3):
            amount = input("\nEnter Amount to withdraw: ") 
            pin = input("Enter pin: ")
            if pin == "1234":
                return f"\nYou have withdrawn {amount} shs. New account balance is {amount} shs."
            else:
                return f"\nWrong Pin. You have 4 trials left for the account to be locked."


        #Pay bills
        elif(opt == 4):
            return f"\nSorry, Service is currently not available."


        # My account
        elif(opt == 5):
            print(f'\n1.Check Balance\n2.Change Pin\n3.Last 4 Transactions\n4.Mini Statement\n5.Pay OTT Tax')
            opt = input() 
            return f"\nSorry, Service is currently not available."


        # Back to previous menu
        elif(opt ==0):
            print("\nAIRTEL MONEY\n\n1.Send Money\n2.Airtime/Bundles\n3.Withdraw Cash\n4.Pay Bills\n5.My Account\n0.Back")
        
            # User inputs desired options
            opt = int(input())

            #send money option
            if(opt == 1):
                print("1.Airtel or Other line \n2.Mtn Number\n")
                opt2 = int(input())

                # Send to Airtel or other line
                if opt2 == 1:
                    number = input("Enter  Airtel Number: ")
                    if(number[2] != "7" or len(number) == 10):
                        print(f'number[2] = {number[2]}')
                        return "Enter Amount: "
                    
                    else:
                        print(f'number[2] = {number[2]}')
                        return "\n Sorry You entered an invalid number."
                
                #Send to Mtn Number
                else:
                    number = input("Enter Mtn Number: ")
                    if(number[2] == "7" and len(number) == 10):
                        return "Enter Amount: "
                    
                    else:
                        return "\n Sorry number entered is not a valid mtn number, Try again."

        
            # Airtime/Bundles option
            elif(opt == 2):
                print("\n1.Buy Airtime \n2.Data Bundles\n3.Voice Bundles\n4.OTT Service Tax\n0.Back\n")
                opt2 = int(input())

                # buying airtime 
                if opt2 == 1:
                    print(f'\n1.Buy for Self\n2.Buy for another Number\n')
                
                    number = input()
                
                    # Buying airtime for self
                    if number == "1":
                        amount = input('\nEnter Amount: ')
                        pin = input("Enter pin: ") 
                        return f"\nYou have recieved airtime of {amount} and your new balance is Ushs 70,000."

                    #Buying airtime for another airtel number
                    elif number == "2":
                        number = input("\nEnter  Airtel Number: ")
                        if((number[2] == "5" or number[2] == "0") and len(number)==10):
                            amount = input('Enter Amount: ')
                            pin = input("Enter pin: ") 
                            return f"\nYou have bought airtime of {amount} for {number} and your new balance is Ushs 70,000."
                        else:
                            return f"\nYou entered an invalid Airtel Number Please try again."
                        
                    else:
                        return "Invalid Option."

                # buying data bundle
                elif opt2 == 2:
                    print(f'\n1.Buy for Self\n2.Buy for another Number\n')                
                    number = input()
                
                    # Buying data for self
                    if number == "1":
                        print(f'AVAILABLE BUNDLES')
                        print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
                        opt = input()

                        # daily bundles 
                        if opt == "1":
                            print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 1000 shs  and your new balance is 0Ushs and 100mbs.\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 500 shs  and your new balance is 0Ushs and 50mbs.\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 250 shs  and your new balance is 0Ushs and 15mbs.\n" 
                            else:
                                return f"\n Invalid Option."

                        # weekly bundles
                        elif opt == "2":
                            print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 2000 shs  and your new balance is 0Ushs and 500mbs.\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 6000 shs  and your new balance is 0Ushs and 1GB.\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 15000 shs  and your new balance is 0Ushs and 4GB.\n" 
                            else:
                                return f"\n Invalid Option."

                        # Monthly  Bundles
                        elif opt == "3":
                            print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 30,000 shs  and your new balance is 0Ushs and 9GB.\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 40,000 shs  and your new balance is 0Ushs and 15GB.\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 50,000 shs  and your new balance is 0Ushs and 20GB.\n" 
                            else:
                                return f"\n Invalid Option."

                        # ott service
                        elif opt == "4":
                            return f"\nService is Currently unavailable."
                    
                        # invalid option
                        else:
                            return f"\nInvalid Option."

                    # buying data for another number
                    elif number == "2":
                        airtel_number = input("\nEnter airtel number: ")
                        print(f'\nAVAILABLE BUNDLES')
                        print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
                        opt = input()

                        # daily bundles 
                        if opt == "1":
                            print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 1000 shs for {airtel_number}\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 500 shs  for {airtel_number}\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 250 shs  for {airtel_number}\n" 
                            else:
                                return f"\n Invalid Option."

                        # weekly bundles
                        elif opt == "2":
                            print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 2000 shs  for {airtel_number}\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 6000 shs  for {airtel_number}\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 15000 shs  for {airtel_number}\n" 
                            else:
                                return f"\n Invalid Option."

                        # Monthly  Bundles
                        elif opt == "3":
                            print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                            opt = input()

                            # daily bundles activation
                            if opt == "1":
                                return f"\nYou have bought data of 30,000 shs for {airtel_number}\n" 
                            elif opt == "2":
                                return f"\nYou have bought data of 40,000 shs  for {airtel_number}\n" 
                            elif opt == "3":
                                return f"\nYou have bought data of 50,000 shs  for {airtel_number}\n" 
                            else:
                                return f"\n Invalid Option."

                        # ott service
                        else:
                            return f"\nService is Currently unavailable."


        # withdraw cash
        elif(opt == 3):
            amount = input("\nEnter Amount to withdraw: ") 
            pin = input("Enter pin: ")
            if pin == "1234":
                return f"\nYou have withdrawn {amount} shs. New account balance is {amount} shs."
            else:
                return f"\nWrong Pin. You have 4 trials left for the account to be locked."


        #Pay bills
        elif(opt == 4):
            return f"\nSorry, Service is currently not available."


        # My account
        elif(opt == 5):
            print(f'\n1.Check Balance\n2.Change Pin\n3.Last 4 Transactions\n4.Mini Statement\n5.Pay OTT Tax')
            opt = input() 
            return f"\nSorry, Service is currently not available."

            
        # any other input
        else:
            return f"\nInvalid Option, Try again!"
    
    
    # mobile internet
    elif ussd == "*175#":
        print("\n\nAIRTEL INTERNET\n")
        print(f'1.BUY BUNDLE\n2.BUY BUNDLE FOR ANOTHER\n3.CHECK BALANCE\n4.INTERNET SETTINGS\n5.MORE \n')

        opt = input() 
        # if user inputs 1
        if opt == "1":
                    print(f'AVAILABLE BUNDLES')
                    print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
                    opt = input()

                    # daily bundles 
                    if opt == "1":
                        print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 1000 shs  and your new balance is 0Ushs and 100mbs.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 500 shs  and your new balance is 0Ushs and 50mbs.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 250 shs  and your new balance is 0Ushs and 15mbs.\n" 
                        else:
                            return f"\n Invalid Option."

                    # weekly bundles
                    elif opt == "2":
                        print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 2000 shs  and your new balance is 0Ushs and 500mbs.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 6000 shs  and your new balance is 0Ushs and 1GB.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 15000 shs  and your new balance is 0Ushs and 4GB.\n" 
                        else:
                            return f"\n Invalid Option."

                    # Monthly  Bundles
                    elif opt == "3":
                        print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                        opt = input()

                        # daily bundles activation
                        if opt == "1":
                            return f"\nYou have bought data of 30,000 shs  and your new balance is 0Ushs and 9GB.\n" 
                        elif opt == "2":
                            return f"\nYou have bought data of 40,000 shs  and your new balance is 0Ushs and 15GB.\n" 
                        elif opt == "3":
                            return f"\nYou have bought data of 50,000 shs  and your new balance is 0Ushs and 20GB.\n" 
                        else:
                            return f"\n Invalid Option."

                    # ott service
                    else:
                        return f"\nService is Currently unavailable."

        elif opt == "2":

            airtel_number = input("\nEnter airtel number: ")
            print(f'\nAVAILABLE BUNDLES')
            print(f'\n1.DAILY BUNDLES\n2.WEEKLY BUNDLES\n3.MONTHLY BUNDLES\n4.PAY ONLY OTT PACK\n')
            opt = input()

            # daily bundles 
            if opt == "1":
                print(f'\n1.BUY 100 MBS @ 1K VALID FOR 24HRS\n2.BUY 50 MBS @ Ushs 500 VALID FOR 24HRS\n3.BUY 15 MBS @ 250 SHS VALID FOR 24HRS\n')
                opt = input()

                # daily bundles activation
                if opt == "1":
                    return f"\nYou have bought data of 1000 shs for {airtel_number}\n" 
                elif opt == "2":
                    return f"\nYou have bought data of 500 shs  for {airtel_number}\n" 
                elif opt == "3":
                    return f"\nYou have bought data of 250 shs  for {airtel_number}\n" 
                else:
                    return f"\n Invalid Option."

            # weekly bundles
            elif opt == "2":
                print(f'\n1.BUY 500 MBS @ 2K VALID FOR 7DAYS\n2.BUY 1GB MBS @ Ushs 6K VALID FOR 7DAYS\n3.BUY 4GB MBS @ 15K  VALID FOR DAYS\n')
                opt = input()

                # weekly bundles activation
                if opt == "1":
                    return f"\nYou have bought data of 2000 shs  for {airtel_number}\n" 
                elif opt == "2":
                    return f"\nYou have bought data of 6000 shs  for {airtel_number}\n" 
                elif opt == "3":
                    return f"\nYou have bought data of 15000 shs  for {airtel_number}\n" 
                else:
                    return f"\n Invalid Option."

            # Monthly  Bundles
            elif opt == "3":
                print(f'\n1.BUY 9GB @ 30K VALID FOR 1 MONTH\n2.BUY 15GB @ Ushs 40K VALID FOR 1 MONTH\n3.BUY 20GB  @ 50K  VALID FOR 1 MONTH\n')
                opt = input()

                # daily bundles activation
                if opt == "1":
                    return f"\nYou have bought data of 30,000 shs for {airtel_number}\n" 
                elif opt == "2":
                    return f"\nYou have bought data of 40,000 shs  for {airtel_number}\n" 
                elif opt == "3":
                    return f"\nYou have bought data of 50,000 shs  for {airtel_number}\n" 
                else:
                    return f"\n Invalid Option."

        elif opt =="3":
            return f"\nYou currently do not have an active bundle. Dial *175# to purchase \na bundle for as low as 300 shs. Thank You."
        
        # ott service
        else:
            return f"\n Sorry, Service is Currently unavailable."
                

    # if ussd code is not yet availbe
    else:
        return "\n\nInvalid USSD code! Try again\n\n"

            

# Calling the function
print(ussd_code())