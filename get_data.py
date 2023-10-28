import json 
def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    fun = open(filename,"r",encoding="UTF8").read()
    ls = json.loads(fun)
    return ls
data="randomuser_data.json"
print(get_data(data))