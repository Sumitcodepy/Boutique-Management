import mysql.connector

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
   
   list_of_ids = check_id()

   print("Create a New Account")
   print(" ")
   cust_id = input("Enter your Customer ID :")

   if cust_id in list_of_ids :
      print("You have an existing account , you can't register with this customer id.")

      
      
       



print ("Welcome to Vogue Services")

while True :

   print('''Please specify yourself 
        A. Customer
        B. Employee
        C. Management
         
        type e to exit ! ''')

   choice = input("Enter : ")

   try :
      
      if choice in ('a','A') :
         choose = int(input ("1. Sign Up \n2. Log In  "))

         if (choose == 1) :
            crt_acc()
         
         elif(choose == 2) :
            pass
         
         while not (choose == 1 | choose == 2) :
            choose = int(input("Invalid Input. Try Again :"))

      elif choice in ('b','B') :
         pass

      elif choice in ('c','C') :
         pass
      
      elif choice in ('e',"E") :
         print("Thanks For Visiting , Come Again")
         break

   except :
      print("Please Enter Valid Input")

