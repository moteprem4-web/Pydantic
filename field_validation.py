from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Dict

# Pydantic model
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    contact_details: Dict[str, str]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com', 'zealeducation.com']  # added gmail for testing
        domain_name = value.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError(f"Invalid domain: {domain_name}")
        return value
    
    @field_validator('name',mode='after')
    @classmethod
    def transfrom_name(cls, value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def age_validate(cls, value):
        if 0 <= value <= 100:
            return  value
        else:
            raise ValueError("Age must be between 0 and 100")
        
    

# Patient data outside the class
Patient_info = {
    "name": "John Doe",
    "age": '45',
    "weight": 98,
    "email": "pr@hdfc.com",
    "married": True,
    "contact_details": {"home": "123-456-7890", "work": "987-654-3210"}
}

# Create a Patient instance
patient1 = Patient(**Patient_info)


# Example function to update patient
def update_patient_data(patient: Patient):
    print(f"Updating patient in database: name={patient.name}, age={patient.age}")

# Test
update_patient_data(patient1)
