import mysql.connector as ch
import random
conn=ch.connect(host='localhost',user="root",passwd='HimankSP4@2021',database='chirag')

cur=conn.cursor()

i=random.randint(100001,999998)

def railsmenu():
                print("| * * * Railway Reservation * * * |")
                print("|---------------------------------|")
                print("| 1. Train Detail                 |")
                print("| 2. Reservation of Ticket        |")
                print("| 3. Cancellation of Ticket       |")
                print("| 4. Display PNR                  |")
                print("| 5. Quit                         |")
                print("|---------------------------------|")
                print()
                n=int(input("| Enter your choice : "))
                print()
                if n == 1:
                        train_detail()
                elif n == 2:
                        reservation()
                elif n == 3:
                        cancel()
                elif n == 4:
                        displayPNR()
                elif n == 5:
                        return("You have successfully exit from the program!")
                else:
                        railsmenu()

def train_detail():
    l=[]
    a=str(input("Enter your starting point : "))
    b=str(input("Enter your destination : "))
    l.append(a)
    l.append(b)
    sql="select train_no,cost,starting_point,destination,via,time_of_departure,date_available,status from train_detail where starting_point=%s and destination=%s"
    cur.execute(sql,l)
    f=cur.fetchall()
    l=len(f)
    print()
    for j in range(0,l):
        print("Information for train number - (",j+1,") :")
        print("     Train ID         :", f[j][0])
        print("      Cost            :", f[j][1])
        print("   Starting Point     :", f[j][2])
        print("    Destination       :", f[j][3])
        print("      VIA             :", f[j][4])
        print("  Time of Departure   :", f[j][5])
        print("      Date            :", f[j][6])
        print("     Status           :", f[j][7])
        print()
    print()
    print("===================================================================")
    print()
    railsmenu()

