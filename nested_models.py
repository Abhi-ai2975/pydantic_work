from pydantic import BaseModel

class Addrass(BaseModel):
    city: str
    state: str
    pin: int

class patient(BaseModel):
    name: str
    age: int
    gender: str
    addrass: Addrass

addrass_dict = {'city': 'pune', 'state':'maharashtra','pin':410011}
addrass_1 = Addrass(**addrass_dict)

patient_dict = {'name':'abhijit', 'age':19, 'gender':'male', 'addrass':addrass_1}
patient_1 = patient(**patient_dict)

# to dump dict or json 
temp = patient_1.model_dump(exclude= ('name','age')) | patient_1.model_dump(include={'addrass':'city'})

print(temp)
print(type(temp))

print('name: ',patient_1.name)
print('city: ',patient_1.addrass.city)
print('state: ',patient_1.addrass.state)
