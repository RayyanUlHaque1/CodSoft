#Create Class Name Calculator:
class Calculator:

#Adding Funtions:
  def add(self,x,y):
    return x+y
  def sub(self,x,y):
    return x-y
  def mul(self,x,y):
    return x*y
  def division(self,x,y):
    if y !=0:
      return x/y
    else:
      return "Error Division by zero...."  
  def mod(self,x,y):
    return x%y
  def pow(self,x,y):
    return x**y

def Calculator_code():
  calc=Calculator()

#Adding Option to Choose :
  while True:
    print("\nSelect Operation:")
    print("Press 1.+")
    print("Press 2.-")
    print("Press 3.*")
    print("Press 4./")
    print("Press 5.%")
    print("Press 6.**")
    print("Press 7.Exit")

#Adding User input:
    choice=input("Press Number: ")
    if choice=='7':
      print("Exiting Calculator: ")
      break

    if choice =='1':
      num_1=int(input("Enter First Number: "))
      num_2=int(input("Enter Second Number: "))
      print(f'{num_1}+{num_2}={calc.add(num_1,num_2)}')
    elif choice =='2':
      num_1=int(input("Enter First Number: "))
      num_2=int(input("Enter Second Number: "))
      print(f'{num_1}-{num_2}={calc.sub(num_1,num_2)}')
    elif choice =='3':
      num_1=int(input("Enter First Number: "))
      num_2=int(input("Enter Second Number: "))
      print(f'{num_2}*{num_2}={calc.mul(num_1,num_2)}')
    elif choice =='4':
      num_1=float(input("Enter First Number: "))
      num_2=float(input("Enter Second Number: "))
      print(f'{num_1}/{num_2}={calc.division(num_1,num_2)}')
    elif choice =='5':
      num_1=float(input("Enter First Number: "))
      num_2=float(input("Enter Second Number: "))
      print(f'{num_1}%{num_2}={calc.mod(num_1,num_2)}')
    elif choice =='6':
      num_1=int(input("Enter First Number: "))
      num_2=int(input("Enter Second Number: "))
      print(f'{num_1}^{num_2}={calc.pow(num_1,num_2)}')
    else:
        print("Choose from the given options : Invalid Input ")

# Final Function Call
Calculator_code()


  