def reservation():
    print("1. Enter YOUR INFORMATION AS FOLLOWS:")
    l=[]
    l1=[]
    l2=[]
    global i
    l.append(i)

    e="select uname from user_information where unique_id=%s"
    cur.execute(e,l)
    f=cur.fetchall()

    if f == []:
            a=str(input("Enter passenger's name : "))
            l.append(a)
            b=str(input("Enter your age : "))
            l.append(b)
            c=str(input("Enter your gender (Male/Female/Others) : "))
            l.append(c)
            d=str(input("Enter train_no : "))
            l.append(d)
            l1.append(d)
            l2.append(d)

            e="select starting_point,destination,status from train_detail where train_no=%s"
            cur.execute(e,l1)
            f=cur.fetchall()
            
            if f == []:
                print("Kindly enter the correct train number!")
            else:
                w=f[0]
                x=w[0]
                t=w[1]
                xt = w[2]
                if xt == 'AVAILABLE':
                    print("Starting Point : ",x)
                    print("Destination : ",t)
                    l.append(x)
                    l.append(t)
                    g="insert into user_information(unique_id,uname,age,gender,train_no,starting_point,destination)values(%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(g,l)
                    conn.commit()
                    print()
                    print("Information uploaded")
                    Z="select cost from train_detail where train_no=%s"
                    cur.execute(Z,l1)
                    n=cur.fetchall()
                    print()

                    print("You have to pay : ",n[0][0])
                    mn=str(input("Would you like to confirm your seat? (y/n) : "))
                    print()
                    l3=[]
                    l4=[]
                    pop="reserved"
                    dop="not reserved"
                    l3.append(pop)
                    l4.append(dop)
                    l5=l3+l1
                    l6=l4+l1
                    
                    if mn=="y":
                        print("Your ticket is reserved (or) confirmed!")
                        print("In case of cancellation your unique_id is : ",l[0])
                        print()
                        mysql="update user_information set reservation=%s where train_no=%s"
                        cur.execute(mysql,l5)
                        conn.commit()
                    elif mn=="n":
                        print("Your ticket is not reserved")
                        print()
                        mysql="update user_information set reservation=%s where train_no=%s"
                        cur.execute(mysql,l6)
                        conn.commit()
                    else:
                        print("Wrong option!")
                        print()
                        railsmenu()
                else:
                    print()
                    print("Train fully filled!")
    else:
            l.pop()
            i = random.randint(100001,999998)
            l.append(i)
            a=str(input("Enter passenger's name : "))
            l.append(a)
            b=str(input("Enter your age : "))
            l.append(b)
            c=str(input("Enter your gender (Male/Female/Others) : "))
            l.append(c)
            d=str(input("Enter train_no : "))
            l.append(d)
            l1.append(d)
            l2.append(d)

            e="select starting_point,destination,status from train_detail where train_no=%s"
            cur.execute(e,l1)
            f=cur.fetchall()
            
            if f == []:
                print("Kindly enter the correct train number!")
            else:
                w=f[0]
                x=w[0]
                t=w[1]
                xt = w[2]
                if xt == 'AVAILABLE':
                    print("Starting Point : ",x)
                    print("Destination : ",t)
                    l.append(x)
                    l.append(t)
                    g="insert into user_information(unique_id,uname,age,gender,train_no,starting_point,destination)values(%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(g,l)
                    conn.commit()
                    print()
                    print("Information uploaded")
                    Z="select cost from train_detail where train_no=%s"
                    cur.execute(Z,l1)
                    n=cur.fetchall()
                    print()

                    print("You have to pay : ",n[0][0])
                    mn=str(input("Would you like to confirm your seat? (y/n) : "))
                    print()
                    l3=[]
                    l4=[]
                    pop="reserved"
                    dop="not reserved"
                    l3.append(pop)
                    l4.append(dop)
                    l5=l3+l1
                    l6=l4+l1
                    
                    if mn=="y":
                        print("Your ticket is reserved (or) confirmed!")
                        print("In case of cancellation your unique_id is : ",l[0])
                        print()
                        mysql="update user_information set reservation=%s where train_no=%s"
                        cur.execute(mysql,l5)
                        conn.commit()
                    elif mn=="n":
                        print("Your ticket is not reserved")
                        print()
                        mysql="update user_information set reservation=%s where train_no=%s"
                        cur.execute(mysql,l6)
                        conn.commit()
                    else:
                        print("Wrong option!")
                        print()
                        railsmenu()
                else:
                    print()
                    print("Train fully filled!")

    print("===================================================================")
    print()
    railsmenu()

def cancel():
    l=[]
    q="not reserved"
    l.append(q)
    a=int(input("Enter the value Of your unique_id provided : "))
    print()
    checker = []
    checker.append(a)
    e="select uname from user_information where unique_id=%s"
    cur.execute(e,checker)
    f=cur.fetchall()
    if f == []:
        print("Wrong unique ID!")
    else: 
        l.append(a)
        b="update user_information set reservation=%s where unique_id=%s"
        cur.execute(b,l)
        conn.commit()
        print("YOUR TICKET IS CANCELLED")
    print("===================================================================")
    print()
    railsmenu()
    
def displayPNR():
    l=[]
    a=int(input("Enter the value Of your unique_id provided : "))
    l.append(a)
    print()
    checker = []
    checker.append(a)
    e="select uname from user_information where unique_id=%s"
    cur.execute(e,checker)
    f=cur.fetchall()
    if f == []:
        print("Wrong unique ID!")
    else:
        sql="select * from user_information where unique_id=%s"
        cur.execute(sql,l)
        f=cur.fetchall()
        print("Your current reservation status is:")
        print("    Unique ID       :",f[0][0])
        print("  Passenger Name    :",f[0][1])
        print("      Age           :",f[0][2])
        print("     Gender         :",f[0][3])
        print("     Train ID       :",f[0][4])
        print("   Starting Point   :",f[0][5])
        print("    Destination     :",f[0][6])
        print(" Reservation Status :",f[0][7])
        print()
    print("===================================================================")
    print()
    railsmenu()

print(railsmenu())
    
    