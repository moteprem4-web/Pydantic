from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address
    

address_dict = {
    "city": "Pune",
    "state": "Maharashtra",
    "pin_code": "411033"
}
address1 = Address(**address_dict)

Patient_info = {
    "name": "John Doe",
    "age": 45,
    "gender": "male",
    "address": address1
}   

patient1 = Patient(**Patient_info)


temp = patient1.model_dump()#make it as model_dump_json
print("\n")
temp = patient1.model_dump(include=['name','gender'])
print("\n")
temp= patient1.model_dump(exclude=['address'])
#when we  don't want to show the state
temp= patient1.model_dump(exclude={'address':['state']})
print(temp)
print(type(temp))

