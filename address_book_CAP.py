"""
//Autumn Capasso
//UMUC 
//Address book python porgram that uses Real expression and Pandas 
"""


import pandas as pd 
import re

def main():
    """main function"""

    contacts = get_contacts()
    contactsdf = pd.DataFrame(contacts,
                              columns=["Firstname", "Lastname", "Zipcode",
                                      "Phonenumber"])

    updated_records = update_format(contactsdf)
    print(updated_records.to_string(index=False))

def get_contacts():
    """Returns list of lists of contacts"""
    
    #Firstname, Lastname, Zipcode, Phonenumber
    
    contacts = [
    ["B@dN@m3", "Johnson", "23435", "808-123-1234"],
    ["Ada", "O'Mally", "12345", "000-000-0000"],
    ["Grace", "Hopper", "35254", "983-245-3535"],
    ["Mary", "Jackson-Smith", "23435", "757-389-8372"],
    ["Dorthy", "Vaughan", "56","567-353-35654323456"],
    ["Mary", "Keller", "8", "875-98766-9"],
    ["Edith", "Clarke","34533", "5678909876545678"],
    ["John", "Doe", "87624", "878-345-2463"],
    ["Jim", "Bob", "98769", "800-777-5555"],
    ["John", "Smith", "34535", "345-355-3452"],
    ["Anna", "Queen", "83752", "453-254-8472"],
    ["Moana", "Princess", "96707", "808-551-5555"],
    ["Sam", "Smith", "24553", "864-284-9328"],
    ["John", "Doe", "87624", "878-345-2463"],
    ["Jim", "Bob", "98769", "800-777-5555"],
    ["Katherine", "Johnson", "23435", "808-123-1234"],
    ["Ada", "Lovelace", "12345", "000-000-0000"],
    ["Grace", "Hopper", "35254", "983-245-3535"],
    ["Mary", "Jackson", "23435", "757-389-8372"],
    ["Dorthy", "Vaughan", "56","567-353-35654323456"],
    ["Mary", "Keller", "8", "875-98766-9"],
    ["Edith", "Clarke","34533", "5678909876545678"],
    ["John", "Doe", "87624", "878-345-2463"],
    ["Jim", "Bob", "98769", "800-777-5555"],
    ["John", "Smith", "34535", "345-355-3452"]
    ]
    
    return contacts
    

def update_format(record):
    record['Firstname'] = record['Firstname'].map(update_name)
    record['Lastname'] = record['Lastname'].map(update_name)
    record['Zipcode'] = record['Zipcode'].map(zip_code)
    record['Phonenumber'] = record['Phonenumber'].map(phone_number)
    return record
    
def update_name(value=None):
    """"function for the name column"""
    # Handle A-Z a-z ' and - in name
    if re.fullmatch('^[a-z \' A-Z]+(-[a-z A-Z]+)?$', value):
        return value.title()
    return ''


def zip_code(value=None):
    """Funtion for the zip code column"""
    if re.fullmatch('\d{5}', value):
        return value.title()
    return ''
    
    
        
    

def phone_number(value=None):
    """Function for the phone number column"""
    if re.fullmatch('\d{3}-\d{3}-\d{4}', value):
        return value.title()
    return ''
    
   

        



if __name__ == '__main__':
    main()
