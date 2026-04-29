from pydantic import BaseModel, EmailStr , AnyUrl, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):   
    name: str
    gmail: EmailStr
    age: int   
    height: float
    weight: float 
    hobbies: Optional[List[str]] = None
    contact_details: Dict[str,str|int]   
    @computed_field
    @property
    def bmi(self) -> float:
        height_in_m = self.height / 100
        BMI = round(self.weight / (height_in_m ** 2), 2)
        return BMI                                                  

   

def patient_data(patient : Patient):
    print(f'this is certified to {patient.name} for being {patient.gmail} well fit at age {patient.age} and weight {patient.weight} and instring this is his hobbies are {patient.hobbies}. for contact details {patient.contact_details} and BMI of patient is {patient.bmi}')

patient_info = {'name' :'abhijit' ,'age': 19,'gmail':'xyz@gmail.com', 'weight': 65.800,'height': 173,  'contact_details':{'mobile_num':7276457979}}

patient_list = Patient(**patient_info)

patient_data(patient_list)