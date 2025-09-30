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
    'gender':'male',
    'address': address1
}   


patient1 = Patient(**Patient_info)
print(patient1)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin_code)

