import  json
data=''' [{"name":"faiz","password":"faizy@1","age":"19","phonenumber":"92675402335"},
      {"name":"Mahtab","password":"madni@01","age":"16","phonenumber":"235748908734"}]'''
info=json.loads(data)
for item in info:
    print("Name-",item["name"])
    print("Password-",item["password"])
    print("Age-",item["age"])
    print("PhoneNo-",item["phonenumber"])