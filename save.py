# hi there lets write a code for first Banks USSD CODE 
print("Good Afternoon , Welcome to first Bank ...what would you like to do Today?  ")
print("1. Create New Account \n2. Transfer \n3. Airtime \n4. Data \n5. Balance \n6. BIlls and Utilities \nPlease select one option above  ")
response = int(input(">>   "))
# lets collect the users response
if response == 1:
     fn = str(input("To create a new account please enter the following informations \n First name?>>    ")).upper()
     ln = str(input("Last Name ?>>   ")).upper()
     ot = str(input("Other names?>>  ")).upper()
     str(input("Email Adresss>>")).upper()
     bvn = int(input("BVN>>  "))
     while len(str(bvn)) < 10:
           enter = input("BVN shouldn't be less than or more than 10 Characters ,PLease enter a valid bvn>   ")
           if len(enter) == 10:     
              print("Please wait ...")
              print("Verifying BVN ...")
              print("BVN  Verified")
              break
     while len(str(bvn)) > 10 :
          enter = input("BVN shouldn't be less than or more than 10 characters , PLease enter a valid bvn>   ")
          if len(enter) == 10:
                 print("Please wait ...")
                 print("Verifying BVN ...")
                 print("BVN  Verified")
                 break
     else:
       len(str(bvn)) == 10
       print("Verifying BVN ...")
       print("Verifying BVN ...")
       print("BVN  Verified")
     phn = int(input("Phone Number>  "))
     while len(str(phn)) <11 or len(str(phn))>11:
         retry = input("INVALID ,Please re-enter a valid Phone number >>  ")
         if len(str(retry)) == 11:
             break
     print(f"{fn} Please hold ....\nGenerating Account Number \nAccount creation successfull")
     import random
     account_number = str(random.randint(11,99)) + str(random.randint(11,99)) +str(random.randint(11,99)) + str(random.randint(11,99)) + str(random.randint(11,99))
     print(f"{fn} {ln} {ot} Your New FIRST BANK Account has been created and your new Account number is {account_number} Welcome to FIRST BANK  ")
elif response == 2:
  print("Transfer!, Current Ballance is : 360,000 Naira ")
  bn = input("Enter Bank Name ")
  dest = int(input("Enter Destination account number>>  "))
  bene = str(input("Enter Beneficiary's Name>>  ")).lower()
  cb = 360000
  amt = int(input("Enter Amount "))
  ballance = cb - amt
  if amt <= 360000:
    input(f"Would you like to send the sum of {amt} to {bene} {dest} {bn} \n1. Yes \n2. No ")
    rezp= int(input("> " ))
    if rezp == 1:
        print(f"Proccessing transfer to {bene}  ")
        print(f"Transfer Successfull your new ballance is {ballance}")
    elif rezp == 2:
        print("Transfer Canceled ")
    else:
        print("Invalid Command Please Restart ")
  else:
      amt > 360000
      print("Insufficient Ballance ")
