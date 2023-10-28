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
    c={}
    l=[]
    f=open(data,"r",encoding="UTF8").read()
    ls=json.loads(f)["results"]
    for i in ls:
        c['first_name']= i['name']['first']
        l.append(c)
    return l
data="randomuser_data.json"
print(get_users_data(data))