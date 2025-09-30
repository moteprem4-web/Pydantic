from pydantic import BaseModel, EmailStr,AnyUrl,Field

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='name of the patient',description='This is the name of the patient',example='Prem Mote')]
    age:int=Field(gt=0,lt=120) #for the optional field
    weight:Annotated[float,Field(gt=0,strict=True)] #strict=doe not allow the type conversion
    married:Annotated[bool,Field(default=None,description='Marital status of the patient yes or no ')]
    email: EmailStr
    linkedin_url: AnyUrl
    allergies:Optional[List[str]]=None
    contacts:Dict[str,str]


Patient_info = {
    "name": "John Doe", 
    "age": 45,
    "weight": 98,
    "email": "pr@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe",
    "married": True,
    # "allergies": ["Peanuts", "DUST"],
    "contacts": {"home": "123-456-7890", "work": "987-654-3210"}

}

def insert_patient(patient: Patient):
    # Simulate inserting patient into a database
    print(f"Inserting patient into database name: {patient.name},\n age: {patient.age},\n weight:{patient.weight},\n allergies:{patient.allergies},\n contacts:{patient.contacts},\n Email:{patient.email},\n linkedin_url:{patient.linkedin_url} ")

def update_patient(patient: Patient):
    # Simulate updating patient in a database
    print(f"Updating patient in database name: {patient.name}, age: {patient.age} ")


patient1= Patient(**Patient_info)
print(patient1)

insert_patient(patient1)
update_patient(patient1)

