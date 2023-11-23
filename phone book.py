import os
import csv
import datetime

def title():
    line_1 = ("_________________________")
    line_2 = "-------------------------"
    title = ("contact management system")
    print(line_1.center(130))
    print(title.center(130))
    print(line_2.center(130))


class contact_functions:
    contact_fields = ["Name", "Mobile_No"]
    contact_database = "Contacts.csv"
    contact_data = []

    def create(self):
        os.system("cls")
        title()
        print("create contact: ")
        print(" _ _ _ _ _  _ ")
        print("")

        for field in self.contact_fields:
            contact_details = input(f"    enter {field}: ")
            print("")
            self.contact_data.append(contact_details)

        date = datetime.datetime.today().strftime("%B %d %Y")
        self.contact_data.append(date)

        with open(self.contact_database, "a") as file:
            write = csv.writer(file)
            write.writerow(self.contact_data)
        self.contact_data = []
        print("")
        print("contact is created successfully".center(129))
        print("\n")

    def view(self):
        os.system("cls")
        title()
        print("contact: ".center(10))
        print("___________".center(10))
        print("")

        count = 0
        with open(self.contact_database, "r") as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count += 1
        print(" total contact:", count)
        print("")

        with open(self.contact_database, "r") as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("contact book is empty, please create contact".center(129))
            else:
                for field in self.contact_fields:
                    print("{0:<10}".format(field).center(10), end="\t\t")
                print('{0:<10}'.format("date"))
                print('{:<10}\t\t{:<10}\t\t{:<10}'.format("_________", "_________", "_________"))
                print("")

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(10), end="\t\t")
                    print("")
        print("\n")
        input("\t press enter key to continue..".center(120))
        os.system("cls")

    def search(self):
        os.system("cls")
        title()
        print("search contacts:".center(10))
        print("______________".center(10))
        print("")

        contact_match = False
        search_value = input("enter your name: ")
        print("")

        for field in self.contact_fields:
            print("{0:<10}".format(field).center(10), end="\t\t")
        print('{0:<10}'.format("date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format("_________", "_________", "_________"))
        print("")

        with open(self.contact_database, "r") as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        contact_match = True
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2].center(10)))
        if not contact_match:
            print("")
            print("Sorry, there is no contact with this name".center(129))
        print("")

    def delete(self):
        os.system("cls")
        title()
        print("delete contacts:".center(10))
        print("______________".center(10))
        print("")

        contact_match = False
        delete_value = input("enter the name to delete: ")
        update_list = []

        with open(self.contact_database, "r") as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        contact_match = True

        if contact_match:
            with open(self.contact_database, "w", newline="") as file:
                write = csv.writer(file)
                write.writerows(update_list)
            print("")
            print("Contact deleted successfully!".center(129))
        else:
            print("")
            print("Sorry, data not found".center(129))
        print("")


contact_class = contact_functions()

os.system("cls")
title()

while True:
    print("1. View Contact".center(128))
    print("2. Create Contact".center(129))
    print("3. Search Contact".center(129))
    print("4. Delete Contact".center(129))
    print("5. Exit".center(120))
    print("______________.".center(131))
    option = int(input("\t\t\t\t\t\t\t\t\t\tChoose your option: "))

    if option == 1:
        contact_class.view()
        title()
    elif option == 2:
        while True:
            contact_class.create()
            ans = input("\t\t\t\t\t\tdo you want to create contact number?[Y/N]: ")
            if ans.lower() == "y":
                continue
            else:
                break
        os.system("cls")
        title()
    elif option == 3:
        while True:
            contact_class.search()
            ans = input("\t\t\t\t\t\tdo you want to search again?[Y/N]: ")
            if ans.lower() == "y":
                continue
            else:
                break
        os.system("cls")
        title()
    elif option == 4:
        while True:
            contact_class.delete()
            ans = input("\t\t\t\t\t\tdo you want to delete contact number?[Y/N]: ")
            if ans.lower() == "y":
                continue
            else:
                break
        os.system("cls")
        title()
    elif option == 5:
        break