elif response == 3:
    print("FIRST BANK AIRTIME NG ")
    aamt = input("Choose an amount: \n1. N100\n2. N200\n3. N500\n4. N1000")
    if aamt == 1:
        net = input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE ")
        if net == 1:
            mtn = "MTN"
            apn = int(input("Enter {mtn} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"100 Naira {mtn} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid MTN Phone number>  ")
        elif net == 2:
            atl = "AIRTEL"
            apn = int(input(f"Enter {atl} Phone number "))
            while len(str(apn)) == 11:
                print(f"100 Naira {atl} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid Airtel")
        elif net == 3:
            gl = "GLO"
            apn = int(input("Enter {gl} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"100 Naira{gl} Airtime Top up Successfull for {apn}")
                break
        elif net == 4:
            m9 = "9MOBILE"
            apn = int(input("Enter {m9} Phone number >   "))
            while len(str(apn)) == 11:
                print(f" {m9} Airtime Top up Successfull for {apn}")
                break
    elif aamt == 2:
        net = input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE ")
        if net == 1:
            mtn = "MTN"
            apn = int(input("Enter {mtn} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"200 Naira {mtn} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid MTN Phone number>  ")
        elif net == 2:
            atl = "AIRTEL"
            apn = int(input(f"Enter {atl} Phone number "))
            while len(str(apn)) == 11:
                print(f"200 Naira {atl} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid Airtel")
        elif net == 3:
            gl = "GLO"
            apn = int(input("Enter {gl} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"200 Naira {gl} Airtime Top up Successfull for {apn}")
                break
        elif net == 4:
            m9 = "9MOBILE"
            apn = int(input("Enter {m9} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"200 Naira  {m9} Airtime Top up Successfull for {apn}")
                break
    elif aamt == 3:
        net = input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE ")
        if net == 1:
            mtn = "MTN"
            apn = int(input("Enter {mtn} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"500 Naira {mtn} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid MTN Phone number>  ")
        elif net == 2:
            atl = "AIRTEL"
            apn = int(input(f"Enter {atl} Phone number "))
            while len(str(apn)) == 11:
                print(f"500 Naira {atl} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid Airtel")
        elif net == 3:
            gl = "GLO"
            apn = int(input("Enter {gl} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"500 Naira {gl} Airtime Top up Successfull for {apn}")
                break
        elif net == 4:
            m9 = "9MOBILE"
            apn = int(input("Enter {m9} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"500 Naira {m9} Airtime Top up Successfull for {apn}")
                break
    elif aamt == 4:
        net = input("Select Network\n1. MTN\n2. AIRTEL\n3. GLO\n4. 9MOBILE ")
        if net == 1:
            mtn = "MTN"
            apn = int(input("Enter {mtn} Phone number >   "))
            while len(str(apn)) == 11:
                print(f"1000 Naira {mtn} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid MTN Phone number>  ")
        elif net == 2:
            atl = "AIRTEL"
            apn = int(input(f"Enter {atl} Phone number "))
            while len(str(apn)) == 11:
                print(f"1000 Naira {atl} Airtime Top up Successfull for {apn}")
                break
            else:
                print("Please enter a valid Airtel")
        elif net == 3:
            gl = "GLO"
            apn = int(input("Enter {gl} Phone number >   "))
            while len(str(apn)) == 11:
                print(f" 1000 Naira {gl} Airtime Top up Successfull for {apn}")
                break
        elif net == 4:
            m9 = "9MOBILE"
            apn = int(input("Enter {m9} Phone number >   "))
            while len(str(apn)) == 11:
                print(f" 1000 Naira {m9} Airtime Top up Successfull for {apn}")
                break
elif response == 4:
    print("DATA PURCHASE ")
    print("INTERNET SERVICE PROVIDERS:\n1. MTN-NG DATA \n2. AIRTEL-NG DATA \n3. GLO-NG DATA\n4. 9MOBILE-NG DATA \n5. SPECTRANET-NG \n6. SMILE NG ")
    service_c = int(input("Choose A Provider "))
    if service_c == 1:
        print("1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = input("Choose A Package ")
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n100MB \nMTN \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s)")
                break
            while confm == 2:
                print("Data purchase canceled")
                break
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n2.5GB \nMTN \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"2.5GB Data Plan Successfull for {rphn} Valid for 2 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n11GB \nMTN \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"11GB Data Plan Successfull for {rphn} Valid for 30 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
    elif service_c == 2:
        print("1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = input("Choose A Package ")
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n100MB \nAIRTEL \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s)")
                break
            while confm == 2:
                print("Data purchase canceled")
                break
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n2.5GB \nAIRTEL \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"2.5GB Data Plan Successfull for {rphn} Valid for 2 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n11GB \nAIRTEL \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"11GB Data Plan Successfull for {rphn} Valid for 30 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
    elif service_c == 3:
        print("1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = input("Choose A Package ")
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n100MB \nGLO \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s)")
                break
            while confm == 2:
                print("Data purchase canceled")
                break
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n2.5GB \nGLO \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"2.5GB Data Plan Successfull for {rphn} Valid for 2 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n11GB \nGLO \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"11GB Data Plan Successfull for {rphn} Valid for 30 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
    elif service_c == 4:
        print("1. 100MB For 1 Day \n2. 2.5GB For 2Days \n3. 11GB For 1month")
        data_c = input("Choose A Package ")
        if data_c == 1:
            print("Purchase A 100MB Daily Plan For 100 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n100MB \n9MOBILE \nTo {rphn}\nAmount 100 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"100MB Data Plan Successfull for {rphn} Valid For 1 Day(s)")
                break       
            while confm == 2:
                print("Data purchase canceled")
                break
        elif data_c == 2:
            print("Purchase A 2.5GB 2 Days Plan For 600 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n2.5GB \n9MOBILE \nTo {rphn}\nAmount 600 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"2.5GB Data Plan Successfull for {rphn} Valid for 2 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
        elif data_c == 3:
            print("Purchase A 11GB 30 Days Plan For 3,500 Naira: ")
            rphn = int(input("Enter Recipient Phone number>>  "))
            confm = input(f"Confirm \n11GB \n9MOBILE \nTo {rphn}\nAmount 3,500 Naira\n1. Yes \n2. No >> ")
            while confm == 1:
                print(f"11GB Data Plan Successfull for {rphn} Valid for 30 Days ")
                break
            while confm == 2:
                print("Data Purchase canceled ")
                break
    elif service_c == 5:
        print("...Sorry The Spectranet Service Is Temporarily Unavailable ")
    elif service_c == 6:
        print("...Sorry The Smile Service is Currently Unavailable")
    else:
        print("Please Enter a Correct Option ")
