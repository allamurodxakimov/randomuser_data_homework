import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    func=open(data,'r',encoding="UTF8").read()
    ls=json.loads(func)["results"]
    l=[]
    for i in ls:
        l.append(i["email"])
    return l
data = 'randomuser_data.json'
print(get_email(data))