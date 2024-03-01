# hi there lets write a code for first Banks USSD CODE 
#Line 1 to last line of the code was written by me Favour Peter
print("Good Afternoon🌞 , Welcome to first Bank 🏦 ...what would you like to do Today?  ")
print("1. Create New Account🏦 \n2. Transfer 📲 \n3. Airtime 📞\n4. Data 🌐 \n5. Balance 🏧 \n6. BIlls and Utilities 💵 \n7. Quit 🚪 \nPlease select one option above  ")
response = int(input("➡️   "))
# lets collect the users response
if response == 1:
     fn = str(input("To create a new account please enter the following informations \n First name?➡️    ")).upper()
     ln = str(input("Last Name ➡️   ")).upper()
     ot = str(input("Other names ➡️  ")).upper()
     str(input("Email Adresss ➡️   ")).upper()
     bvn = int(input("BVN ➡️  "))
     while len(str(bvn)) < 10:
           enter = input("⚠️ BVN shouldn't be less than or more than 10 Characters ,PLease enter a valid bvn ➡️   ")
           if len(enter) == 10:     
              print("Please wait ...")
              print("Verifying BVN ...")
              print("BVN  Verified")
              break
     while len(str(bvn)) > 10 :
          enter = input("BVN shouldn't be less than or more than 10 characters , PLease enter a valid bvn>   ")
          if len(enter) == 10:
                 print("⚠️ Please wait ...")
                 print("Verifying BVN ...")
                 print("BVN  Verified")
                 break
     else:
       len(str(bvn)) == 10
       print("Verifying BVN ...")
       print("Verifying BVN ...")
       print("BVN  Verified")
     phn = int(input("Phone Number ➡️  "))
     while len(str(phn)) <11 or len(str(phn))>11:
         retry = input(" ⚠️ INVALID ,Please re-enter a valid Phone number ➡️  ")
         if len(str(retry)) == 11:
             break
     print(f"{fn} ⚠️ Please hold ....\nGenerating Account Number \nAccount creation successfull")
     import random
     account_number = str(random.randint(11,99)) + str(random.randint(11,99)) +str(random.randint(11,99)) + str(random.randint(11,99)) + str(random.randint(11,99))
     print(f"{fn} {ln} {ot} Your New FIRST BANK🏦  Account has been created and your new Account number is {account_number} Welcome to FIRST BANK 👏🤝 ")
elif response == 2:
  print("TRANSFER! 📲 \nCurrent Ballance is : 360,000 Naira 💵 ")
  bana = input("Enter Bank Name ➡️  ")
  bena = str(input("Enter Beneficiary's Name ➡️  ")).upper()
  dest = int(input("Enter Destination account number ➡️  "))
  while len(str(dest)) <10 or len(str(dest))>10:
      retry = input("Unable To Find an account ,Please Enter A Valid Account Number ➡️   ")
      if len(str(retry)) == 10:
          print("Account Found!")
          break
  else:
      print("Account Found! ")   
  cb = 360000
  amt = int(input("Enter Amount ➡️ "))
  ballance = cb - amt
  if amt <= 360000:
    print(f"Would you like to send the sum of {amt} NAIRA to {bena} {dest} {bana} \n1. Yes \n2. No ")
    rezp= int(input("➡️ " ))
    if rezp == 1:
        print(f"Proccessing transfer to {bena}  ")
        print(f"Transfer Successfull your new ballance is {ballance} NAIRA")
    elif rezp == 2:
        print("Transfer Canceled ")
    else:
        print("Invalid Command Please Restart ")
  else:
      amt > 360000
      print("Insufficient Ballance ")
