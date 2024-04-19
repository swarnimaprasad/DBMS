import mysql.connector
import re
from datetime import date

usernumber = 22

transactionno=2002
cnx = mysql.connector.connect(
    user="root", host="localhost", password="hello", database="accessisphere"
)
mycursor = cnx.cursor()


def validate_email(email):
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return pattern.match(email)


def login():
    print("^" * 50)
    print("Welcome Admin")
    print("^" * 50)
    print("Please Enter Valid Username and Password")
    admin_id = str(input("enter username:"))
    password = str(input("enter password:"))
    try:
        query = "Select * From Admin where AdminID='{}' and Password='{}'".format(
            admin_id, password
        )
        mycursor.execute(query)
        rec = mycursor.fetchall()
        cnx.commit()

        if rec:
            print("\tACCESS GRANTED")
            return 1
        else:
            return 0
    
        
    except mysql.connector.Error as err:
        print("Error:", err)
    # else:
    #     print("-" * 50)
    #     print("\tWrong credentials")
    #     print("-" * 50)
    #     return False


def after_login(userid):
    global transactionno
    
    # print("3.See all product categories")
    # print("4.See all products under a productcategory")
    # print("5.See products in cart")
    # print("6.Order products from your cart")
    # print("7.Exit")
    while True:
        print("1.View products")
        print("2.View Cart")
        # print("3.Search Product")
        cart_id = userid             
        print("3.Logout")
        inuu = int(input())
        if inuu == 1:
            mycursor.execute("select distinct(category) from product")
            index = 1
            print("*" * 20)
            for row in mycursor:
                print(index, " -> ", row[0])
                index += 1
            print("*" * 20)
            ch = int(input("enter choice number for category : "))
            if ch == 1:
                cat = "Mobility"
            elif ch == 2:
                cat = "Hearing"
            elif ch == 3:
                cat = "Vision"
            elif ch == 4:
                cat = "Speech"

            sql = "SELECT Name, Product_id FROM product WHERE product.Category = %s"
            val = (cat,)
            mycursor.execute(sql, val)

            print("These are the Availible products for this category:")
            for row in mycursor:
                print(row[1], " ", row[0])

            pro_id = int(input("Enter product id of the required product : "))
            query3 = "select  * from product where product_id= %s"
            val = (pro_id,)
            mycursor.execute(query3, val)
            
            for row in mycursor:
                print("Description  ",row[2])
                print("Price - ",row[5]  )
                print("Company - ",row[6]  )

            cart_ch = int(input("enter 1 to add to cart / else 2 : "))
            print("-"*50)
            if cart_ch == 1:
                qty = int(input("enter quantity"))
                
                print("Your cartID is ",cart_id)
                sql_q = "insert into Cart (cart_id, productID, quantity) values(%s,%s,%s)"
                val2 = (
                    cart_id,
                    pro_id,
                    qty,
                )
                mycursor.execute(sql_q, val2)
                cnx.commit()

                print("Added to cart")
            else:
                print("not added. Retry")
                continue
        elif inuu == 2:
            print("Products in cart are ")
            # query2 = "Select * From logincredentials where username='{}' ".format(
            #         username
            #     )

            sql = "SELECT Product_id,Name FROM product,cart WHERE product.product_ID = cart.productID and cart_id=%s"
            val = (cart_id,)
            mycursor.execute(sql, val)
            result_set = mycursor.fetchall()  
            for row in result_set:
                print(row)  
            cnx.commit()
            sql =  "SELECT SUM(Price) FROM product INNER JOIN cart ON product.Product_ID = cart.productID WHERE cart.cart_id = %s GROUP BY cart.cart_id"
            val = (cart_id,)
            mycursor.execute(sql, val)
            res=mycursor.fetchone()
            
            if res is not None:
                totalprice = res[0]
                print("Total price is", totalprice)
            else:
                print("No items in the cart")
                continue

            cnx.commit()


            while True:
                print("1. to place order")
                print("2. exit")
                order_ch=int(input("enter choice "))
                
                if order_ch==1:
                   
                  
                    sql = "SELECT * from Users WHERE Users.UserID=%s"
                    val = (userid,)
                    mycursor.execute(sql, val)
                    re = mycursor.fetchone()  
                    State=re[6]
                    City=re[7]
                    Street=re[8]
                    Pincode=re[10]
                    cnx.commit()

                    # sql = "SELECT SUM(Quantity) FROM Cart WHERE cart_id=%s"
                    # val=(cart_id,)
                    # re = mycursor.fetchall()
                    # if re:  # Check if any rows are returned
                    #     qty = re[0][0]  # Access the first element of the first row
                    #     print("Total Quantity in Cart:", qty)
                    # else:
                    #     print("No items in the cart")



                    pc=int(input("enter your payment mode \n 1- UPI\n 2- Cash \n 3-Card\n enter: "))
                    if pc==1:
                        PaymentMode="UPI"
                    elif pc==2:
                        PaymentMode="Cash"
                    elif pc==3:
                        PaymentMode="Card"
                    transactionno+=1 
                    transactionid=transactionno
                    date_today = date.today()
                    # Orderstatus="Pending"
                    Deliveryworkerid=3
                   

                    sql="INSERT INTO OrderTable ( Cart_id, Discount,  State, City, PaymentMode, Street, Pincode, TransactionID, ProductAmount, DeliveryworkerID,  UserID, OrderDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(cart_id,0,State,City,PaymentMode,Street,Pincode,transactionid,totalprice,Deliveryworkerid,userid,date_today)
                    mycursor.execute(sql, val)
                    cnx.commit()

                    # sql="DELETE FROM Cart WHERE cart_id=%s"
                    # val=(cart_id,)
                    # mycursor.execute(sql, val)
                    # cnx.commit()
                    print("Order Placed")



                    break
                else :
                    print("Exited")
                    break



        elif inuu == 3:
            print("Logged out")
            break


