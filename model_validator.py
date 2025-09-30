from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Dict

# Pydantic model
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60:
            if 'emergency' not in model.contact_details:
                raise ValueError("Emergency contact is required for patients over 60")
        return model

# Patient data outside the class
Patient_info = {
    "name": "John Doe",
    "age": 98,  # make sure it's int
    "weight": 98,
    "email": "pr@gmail.com",
    "married": True,
    "contact_details": {"home": "123-456-7890", "work": "987-654-3210","emergency":"9529984098"}
}

# Create instance
patient1 = Patient(**Patient_info)

# Example function to update patient
def update_patient_data(patient: Patient):
    print(f"Updating patient in database: name={patient.name}, age={patient.age}")

# Test
update_patient_data(patient1)
