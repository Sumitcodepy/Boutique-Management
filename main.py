import mysql.connector
import time

connect_me = mysql.connector.connect(
    host = "localhost" , user = "root",
    password = "Happy12#" , database = "boutique"
)

mycursor = connect_me.cursor()

def check_id() :
   
   qry_1 = "SELECT c_id FROM customer;"

   mycursor.execute(qry_1)

   ids_all = mycursor.fetchall()

#    Above Statement fetches the ids from database in form of tuples . Each customer have a seperate tuple , which contains single
#    element i.e. ids which is fetched.
 
   list_ids = []
   id = 0

   for id in ids_all :
      list_ids.append(id[0])
   return list_ids  

def crt_acc() :
   
   ask = 'Y'
   list_of_ids = check_id()

   while ask in ("yY") :

      
      

      print("Create a New Account")
      print(" ")
      cust_id = int(input("Enter your Customer ID :"))

      if cust_id in list_of_ids :
         print("You have an existing account , you can't register with this customer id.")
         return 2
      
      # Solve it Error Above
   
      else :
         cust_fname = input("Enter Your First Name :")
         cust_lname = input("Enter Your Last Name :")
         cust_phone = input("Enter Your Contact Number :")
         cust_address = input("Enter Your address :")

      cust_info = (cust_id,cust_fname,cust_lname,cust_phone,cust_address)

      qry = "INSERT INTO customer (c_id, c_fname, c_lname, c_phone, c_address) VALUES (%s,%s,%s,%s,%s);"

      value = cust_info

      mycursor.execute(qry,value)
      connect_me.commit()

      print("Your Details Are Submitted.")
      ask = input("Do you want to continue(Y/N) :")

      if ask not in "Yy" :
         break
      
def get_bk_pr(c_id) :

  

  qry = "SELECT c_productbk FROM customer WHERE c_id = %s;"

  mycursor.execute(qry,(c_id,))

  product = mycursor.fetchone()

  bk_product = product[0]
  return bk_product

def pr_list() :

  qry = "SELECT p_id FROM products;"

  mycursor.execute(qry)

  pr_id = mycursor.fetchall()
  list_pr_id = []

  for id in pr_id :
    list_pr_id.append(id)
    return list_pr_id

def log_in() :
 cust_id = int(input("Enter your Customer ID :"))
 i = 1
 list_of_ids = check_id()
 while i == 1 :
  if cust_id in list_of_ids :
     
     print(" ")
     ask = input('''
     What's your motive :
     1. View your Booked Products
     2. Book a new product
     3. Update the self details
     4. Delete Booking
     
     Enter null to exit..
     Enter your choice :''')

     if ask == "1" :
       p = get_bk_pr(cust_id)

       if p is None or p == '' or p== 0 :
         print("You don't have any products booked.")
         time.sleep(1)

       elif p > 0 :
         q = p.split('-')
         print("Your products are :")
         for prds in q :
           print(prds)
           
     if ask == "2" :
      while ask == "2" :
       print("To Book a new product")
       pd_id = input("Enter The ID of product : ")

       pd_ids = pr_list()
       
       if pd_id in pd_ids :
          print("Your Product is available with us ")
          print("Your Product Booking is on the way..")
          c_id = cust_id
          qry = "INSERT INTO customer (c_productbk) VALUES (%s) WHERE c_id = %s;"

          mycursor.execute(qry,pd_id,c_id)
          connect_me.commit()
          print("Your Product Booked Successfully")
          ans = input("Do You want to add more products (Y/N) :")
          ask = 2 if ans in 'Yy' else  0
          if ask == 0 :
            i = "1"
          else :
            exit()

     if ask == "3" :
         print(''' To Update :
         Contact No. = 0
         Address     = 1''')
         ans = input("Enter your choice :")

         # if ans == 0 :
           


   
       



print ("Welcome to Vogue Services")

while True :

   print('''Please specify yourself 
        A. Customer
        B. Employee
        C. Management
         
        type e to exit ! ''')

   choice = input("Enter : ")

   

      
   if choice in ('a','A') :
      choose = int(input ('''1. Sign Up 
2. Log In 
Enter : '''))

      if (choose == 1) :
         crt_acc()
         
      elif(choose == 2) :
         log_in()
         
      while not (choose == 1 | choose == 2) :
         choose = int(input("Invalid Input. Try Again :"))

   elif choice in ('b','B') :
      pass

   elif choice in ('c','C') :
      pass
      
   elif choice in ('e',"E") :
      print("Thanks For Visiting , Come Again")
      break

   else :
      print("Enter Valid Input")
      break