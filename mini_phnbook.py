phone_book={
    "TANISHQ":{"PHONE NUMBER":7015727465},
    "SHUBHAM":{"PHONE NUMBER":7015727466},
    "DEV":{"PHONE NUMBER":7015727467}
}
#ADDING A CONTACT
phone_book["AVNI"]={"PHONE NUMBER":9467838065}
print(phone_book)

#SEARCH FOR A CONTACT
NAME=input("Enter the name of the contact you want to search for:")
if NAME in phone_book:
    print("the phone no of  "+ NAME  + "is " +  str(phone_book[NAME]["PHONE NUMBER"]) )

#DELETING A CONTACT
NAME=input("Enter the name of the contact you want to delete:")
if NAME in phone_book:
    phone_book.pop(NAME)
    print("the contact " + NAME + " has been deleted.") 