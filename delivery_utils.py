def check_filepath():
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        import json
        package_objects = {
            "id" : [],
            "sender" : [],
            "recipient" : [],
            "status" : []
        }
        file_path1 = os.path.join(BASE_DIR, "packages_record.json")
        if not os.path.exists(file_path1):
            with open(file_path1, "x") as file:
                json.dump(package_objects, file)
        else:
            print("json file called book_record already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")
    

def menu():
    print(".............................................................")
    print()
    print("...     Welcome to ACSP Package Delivery System       ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Register a packagee", "Mark package as delivered", "View all packages", "Save to file", "Load from file", "exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 6:
                print("Kindly choose from the option above")
                print()
                continue
            elif options < 1:
                print("Kindly choose from the option above")
                print()
                continue
            else:
                break
        except:
            print("Please Enter a valid Integer")
            print()
            continue
    return options      
#
def register_option():
    import json
    import uuid
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "packages_record.json")
    with open(file_path, "r") as file:
        old_json = json.load(file)
    while True:
        try:
            sender = input("Enter your package_sender info: \n").lower()
            id = str(uuid.uuid4())
            recipient = input(f"Enter package recipient info: \n").lower()
            status = "pending"
        except Exception as e:
            print(f"Error with the code: {e}")
            continue
        #create an Package object
        package_objects = Package(id, sender, recipient, status)
        #add Package to the object 
        package_objects.add_to_record(old_json)
        with open(file_path, "w") as file:
            json.dump(old_json, file)
        print(f"Package {id} sucessully registered!")
        break


def view_option():
    import json
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "packages_record.json")
    with open(file_path, "r") as file:
        old_json = json.load(file)
    import pandas as pd
    view = pd.DataFrame(old_json)
    return print(view)     


def markdelivered_option():
    import json
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "packages_record.json")
    with open(file_path, "r") as file:
        old_json = json.load(file)
    while True:
        try:  
            id = input(f"copy the package id from the view and insert it here: \n").strip()
            index = old_json['id'].index(id)
            if old_json['status'][index] == "delivered":
                print("package id can't be marked as delivered \nAs it has already been delivered before")
                continue
            elif id in old_json['id']:
                index = old_json['id'].index(id)
                old_json['status'][index] = "delivered"
                print(f"sender: {old_json['sender'][index]}")
                print(f"ID: {old_json['id'][index]}")
                print(f"recipient: {old_json['recipient'][index]}")
                print(f"status: marked as delivered")
                with open(file_path, "w") as file:
                    json.dump(old_json, file)
                break
            else:
                print("package with this ID does not exists:")
        except Exception as e:
            print(f"Error with the code: {e}")
            continue

def save_to_file():
    import json
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "Packages_record.json")
    with open(file_path, "r") as file:
        old_json = json.load(file)
    file_path1 = os.path.join(BASE_DIR, "saved_record.json")
    with open(file_path1, "x") as file:
                json.dump(old_json, file)
    print("Your Packages records has been succeesuly saved as saved_records.json")


def load_from_file():
    import json
    import os
    from models import Package
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_sender = input("only json files!!!, Kindly uploaded your file by typing the file name, *json e.g file.json: \n")
    file_path = os.path.join(BASE_DIR, file_sender)
    with open(file_path, "r") as file:
        uploaded_json = json.load(file)
    file_path1 = os.path.join(BASE_DIR, "Packages_record.json")
    with open(file_path1, "r") as file:
        old_json = json.load(file)
    num_Packages = len(uploaded_json["id"])

    for i in range(num_Packages):
        try:
            sender = uploaded_json["sender"][i]
            id = uploaded_json["id"][i]
            recipient = uploaded_json["recipient"][i]
            status = uploaded_json["status"][i]
            Package_objects = Package(id, sender, recipient, status)
            #add Package to the object 
            Package_objects.add_to_record(old_json)
        except Exception as e:
            print(f"Error at index {i}: {e}")
            continue
        print(f"Package {id} sucessully added!")
    with open(file_path1, "w") as file:
        json.dump(old_json, file)