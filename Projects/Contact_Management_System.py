'''
Contact management system.

Key features to consider : 
1. Adding new contacts : name, phone, address and email
2. View all contacts
3. Search for a contact by name or phone
4. UPdate contact details
5. Delete contact details

Storing all the contacts in CSV file

function 1 : Adding contacts : 
    Name
    phone number
    email
    add them to CSV file

function 2 : View all contacts
    display all the contacts saved in name sorted in ascending order
    extract the contacts from the CSV file

function 3 :
    Search for the contact in CSV stored file

function 4:
    update the existing contact with new phone or new address or new enail

function 5:
    delete the contact fromn the list

'''

import csv
import os


# Function to add contacts in the file
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter PHone number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Location: ").strip()

    file_exists = os.path.exists('contacts.csv') # This checks if the file exists in the system
    with open('contacts.csv','a',newline='') as file:
        write = csv.writer(file)
        if not file_exists:
            write.writerow(['Name','Phone','Address','Email'])

        write.writerow([name,phone,address,email])

    print("Contact added successfully")

# Function to view the contacts from the file
def view_contacts():
    contacts = []
    try:
        with open('contacts.csv','r') as file:
            read = csv.reader(file)
            next(read) # skips the header row
            for row in read:
                if len(row) == 4:
                    contacts.append(row)

        contacts.sort(key=lambda x : x[0]) # sorts the contact by name in ascending order
        if not contacts:
            print("No contacts found")

        else:
            print("Contacts List: ")
            for contact in contacts:
                print(f' Name : {contact[0]}\n Phone : {contact[1]}\n Address : {contact[2]}\n Email : {contact[3]}\n\n')
            print()

    except FileNotFoundError:
        print("NO contacts found. FIle not found")


# Function of search the contact from the file by name or phone
def search_contact():
    search = input("Enter Name/phone to search : ").strip().lower()
    found = []
    try:
        with open('contacts.csv','r') as file:
            read = csv.reader(file)
            next(read)
            for row in read:
                if len(row) == 4:
                    name, phone, email, address = row
                    if search in name.lower() or search == phone:
                        found.append(row)
                
        if found:
            print("Search Results : ")
            for contact in found:
                print(f'Name : {contact[0]}, Phone : {contact[1]}, Email : {contact[2]}, Address : {contact[3]}')
            print()
        else:
            print("Contact not found")

    except FileNotFoundError:
        print("File not found. Please try again later after reviewing the code")


# Function to update the existing contact from the file
def update_contact():
    name_search = input("Enter contact name to update : ").strip().lower()
    update = []
    updated = False
    try:
        with open('contacts.csv','r') as file:
            read = csv.reader(file)
            header = next(read,None)
            
            for row in read:
                if len(row) == 4:
                    name,phone,address,email = row
                    if name.lower()  == name_search:
                        new_phone = input("Enter the new phone number : ").strip()
                        new_address = input("Enter the new Address : ").strip()
                        new_email = input("Enter new email address : ").strip()
                        update.append([name,new_phone,new_address,new_email])
                        updated =True
                    else:
                        update.append(row)

            if updated:
                with open('contacts.csv','w',newline='') as file:
                    appends = csv.writer(file)
                    if header:
                        appends.writerow(header)
                    appends.writerows(update)
                print("Contact updated successfully")
            else:
                print("COntact not found")
    except FileNotFoundError:
        print("FIle not found. Please review the code ")


# FUnction to delete the contact from the file 
def delete_contact():
    inputs = input("Enter contact to delete : ").strip().lower()
    deleted = False
    contacts = []

    try:
        with open('contacts.csv','r') as file:
            read = csv.reader(file)
            header = next(read,None)
            for row in read:
                if len(row) == 4:
                    name,phone,address,email = row
                    if name.lower() == inputs:
                        confirmed = input("Do you want to Delete the contact : ").strip().lower()
                        if confirmed == 'yes':
                            deleted = True
                        else:
                            contacts.append(row)
                    else:
                        contacts.append(row)

            if deleted:
                print("Contact Deleted Successfully")
                with open('contacts.csv','w',newline='') as file:
                    write = csv.writer(file)
                    if header:
                        write.writerow(header)
                    write.writerows(contacts)
            else:
                print("Contact not founds")
    except FileNotFoundError:
        print("File not found. Please review the code if possible.")



# Main function 

print("**************** Welcome to Contact Management System **********************")
print(" FOr adding new contacts press 1 ")
print(" For viewing all the contacts press 2")
print(" To search for a contact press 3")
print(" TO update the existing contact press 4")
print(" TO delete a contact press 5")
print(" TO exit the application press 0 or exit")
    


while True:
    n = input("Enter a Key : ")
    if n not in ['1','2','3','4','5','0','exit','help']:
        print("You have entered a wrong input. Please enter a correct input or enter help for display the controls")
        continue
    if n == '1':
        add_contact()
    elif n == '2':
        print("\n**** Contact List ****")
        view_contacts()
    elif n == '3':
        search_contact()
    elif n == '4':
        update_contact()
    elif n == '5':
       delete_contact()
    elif n == '0' or n == 'exit':
        print("Thank you for using the application")
        break
    elif n == 'help':
        print(" FOr adding new contacts             press 1 ")
        print(" For viewing all the contacts        press 2")
        print(" To search for a contact             press 3")
        print(" TO update the existing contact      press 4")
        print(" TO delete a contact                 press 5")
        print(" TO exit the application             press 0 or exit")


# End of the code
