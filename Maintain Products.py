import os
import platform
global products
# create product dictionary
products=dict()
def create_product_database():
    products['pen']={"company":"reynolds", "price":25}
    products['pencil']={"company":"natraj","price":15}
    products['notebook']= {"company":"rotomac", "price":80}
         
    

create_product_database()


def manageProduct():
       x = "#" * 30
       y = '=' * 28
       global bye
       bye = "\n {} \n# {} #\n# ===> Brought To You By <=== #\n# ====> code-projects.org <=== #\n# {} #\n {}".format(x,
                                                                                                                     y,
                                                                                                                     y,
                                                                                                                     x)
       print("""

    ------------------------------------------------------------------------------
    |=============================================================================|
    |===============Welcome to Prodcuts System==========================|
    |=============================================================================|
    ------------------------------------------------------------------------------

    Enter 1 : To view Products list
    Enter 2 : To Get price of a product
    Enter 3 : To Delete a product
    Enter 4 : To get total price of all the products
    Enter 5 : Add product
    Enter 6 : Modify price of an product
    """)

       try:
              userInput = int(input("Please select and above option: "))
       except ValueError:
              print("That's not a number ")
       else:
              print("\n")  # print new line
       # checking using option
       if(userInput == 1):
           for key in products.keys():
               print(key,products[key])
       elif(userInput == 2):
           product=input("Enter product name: ")
           for i in products:
               if i==product:
                   print(products[i]["price"])
                   break
       elif(userInput == 3):
            product = input("Enter product name: ")
            for i in products:
                if i == product:
                    products.pop(product)
                    break
            print("After deleting produt ",product)
            print(products)
       elif(userInput == 4):
            total_price=0
            for i in products:
                total_price = total_price+products[i]["price"]
            print("Total price of all the products: ",total_price)
       elif(userInput == 5):
            new_product_name = input("Enter Product Name: ")
            new_product_company = input("Enter company Name of the product: ")
            new_product_price = input("Enter price of the product: ")
            temp_dict = {"company":new_product_company,"price":new_product_price}
            products[new_product_name] = temp_dict
            print(products)
       elif(userInput == 6):
            product = input("Enter product Name: ")
            for i in products:
                if i == product:
                    new_price = input("Enter new price of the product: ")
                    products[i]["price"] = int(new_price)
                    break
            print("After changing price of the product ")
            print(products)
            
                    
        
manageProduct()

def runAgain():
    runAgn = input("\nwant to run again Y/n: ")
    if(runAgn.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageProduct()
        runAgain()
    else:
        print("Goodbye")
runAgain()

           
