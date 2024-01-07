# Project Details
def Add_Contact():
    n=int(input("Number Of Contacts To Be Add="))
    for i in range(n):
        mob=int(input("Enter Mobile No="))
        name=input("Enter Name=")
        if len(name)==0:
            print("Enter Proper Name")
            break
        else:
            contacts[mob]=name
            print("Contacts Added Sucsessfully")
        
    
def Delete_Cotact():
    dele=int(input("Enter Phone.No to Delete\n"))
    if dele in contacts:
        contacts.pop(dele)
        print('\nDeleted')
    else:
        print("contatct is not existes")

def Show_Contacts():
      if len(contacts)==0:
          print("No Contatcs ")
      else:
          print("SR\tName\t\tMobile")
          sr=1
          for k,v in contacts.items():
               print(sr,'\t',v,'\t',k)
               sr += 1
               

def Update_Contact():
    update_key=int(input("Enter Phone.No to Update\n"))
    if update_key in contacts:
        new_name=input('Enter New Name')
    elif len(new_name)==0:
        print("Enter Proper Name")
        
    else:
        contacts[update_key]=new_name
        print('\nUpdated')   
        
def Clear():
    contacts.clear()
    print("Cleared")
      
             
contacts={9786341247:'Akshyakumar',8645319001:'Prashant',7856901528:'Manisha',9177110349:'Ashvini',7786000010: ' Smita'}
while True:
    ch=int(input("\n\nEnter Choice=\n1:Add_Contact()\n2:Show_Contacts()\n3:Delete_Cotact()\n4.Update_Contact()\n5.Clear()\n6.Exit"))
    if ch==1:
        Add_Contact()
    elif ch==2:
        Show_Contacts()
    elif ch==3:
        Delete_Cotact()
    elif ch==4:
        Update_Contact()
    elif ch==5:
        Clear()
    elif ch==6:
        break
    else:
        print("Invalid Choice")