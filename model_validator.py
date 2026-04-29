from pydantic import BaseModel, EmailStr ,model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):   
    name: str
    gmail: EmailStr
    age: int   
    weight: float 
    hobbies: Optional[List[str]] = None
    contact_details: Dict[str,str|int]   

    @model_validator(mode='after')
    def emergency_contact_details(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('patient is above 60 please mention emergency contact details')
        return model



def patient_data(patient : Patient):
    print(f'this is certified to {patient.name} for being {patient.gmail} well fit at age {patient.age} and weight {patient.weight} and instring this is his hobbies are {patient.hobbies}. for contact details {patient.contact_details}')

patient_info = {'name' :'abhijit' ,'age': 34,'gmail':'xyz@gmail.com', 'weight': 65.800, 'contact_details':{'mobile_num':7276457979, 'emergency':91375691}}

patient_list = Patient(**patient_info)

patient_data(patient_list)