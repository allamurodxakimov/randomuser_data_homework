import json

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    c={}
    f=open(data,'r',encoding="UTF8").read()
    ls=json.loads(f)['results']
    l=[]
    for i in ls:
        if i["gender"]=="male":
            c["Male"]=1
            l.append(c)
        elif i["gender"]=="female":
            c["Female"]=0
            l.append(c)
    return l
data="randomuser_data.json"
print(get_gender_users(data))