# baadne
def signup():
    global usernumber
    while True:

        print("^" * 50)
        userID = usernumber + 1
        usernumber += 1
        username = str(input("enter username:"))
        password = str(input("enter password:"))
        print("^" * 50)

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        phonenumber = input("Enter Phone Number: ")
        emailaddress1 = input("Enter Email Address1: ")
        emailaddress2 = input("Enter Email Address2 (optional): ")
        if not emailaddress2:
            emailaddress2 = None
        state = input("Enter State: ")
        city = input("Enter City: ")
        street = input("Enter Street: ")
        apartmentno = input("Enter Apartment No: ")
        pincode = input("Enter Pincode: ")
        landmark = input("Enter Landmark: ")

        # Validations
        if len(phonenumber) != 10:
            print("Error: Only 10 digits allowed for Phone Number")
            continue
        if not validate_email(emailaddress1):
            print("Error: Email Address1 isn't valid")
            continue
        if emailaddress2 and not validate_email(emailaddress2):
            print("Error: Email Address2 isn't valid")
            continue

        # Insert into database
        try:
            sql1 = "INSERT INTO Users (UserID, name, Age, PhoneNumber1, EmailAddress1, EmailAddress2, State, City, Street, ApartmentNo, Pincode, Landmark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val1 = (
                userID,
                name,
                age,
                phonenumber,
                emailaddress1,
                emailaddress2,
                state,
                city,
                street,
                apartmentno,
                pincode,
                landmark,
            )
            sql2 = "INSERT INTO logincredentials (UserID, username,password) VALUES (  %s,  %s, %s)"
            val2 = (
                userID,
                username,
                password,
            )
            mycursor.execute(sql1, val1)
            mycursor.execute(sql2, val2)
            cnx.commit()  # Commit the changes to the database
            print("User signed up successfully!")
            break
        except mysql.connector.Error as err:
            if err.errno == 1062:
                print("Error: Duplicate entry. UserID or Email Address already exists.")
            elif err.errno == 1406:
                print("Error: Input value too long. Please provide shorter values.")
            elif err.errno == 1264:
                print("Error: Age value is too big. Please provide a smaller value.")
            elif err.errno == 3819:
                print(
                    "Error: Invalid input format for Email Address/ Age incorrect/phone number/ pincode. Please provide a valid email address."
                )
            else:
                print(
                    "Error, try with valid entries. try entering all essential details:"
                )
        finally:
            mycursor.close()  # Close the cursor
            # cnx.close()  # Close the connection


