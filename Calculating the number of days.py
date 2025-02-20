from datetime import datetime
DAY = True
while True:
    try : 
            dob_str = input("Enter your birthdate (d,m,y) or 0 to close  -> ")     
            dob = datetime.strptime(dob_str, "%d/%m/%Y") 
            today = datetime.today()  
            difference = today - dob 
            days_lived = difference.days 
            days_lived = difference.days 
            print("Yoou have lived -> " , days_lived , "days")
    
    except :
        print("error")
        DAY = False
        break