from pydantic import BaseModel, EmailStr,computed_field

from typing import Dict

# Pydantic model
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #
    married: bool #meter
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
# Patient data outside the class
Patient_info = {
    "name": "John Doe",
    "age": '45',
    "weight": 98,
    "height":1.75,
    "email": "pr@hdfc.com",
    "married": True,
    "contact_details": {"home": "123-456-7890", "work": "987-654-3210"}
}

# Create a Patient instance
patient1 = Patient(**Patient_info)


# Example function to update patient
def update_patient_data(patient: Patient):
    print(f"Updating patient in database: name={patient.name}, age={patient.age}")
    print(f"Patient BMI is: {patient.bmi}")

# Test
update_patient_data(patient1)