# def signup():
#     while True:
#         userID = input("Enter UserID: ")
#         name = input("Enter Name: ")
#         age = input("Enter Age: ")
#         phonenumber = input("Enter Phone Number: ")
#         emailaddress1 = input("Enter Email Address1: ")
#         emailaddress2 = input("Enter Email Address2 (optional): ")
#         state = input("Enter State: ")
#         city = input("Enter City: ")
#         street = input("Enter Street: ")
#         apartmentno = input("Enter Apartment No: ")
#         pincode = input("Enter Pincode: ")
#         landmark = input("Enter Landmark: ")
#         cnx.commit

#         # Validations
#         if len(phonenumber) != 10:
#             print("Error: Only 10 digits allowed for Phone Number")
#             continue
#         if not validate_email(emailaddress1):
#             print("Error: Email Address1 isn't valid")
#             continue
#         if emailaddress2 and not validate_email(emailaddress2):
#             print("Error: Email Address2 isn't valid")
#             continue

#         # Insert into database
#         try:

#             sql = "INSERT INTO Users (UserID, name, Age, PhoneNumber1, EmailAddress1, EmailAddress2, State, City, Street, ApartmentNo, Pincode, Landmark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#             val = (userID, name, age, phonenumber, emailaddress1, emailaddress2, state, city, street, apartmentno, pincode, landmark)
#             mycursor.execute(sql, val)

#             print("User signed up successfully!")
#             break
#         except mysql.connector.Error as err:
#             if err.errno == 1062:
#                 print("Error: Duplicate entry. UserID or Email Address already exists.")
#             elif err.errno == 1406:
#                 print("Error: Input value too long. Please provide shorter values.")
#             elif err.errno == 1264:
#                 print("Error: Age value is too big. Please provide a smaller value.")
#             elif err.errno == 3819:
#                 print("Error: Invalid input format for Email Address. Please provide a valid email address.")
#             else:
#                 print("Error, try with valid entries:", err.msg)