elif response == 3:
    print("FIRST BANK AIRTIME NG 📞 ")
    aamt = int(input("Choose an amount: \n1. N100\n2. N200\n3. N500\n4. N1000  \n ➡️ "))
    if aamt == 1:
        net = int(input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE \n ➡️   "))
        if net == 1:
            mtn = "MTN"
            apn = input("Enter MTN Phone number ➡️   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid MTN Number ➡️ ")
                if len(retry) == 11:
                    print(f"100 Naira {mtn} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"100 Naira {mtn} Airtime Top up Successfull for {apn}")
        elif net == 2:
            atl = "AIRTEL"
            apn = input(f"Enter {atl} Phone number ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"100 Naira {atl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"100 Naira {atl} Airtime Top up Successfull for {apn}")
        elif net == 3:
            gl = "GLO"
            apn = input(f"Enter {gl} Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"100 Naira {gl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"100 Naira {gl} Airtime Top up Successfull for {apn}")
        elif net == 4:
            m9 = "9MOBILE"
            apn = input(f"Enter {m9} Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"100 Naira {m9} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"100 Naira {m9} Airtime Top up Successfull for {apn}")
        else:
            print("Please enter a Valid Command and Try Again")
    elif aamt == 2:
        net = int(input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE \n>  "))
        if net == 1:
            mtn = "MTN"
            apn = input("Enter MTN Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid  Number ")
                if len(retry) == 11:
                    print(f"200 Naira {mtn} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"200 Naira {mtn} Airtime Top up Successfull for {apn}")
        elif net == 2:
            atl = "AIRTEL"
            apn = input(f"Enter {atl} Phone number ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"200 Naira {atl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"200 Naira {atl} Airtime Top up Successfull for {apn}")
        elif net == 3:
            gl = "GLO"
            apn = input(f"Enter {gl} Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"200 Naira {gl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"200 Naira {gl} Airtime Top up Successfull for {apn}")
        elif net == 4:
            m9 = "9MOBILE"
            apn = input(f"Enter {m9} Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"200 Naira {m9} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"200 Naira {m9} Airtime Top up Successfull for {apn}")
        else:
            print("Please enter a Valid Command and Try Again")
    elif aamt == 3:
        net = int(input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE \n>   "))
        if net == 1:
            mtn = "MTN"
            apn = input("Enter MTN Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"500 Naira {mtn} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"500 Naira {mtn} Airtime Top up Successfull for {apn}")
        elif net == 2:
            atl = "AIRTEL"
            apn = input(f"Enter {atl} Phone number ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"500 Naira {atl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"500 Naira {atl} Airtime Top up Successfull for {apn}")
        elif net == 3:
            gl = "GLO"
            apn = input(f"Enter {gl} Phone number >   ")
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"500 Naira {gl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"500 Naira {gl} Airtime Top up Successfull for {apn}")
        elif net == 4:
            m9 = "9MOBILE"
            apn = (input("Enter 9MOBILE Phone number >   "))
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"500 Naira {m9} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"500 Naira {m9} Airtime Top up Successfull for {apn}")
        else:
            print("Please enter a Valid Command and Try Again")
    elif aamt == 4:
        net = int(input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE \n>   "))
        if net == 1:
            mtn = "MTN"
            apn = (input("Enter MTN Phone number >   "))
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"1000 Naira {mtn} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"1000 Naira {mtn} Airtime Top up Successfull for {apn}")
        elif net == 2:
            atl = "AIRTEL"
            apn = (input(f"Enter {atl} Phone number "))
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"1000 Naira {atl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"1000 Naira {atl} Airtime Top up Successfull for {apn}")
        elif net == 3:
            gl = "GLO"
            apn = (input(f"Enter {gl} Phone number >   "))
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"1000 Naira {gl} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"1000 Naira {gl} Airtime Top up Successfull for {apn}")
        elif net == 4:
            m9 = "9MOBILE"
            apn = (input(f"Enter {m9} Phone number >   "))
            while len(apn) <11 or len(apn) >11:
                retry = input("Please Enter a Valid Number ")
                if len(retry) == 11:
                    print(f"1000 Naira {m9} Airtime Top up Successfull for {retry}")
                    break
            else:
                print(f"1000 Naira {m9} Airtime Top up Successfull for {apn}")
        else:
            print("Please enter a Valid Command and Try Again")
    else:
        print("Please enter a Valid Command and Try Again")
elif response == 4:
    print("DATA PURCHASE ")
    print("INTERNET SERVICE PROVIDERS:\n1. MTN-NG DATA \n2. AIRTEL-NG DATA \n3. GLO-NG DATA\n4. 9MOBILE-NG DATA \n5. SPECTRANET-NG \n6. SMILE NG ")
    service_c = int(input("Choose A Provider \n>   "))
    if service_c == 1:
        print("MTN NG DATA PLANS \n1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = int(input("Choose A Package  \n>  "))
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid MTN Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n100MB \nMTN \nTo {retry}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"100MB Data Plan Successfull for {retry} Valid For 1 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n100MB \nMTN \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s) ")
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid MTN Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n2.5GB \nMTN \nTo {retry}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"2.5GB Data Plan Successfull for {retry} Valid For 2 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n100MB \nMTN \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"2.5GB Data Plan Successfull for {rphn} Valid For 2 Day(s) ")
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid MTN Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n11GB \nMTN \nTo {retry}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"11GB Data Plan Successfull for {retry} Valid For 30 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n11GB \nMTN \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"11GB Data Plan Successfull for {rphn} Valid For 30 Day(s) ")
        else:
            print("Please enter a valid Command")

    elif service_c == 2:
        print("AIRTEL DATA DATA PLANS \n1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = int(input("Choose A Package  \n>  "))
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n100MB \nAIRTEL \nTo {retry}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"100MB Data Plan Successfull for {retry} Valid For 1 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n100MB \nAIRTEL \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s) ")
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n2.5GB \nAIRTEL \nTo {retry}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"2.5GB Data Plan Successfull for {retry} Valid For 2 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n2.5GB \nAIRTEL \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"2.5GB Data Plan Successfull for {rphn} Valid For 2 Day(s) ")
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n11GB \nAIRTEL  \nTo {retry}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"11GB Data Plan Successfull for {retry} Valid For 30 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n11GB \nAIRTEL  \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"11GB Data Plan Successfull for {rphn} Valid For 30 Day(s) ")
        else:
            print("Invalid command")
    elif service_c == 3:
        print("GLO NG DATA PLANS \n1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = int(input("Choose A Package  \n>  "))
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n100MB \nGLO \nTo {retry}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"100MB Data Plan Successfull for {retry} Valid For 1 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n100MB \nGLO \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s) ")
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n2.5GB \nGLO \nTo {retry}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"2.5GB Data Plan Successfull for {retry} Valid For 2 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n2.5GB \nGLO  \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"2.5GB Data Plan Successfull for {rphn} Valid For 2 Day(s) ")
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n11GB \nGLO \nTo {retry}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"11GB Data Plan Successfull for {retry} Valid For 30 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n11GB \nMTN \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"11GB Data Plan Successfull for {rphn} Valid For 30 Day(s) ")
        else:
            print("Invalid Command ")
    elif service_c == 4:
        print("9MOBILE NG DATA PLANS \n1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = int(input("Choose A Package  \n>  "))
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n100MB \n9MOBILE \nTo {retry}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"100MB Data Plan Successfull for {retry} Valid For 1 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n100MB \n9MOBILE \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s) ")
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n2.5GB \n9MOBILE \nTo {retry}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"2.5GB Data Plan Successfull for {retry} Valid For 2 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n2.5gB \n9MOBILE \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"2.5GB Data Plan Successfull for {rphn} Valid For 2 Day(s) ")
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = (input("Enter Recipient Phone number\n>>  "))
            while len(rphn) <11 or len(rphn) >11:
                retry = input("Please Enter a Valid Number  ")
                if len(retry) == 11:
                    confm = int(input(f"Confirm \n11GB \n9MOBILE \nTo {retry}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                    while confm != 1:
                        print("Data purchase canceled")
                        break
                    else:
                        confm == 1
                        print(f"11GB Data Plan Successfull for {retry} Valid For 30 Day(s) ")
                        break
            else:
                confm = int(input(f"Confirm \n11GB \n9MOBILE \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No \n>>  "))
                while confm != 1:
                     print("Data purchase canceled")
                     break
                else:
                    confm == 1
                    print(f"11GB Data Plan Successfull for {rphn} Valid For 30 Day(s) ")
        else:
            print("Invalid Command ")
    elif service_c == 5:
        print("...Sorry The Spectranet Service Is Temporarily Unavailable ")
    elif service_c == 6:
        print("...Sorry The Smile Service is Currently Unavailable")
    else:
        print("Please Enter a Correct Option ")
elif response == 5:
    print("PLease log in your credentials ")
    fn = str(input("Enter your Full Name to Log In ")).upper()
    print(f"Welcome Back {fn}")
    print(f"Checking Account Ballance for {fn}...")
    print(f"Checking Account Ballance for {fn}...Please wait this may take a while... ")
    print(f"Checking Account Ballance for {fn}...")
    print(f"Checking Account Ballance for {fn}...Please wait this may take a while... ")
    print(f"Checking Account Ballance for {fn}...Please wait this may take a while... ")
    print(f"Your current Account Ballance is 360,000 NGN")
    print(f"Have a Wonderfull Day {fn} ")
elif response == 6 :
    print("BILLS AND UTILITIES🪙💳 ")
    print("ESSENTIALS :\n1.    TV📺 \n2.    ELECTRICITY💡 \n3.    EDUCATION📖\n4.    BETTING⚽ ")
    essentials = int(input("Choose A Service \n>   "))
    if essentials == 1:
        print("TV📺 Subscriptions")
        print("Service Providers ")
        pc = int(input("1.    SHOW MAX📺 \n2.    DSTV📺 \n3.    GOTV📺\n    Choose Your Provider ➡️  "))
        if pc == 1:
            sm = input("Available Packages \n SHOWMAX PRO MOBILE📺 4,000 Naira \n Enter ShowMax ID ➡️  ").lower()
            print(f"Processing ShowMax Pro Mobile for {sm}...")
            confam = int(input(f"Confirm Purchase of ShowMax Bundle for {sm}  \n1. YES💳 \n2. NO❌ "))
            while confam == 1:
                print(f"Show Max Pro Mobile Succesfull for {sm} 📺 ")
                break
            else:
                print("Have a Nice Day ")
        elif pc == 2:
            em = input("Available Packages \n DSTV PREMIUM📺 25,000 Naira \n Enter Enter Online DSTV ID ID ➡️  ").lower()
            print(f"Processing DSTV PREMIUM for {em}...")
            confam = int(input(f"Confirm Purchase of ShowMax Bundle for {em}  \n1. YES💳 \n2. NO❌ "))
            while confam == 1:
                print(f"DSTV PREMIUM Succesfull for {em} 📺 ")
                break
            else:
                print("Have a Nice Day ")
        elif pc == 3:
            em = input("Available Packages \n GoTV SUPA📺 7,600 Naira \n Enter Enter Online GoTV ID ID ➡️  ").lower()
            print(f"Processing DSTV PREMIUM for {em}...")
            confam = int(input(f"Confirm Purchase of GoTV Bundle for {em}  \n1. YES💳 \n2. NO❌ "))
            while confam == 1:
                print(f"GoTV SUPA Succesfull for {em} 📺 ")
                break
            else:
                print("Have a Nice Day ")
        else:
            print("Invalid command Entered ")
    elif essentials == 2:
        print("Electricity Prepaid Subscriptions")
        print("Service Providers ")
        pc = int(input("1.    EEDC NG  \n2.   EKEDC NG    \n    Choose Your Provider ➡️  "))
        if pc == 1:
            sm = input("Available Package \n EEDC PREPAID  4,000 Naira \n Enter METER NUMBER  ➡️  ").lower()
            print(f"Processing EEDC PREPAID for {sm}...")
            confam = int(input(f"Confirm Purchase of EEDC for {sm}  \n1. YES💳 \n2. NO❌ "))
            while confam == 1:
                print(f"EEDC PREPAID Succesfull for {sm} 📺 ")
                break
            else:
                print("Have a Nice Day ")
        elif pc == 2:
            sm = input("Available Packages \n EKEDC 5,000 Naira \n Enter METER NUMBER  ➡️  ").lower()
            print(f"Processing EKDEDDC for {sm}...")
            confam = int(input(f"Confirm EKEDC for {sm}  \n1. YES💳 \n2. NO❌ "))
            while confam == 1:
                print(f"EKEDC PREPAID Succesfull for {sm} 📺 ")
                break
            else:
                print("Have a Nice Day ")
        else:
            print("Please choose a valid option")
    elif essentials == 3:
        print("JAMB NG E-PIN ")
        pc = int(input("1.    UTME EPIN 6,200 Naira  \n2.   UTME EPIN (With Mock) 7,700 Naira    \n    Choose  ➡️  "))
        if pc == 1:
            print("UTME EPIN 6,200 Naira")
            phn = input("  Enter Phone Number  ➡️  ")
            prfc = input(f"Enter Your profile code associated with {phn}   ")
            vrfy = input("Please verify the informations you've entered \n Proceed ?! \n 1. YES \n2. NO   ")
            while int(vrfy) == 1:
                import random
                code = str(random.randint(11,99)) + str(random.randint(11,99)) +str(random.randint(11,99)) 
                print(f"{phn} Your ePIN Purchase was succesfull, here's your pin '{code}' for your Profile code '{prfc}'")
                break
            else:
                print("ePIn Purchase canceled , Have a Nice Day ")
        elif pc == 2:
            print("UTME EPIN(Mock Included) 7,700 Naira")
            phn = input("  Enter Phone Number  ➡️  ")
            prfc = input(f"Enter Your profile code associated with {phn}   ")
            vrfy = input("Please verify the informations you've entered \n Proceed ?! \n 1. YES \n2. NO   ")
            while int(vrfy) == 1:
                import random
                code = str(random.randint(11,99)) + str(random.randint(11,99)) +str(random.randint(11,99)) 
                print(f"{phn} Your ePIN Purchase was succesfull, here's your pin ({code}) for your Profile code ({prfc})")
                break
            else:
                print("ePIn Purchase canceled , Have a Nice Day ")
        else:
            print("Please choose a valid option")
    elif essentials == 4:
        print("Sorry! Betting Services are currently Unavailable on our Platform ")
        print("Have a Nice Day")
    else :
        print("Please Select A Valid Option and Try again")
else:
    print("Closing FIRST BANK USSD code ...")
while response == 7:
    print("Closing FIRST BANK USSD CODE ")
    break