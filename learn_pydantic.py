from pydantic import BaseModel, EmailStr , AnyUrl, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):   
    name: str
    gmail: EmailStr
    age: int   
    weight: float 
    hobbies: Optional[List[str]] = None
    contact_details: Dict[str,str|int]   

    @field_validator('gmail')
    def validate_email(cls, value):                 # custom email validator function
        validate_emails = ['hdfc.com','axis.com']    # list of allowed email domains
        domain = value.split('@')[-1]             # extract domain from email

        if domain not in validate_emails:                      # check if domain is in allowed list
            raise ValueError('Email domain not allowed')
        return value
    

    @field_validator('name')     # field validator can be operated in two modes i.e before and after
    @classmethod
    def cap_name(cls, value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def check_age(cls, value):
        if value > 1 and value < 18:
            print('you are not eligible for this certificate')
            raise ValueError('Age must be at least 18')
        return value




def patient_data(patient : Patient): #function to print patient data
    print(f'this is certified to {patient.name} for being {patient.gmail} well fit at age {patient.age} and weight {patient.weight} and instring this is his hobbies are {patient.hobbies}. for contact details {patient.contact_details}')

patient_info = {'name' :'abhijit ankush pise' ,'age': 19,'gmail':'xyz@hdfc.com', 'weight': 65.800, 'contact_details':{'mobile_num':7276457979}}  #dictionary to store patient information

patient_list = Patient(**patient_info)  #creating object of class Patient

patient_data(patient_list)     #calling function to print patient data