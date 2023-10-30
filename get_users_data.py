import json
def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}
    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    l=[]
    for i in data:
        c={}
        c['first_name']= i['name']['first']
        c['first_last']= i['name']['last']
        c['phone_number']= i['phone']
        l.append(c)
    return l
f=open("randomuser_data.json","r",encoding="UTF*").read()
data=json.loads(f)["results"]
print(get_users_data(data))