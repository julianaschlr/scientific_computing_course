import json

data = '''
{ 
    "name": "Chuck",
    "phone": {
    "type" : "intl",
    "number" : "+1 28882 928292" 
    },
    "email": {
    "hide" : "yes"
    }
}'''
# JSON with objects {} key-value
# saving JSON "String" into a dictionary == info


info = json.loads(data)
print(type(info))
print('Name:', info["name"])
print("Hide:", info["email"]["hide"])