def add_product():
    print("Add a Product")
    name = input("Enter Product Name: ")
    description = input("Enter Product Description: ")
    company_name = input("Enter Company Name: ")
    category = input("Enter Product Category: ")
    status = input("Enter Product Status (True/False): ")
    supplier_id = input("Enter Supplier ID: ")
    quantity = input("Enter Quantity: ")

    # Insert into database
    try:
        sql = "INSERT INTO Product (Name, Description, Company_name, Category, Status, SupplierID, Quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name, description, company_name, category, status, supplier_id, quantity)
        mycursor.execute(sql, val)
        cnx.commit()
        print("Product added successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)

def display_delivery_workers():
    try:
        # Establish connection to the database
        # cursor = cnx.cursor()

        # Execute SQL query to retrieve delivery workers data
        query = ("SELECT ID, workerName, Age, City FROM DeliveryWorker")
        mycursor.execute(query)

        # Print column headers
        print("{:<5} {:<15} {:<5} {:<15} ".format(
            "ID", "Name", "Age", "City"))
        print("="*50)

        # Iterate over the rows and print each delivery worker's information
        for (ID, workerName, Age, City) in mycursor:
            print("{:<5} {:<15} {:<5} {:<15}".format(
                ID, workerName, Age, City))

        # Close cursor and connection
        
    except mysql.connector.Error as err:
        print("Error:", err)

def add_ngo():
    print("Add an NGO")
    name = input("Enter NGO Name: ")
    # company_id = input("Enter Company ID: ")
    description = input("Enter NGO Description: ")
    email = input("Enter Email Address: ")
    address = input("Enter Address: ")
    contact_number = input("Enter Contact Number: ")

    try:
        sql = "INSERT INTO NGOs (Name, Description, Email, Address, ContactNumber) VALUES (%s, %s, %s, %s, %s)"
        val = (name, description, email, address, contact_number)
        mycursor.execute(sql, val)
        cnx.commit()
        print("NGO added successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)

def get_active_users_count():
    try:
        # Execute SQL query to count the number of active users
        query = "SELECT COUNT(*) AS ActiveUsersCount FROM Users WHERE account_status = 'Active';"
        mycursor.execute(query)
        result = mycursor.fetchone()
        active_users_count = result[0]
        print(f"The number of active users are : {active_users_count}")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")


def display_user():
    try:
        # Establish connection to the database

        # Execute SQL query to fetch user information
        query = ("""
            SELECT u.UserID, u.name, COUNT(o.OrderID) AS TotalPurchases
            FROM Users u
            LEFT JOIN OrderTable o ON u.UserID = o.UserID
            GROUP BY u.UserID, u.name
            HAVING COUNT(o.OrderID) >= 1
        """)
        mycursor.execute(query)

        # Print column headers
        print("{:<10} {:<30} {:<15}".format(
            "User ID", "User Name",  "Total Purchases"))
        print("="*60)

        # Iterate over the rows and print user information
        for (UserID, name, TotalPurchases) in mycursor:
            print("{:<10} {:<30} {:<15}".format(
                UserID, name, TotalPurchases))

        # Close cursor and connection
        

    except mysql.connector.Error as err:
        print("Error:", err)
    
def inventory_analysis():
    try:
        # Establish connection to the database

        # Execute SQL query for inventory analysis
        query = ("""
            SELECT p.Product_ID, p.Name, p.Quantity, s.Name AS Supplier, s.City AS SupplierCity, s.State AS SupplierState
            FROM Product p
            JOIN Supplier s ON p.SupplierID = s.SupplierID;
           
        """)    
        mycursor.execute(query)

        # Print column headers
        print("{:<10} {:<30} {:<10} {:<20} {:<15} {:<15}".format(
            "Product ID", "Product Name", "Quantity", "Supplier", "Supplier City", "Supplier State"))
        print("="*100)

        # Iterate over the rows and print product information
        for (Product_ID, Name, Quantity, Supplier, SupplierCity, SupplierState) in mycursor:
            print("{:<10} {:<30} {:<10} {:<20} {:<15} {:<15}".format(
                Product_ID, Name, Quantity, Supplier, SupplierCity, SupplierState))


        # Close cursor and connection
    

    except mysql.connector.Error as err:
        print("Error:", err)

def view_product_sales():
    
    try:
        # Establish connection to the database


        # Execute SQL query to fetch product sale statistics from the view
        query = ("SELECT Product_Name, Supplier_Name, Total_Units_Sold, Total_Sales_Amount FROM ProductSalesSummary")
        mycursor.execute(query)

        # Print column headers
        print("="*110)
        print("{:<30} {:<30} {:<20} {:<20}".format(
             "Product Name", "Supplier Name", "Total Units Sold", "Total Sales Amount"))
        print("="*110)

        # Iterate over the rows and print product sale statistics
        for (Product_Name, Supplier_Name, Total_Units_Sold, Total_Sales_Amount) in mycursor:
            print("{:<30} {:<30} {:<30} {:<20} ".format(
                Product_Name, Supplier_Name, Total_Units_Sold, Total_Sales_Amount))


    except mysql.connector.Error as err:
        print("Error:", err)


while True:

    # print("3.See all product categories")
    # print("4.See all products under a productcategory")
    # print("5.See products in cart")
    # print("6.Order products from your cart")
    # print("7.Exit")
    print("1. Admin Login")
    print("2. User Portal")
    login_input = int(input("Enter 1 for Admin Login / Enter 2 for User Activities \n "))

    if login_input == 1:
            exitf=0  
            while True:
                if exitf==1:
                    exitf=0
                    break
                
                log_attempt = login()
                if log_attempt:
                    while True :
                        print(" Admin Menu : Enter digit accordingly")
                        print("*" * 50)
                        print("1. Add Product")
                        print("2. Add NGO")
                        print("3. Show Delivery workers general information ")
                        print("4. See the number of Active users ")
                        print("5. Show Analysis of the current inventory")
                        print("6. Display Users with alteast one purchase")
                        print("7. View Product Sale Stats")
                        print("8. Logout")
                        print("*" * 50)
                        chk = int(input())
                        if chk == 1:
                            add_product()
                        if chk == 2:
                            add_ngo()
                        if chk==3:
                            display_delivery_workers()
                        if chk == 4:
                            get_active_users_count()
                        if chk==5:
                            inventory_analysis()
                        if chk==6:
                            display_user()
                        if chk==7:
                            view_product_sales()
                        if chk == 8:
                            print("Exiting")
                            exitf=1
                            break
                elif log_attempt != True:
                    print("try again")
                    continue
                

    # admin_login_count = 0
    # if login_input == 1:
    #     while(True):
    #         log_attempt = login()
    #         print(" Admin Menu : Enter digit accordingly")
    #         if log_attempt:
    #             print("*"*50)
    #             print("1. Add Product")
    #             print("2. Add NGO")
    #             print("3. Show Delhivery workers")
    #             print("4. See the number of Active users ")
    #             print("5 Exit")
    #             print("*"*50)
    #             chk = int(input())
    #             if chk == 1:
    #                 add_product()
    #             if chk == 2:
    #                 add_ngo()
    #             if chk == 4:
    #                 get_active_users_count()
    #             if chk==5:
    #                 break



        # while login() != True:
        #     admin_login_count += 1
        #     if admin_login_count == 3:
        #         break
        #     login()

    elif login_input == 2:
        print("1.Sign up")
        print("2.Log In")
        print("3.Exit")
        inuu = int(input("enter your choice"))
        if inuu == 1:
            signup()
        elif inuu == 2:

            print("^" * 50)
            print("Login as USER")
            print("^" * 50)
            logincount = 0
            while True:

                if logincount == 4:
                    break
                print("^" * 50)
                print("Please Enter your username")
                username = str(input("enter username:"))
                query2 = "Select * From logincredentials where username='{}' ".format(
                    username
                )
                mycursor.execute(query2)

                rec_recheck = mycursor.fetchone()

                if rec_recheck:
                    userid = rec_recheck[0]
                    print("your user id-",userid)
                    status_query = (
                        "Select account_status From users where userid='{}' ".format(
                            userid
                        )
                    )
                    mycursor.execute(status_query)

                    bl = mycursor.fetchone()
                    b = bl[0]
                    if b == "Blocked":
                        print("^" * 50)
                        print("Blocked userid")
                        print(" Can't Enter ")
                        break
                    password = str(input("enter password:"))
                    pass_query = (
                        "Select * From logincredentials where Password='{}' ".format(
                            password
                        )
                    )
                    mycursor.execute(pass_query)
                    pass_recheck = mycursor.fetchall()

                    if pass_recheck:
                        print("^" * 50)
                        print("ACCESS GRANTED")
                        
                        after_login(userid)
                        #! to include rest of the code
                        break
                    else:
                        logincount += 1
                        print("Password Incorrect")
                        print(" Restarting ")
                        insert_attempt = (
                            "INSERT INTO login_attempts (UserID) VALUES (  %s)"
                        )
                        val2 = (userid,)
                        mycursor.execute(insert_attempt, val2)
                        cnx.commit()
                else:
                    print("wrong username")
        elif inuu == 3:
            print("You have logged out as user")
            break
