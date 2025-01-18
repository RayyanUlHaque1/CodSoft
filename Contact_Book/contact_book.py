contacts={}
while True:
  print('\nContact Book App\n')
  print('1. Add Contact')
  print('2. View Contact')
  print('3. Delete Contact') 
  print('4. Search Contact')
  print('5. Update Contact')
  print('6. Total Contact')
  print('7. Exit')

  choose=input('Enter no. to perform action = ')
#To Create
  if choose =='1':
    name=input('Enter Contact name to Add: ')
    if name in contacts:
      print(f'Contact name {name} already exists!: ')
    else:
      age=int(input('Enter Contacts Age: '))
      email=input('Enter Contacts e-mail: ')
      phone_no=int(input('Enter Mobile number: '))
      contacts[name]={'age':(age),'email':email,'mobile':phone_no}
      print(f'Contact name ({name}) is added successfully: ')

#To view
  elif choose =='2':
    name=input('Enter Contact name to view: ')
    if name in contacts:
      contact=contacts[name]
      print(f'Name: {name}||Age: {age}||Mobile: {phone_no}||E-mail: {email}')
    else:
      print(f'There is no such {name} Contact Found: ')

#To Delete
  elif choose =='3':
    name=input('Enter Contact name to Delete: ')   
    if name in contacts:
      del contacts[name]
      print(f'Contact name {name} is deleted Successfully:')
    else:
      print('Contact not Found: ')   

#To Search
  elif choose =='4':
    S_name=input('Enter Contact name to Search: ')
    found=False
    for name, contact in contacts.items():
      if S_name.lower() in name.lower():
        print(f'Name: {name}||Age: {age}||Mobile: {phone_no}||E-mail: {email}')
        found=True
      else:
        print('There is no such Contact name in the Contact book:')
    
#For Update
  elif choose =='5':
    name=input('Enter Contact name to Update: ')
    if name in contacts:
      age=int(input('Enter Updated Age: '))
      email=input('Enter Updated e-mail: ')
      phone_no=int(input('Enter Updated Mobile number: '))
      contacts[name]={'age':(age),'email':email,'mobile':phone_no}
      print('Contact Updated successfully: ')
    else:
      print('Contact not Found with this Name')
#Total Contact:
  elif choose =='6':
    print(f'Total contacts in your Contact book is :{len(contact)}\n')
  elif choose =='7':
    print('Exiting the Contact book.... ')
    break
  else:
    print('\nInvalid Input Choose Between the Given Option: ')

  
  