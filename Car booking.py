#import cx_Oracle
#con = cx_Oracle.connect("/")
def book() :
    cur = con.cursor()
    cur.execute("select * from vehicledetails")
    vi=str(input("Enter vehicle_id to BOOK: "))
    tin=time()
    custid=generateOTP()
    print("CUSTOMER ID is ",custid)
    cur.execute("insert into userdetails values('"+uname+"','"+password+"','"+mobile+"','"+custid+"','"+tin+"','"+vi+"')")
    cur.execute("delete from vehicledetails where vehicleid=vi")
    k=str(input("1.Cab/2.Self driving"))
    if k==1:
        print("Rent is 12/km")
    else:
        m=str(input("How many days to travel"))
        print("Rent is ",m*1800)
    con.commit()
    print("HAPPY JOURNEY")
    return
def passwordcheck(c,i) :
    if c == i:
        return
    else :
        print("Invalid")
        main()
    
def time() :
    from time import gmtime, strftime
    picktime = strftime("%H:%M", gmtime())
    return showtime
def generateOTP() : 
	import math, random
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)] 
	return OTP
def userlogin() :
    uname = input("Enter the username : ")
    password = input("Enter the password : ")
    cur = con.cursor()
    cur.execute("select * from userdetails where username = '"+uname+"' AND password='"+password+"'")
    con.commit()
    if cur.fetchone():
        while TRUE:
            book()
    else:
        print("Invalid credentials...!")
    return
def register():
                uname = input("Enter the username : ")
                c=generateOTP()
                print("OTP is ",c)
                i=str(input("Enter OTP: "))
                passwordcheck(c,i)
                passwd = input("Enter the password : ")
                cpwd=input("Confirm Password:")
                mobile = input("Enter the mobile number : ")
                hname = input("Enter the House name/Flat no: ")
                city= input("Enter the City: ")
                state= input("Enter the  state : ")
                email = input("Enter the email id : ")
                cur = con.cursor()
                cur.execute("insert into login values('" + uname + "','" + passwd + "','" +cpwd+"','" + mobile + "','" + hname + "','" + city + "','" + state+ "','" + email+ "')") 
                con.commit()
                admin()
                return
def admin():
      uname = input("Enter the username : ")
      passwd = input("Enter the password : ")
      cur = con.cursor()
      cur.execute("select * from  login where username = '" + uname + "' AND password = '" + passwd+ "'")
      if cur.fetchone():
              while True:
                  print("1.Customer details")
                  print("2.Add Vehicle")
                  print("3.Remove Vehicle")
                  print("4.Vehicle details")
                  print("5.Booking Details")
                  print("6.Change profile")
                  ch = int(input("Enter your choice : "))
                  if ch == 1:#view customer details
                        custid=str(input("Enter customer id :"))
                        cur.execute("select * from userdetails where customerid = '" + custid + "' order by  customerid'")
                        con.commit()
                  elif ch==2:#add vehicle
                        vn=input("Add vehicle Model name :")
                        vi=int(input("Enter the vehicle id:"))
                        vt=input("Enter the vehicle type:")
                        vc=input("Enter the vehicle colour:")
                        vcon=input("Enter the vehicle condition:")
                        curc.execute("insert into vehicledetails values(vn,vi,vt,vc,vcon)")
                        con.commit()
                  elif ch==3:#Remove vehicle
                        vi=int(input("Enter the vehicle id:"))
                        curr.execute("delete from vehicledetails where vehicleid=vi")
                        con.commit()
                  elif ch==4: #vehicle details
                        cur.execute("select *from vehicledetails")
                        con.commit()
                  elif ch==5: #Booking details
                        cur.execute("select *from userdetails")
                        con.commit()
                  elif ch==6:#change profile
                        s=int(input("1.Change mobile number\n 2.Change address\n 3.Change email id"))
                        if s==1:
                            mob = input("Enter the mobile number : ")
                            cu.execute("update table login set mobilenumber='"+mob+"'where username='"+uname+"'")
                            con.commit()
                        elif s==2:
                            hn = input("Enter the House name/Flat no: ")
                            ci= input("Enter the City: ")
                            st= input("Enter the  state : ")
                            cur.execute("update table login set housename='"+ hn +"'city='"+ci+"'state='"+state+"'")
                            con.commit()
                        elif s==3:
                            email = input("Enter the email : ")
                            cur.execute("update table login set email='"+email+"'where username='"+uname+"'")
                            con.commit()
                        else:
                            admin()
       
                                     
def usercreate() :
    uname = input("Enter the username : ")
    c=generateOTP()
    print("OTP is ",c)
    i=str(input("Enter OTP: "))
    passwordcheck(c,i)
    password=str(input("SET PASSWORD :"))
    mobile =str(input("Enter mob_no :"))
    cur = con.cursor()
    cur.execute("create table userdetails(uname varchar(20),password number(8),mobile number(10))")
    cur.execute("insert into userdetails values('"+uname+"','"+password+"','"+mobile+"')")
    con.commit()
    main()
def main() :
        print("1.USER LOGIN")
        print("2.CREATE USER ACCOUNT")
        print("3.VEHICLE OWNER LOGIN")
        print("4.CREATE V_OWNER ACCOUNT")
        choice=int(input("Enter your choice :"))
        if choice == 1:
                userlogin()
                main()
        elif choice == 2:
                usercreate()
                main()
        elif choice == 3:
                admin()
                main()
        elif choice == 4:
                register()
                main()
        else:
                print("Enter correct choice")
                main()
        

print("\n================================WELCOME=============================\n")
print("**************************** CAR BOOKING *****************************\n\n")
main()
