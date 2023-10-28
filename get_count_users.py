import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    c=0
    func=open(data,"r",encoding="UTF*").read()
    ls=json.loads(func)["results"]
    for i in ls:
        k = (i['login']['username'])
        c+=1
    return c
data="randomuser_data.json"
print(get_count_users(data))