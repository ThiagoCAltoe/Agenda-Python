contacts = []

def add_contact():
  print("")
  print("")
  Name = input("Enter the name of the contact: ")
  Phone = input("Enter the phone number of the contact: ")
  email = input("Enter the email of the contact: ")
  favorite = input("Is this contact a favorite? (yes/no): ").lower()
  contact = {"Name": Name, "Phone": Phone, "email": email, "favorite": favorite}
  contacts.append(contact)
  print("Contact added successfully")

def view_contacts():
  print("")
  print("")
  for contact in contacts:
    print("Name: ", contact["Name"])
    print("Phone: ", contact["Phone"])
    print("Email: ", contact["email"])
    print("Favorite: ", contact["favorite"])
    print("")

def edit_contact():
  print("")
  print("")
  Name = input("Enter the name of the contact you want to edit: ")
  for contact in contacts:
    if contact["Name"] == Name:
      New_Name = input("Enter the name of the contact: ")
      New_Phone = input("Enter the phone number of the contact: ")
      New_email = input("Enter the email of the contact: ")
      New_favorite = input("Is this contact a favorite? (yes/no): ")
      contact["Name"] = New_Name
      contact["Phone"] = New_Phone
      contact["email"] = New_email
      contact["favorite"] = New_favorite
      print("Contact updated")
      break
    print("Contact not found.")

def edit_favorite():
  print("")
  print("")
  Name = input("Enter the name of the contact you want to add to favorites: ")
  for contact in contacts:
    if contact["Name"] == Name:
      if contact["favorite"] == "yes":
        contact["favorite"] = "no"
        print("Contact removed from favorites")
      else:
        contact["favorite"] = "yes"
        print("Contact added to favorites")
      break
    print("Contact not found.")

def view_favorites():
  print("")
  print("")
  for contact in contacts:
    if contact["favorite"] == "yes":
      print("Name: ", contact["Name"])
      print("Phone: ", contact["Phone"])
      print("Email: ", contact["email"])
      print("Favorite: ", contact["favorite"])
      print("")

def delete_contact():
    print("")
    print("")
    Name = input("Enter the name of the contact you want to delete: ")
    found = False
    for index, contact in enumerate(contacts):
        if contact["Name"] == Name:
            del contacts[index]
            found = True
            print("Contact deleted successfully.")
            break
    if not found:
        print("Contact not found.")

while True:
    print("1. Add contact")
    print("2. View list of contacts")
    print("3. Edit contact")
    print("4. Add contact to favorites")
    print("5. View list of favorites")
    print("6. Delete contact")
    option = int(input("Enter your choice: "))
    if option == 1:
      add_contact()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 2:
      view_contacts()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 3:
      edit_contact()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 4:
      edit_favorite()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 5:
      view_favorites()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 6:
      delete_contact()
      input("Press Enter to continue...")
      print("")
      print("")
    elif option == 7:
      print("Exiting..")
      break
    else:
      print("Invalid option!")
      print("")
      print("")