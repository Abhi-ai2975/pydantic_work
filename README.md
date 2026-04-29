# pydantic_work
# Pydantic Examples Collection

A simple collection of examples demonstrating key features of Pydantic, including:

- Computed fields
- Model validators
- Nested models
- Basic Pydantic usage

This project is intended for learning and experimentation with modern Pydantic patterns.

## Project Structure

```bash
.
├── computed_field.py       # Demonstrates @computed_field usage
├── learn_pydantic.py       # Introductory Pydantic examples
├── model_validator.py      # Custom validation with @model_validator
├── nested_models.py        # Working with nested models
└── README.md
```

## Requirements

- Python 3.10+
- Pydantic v2+

Install dependencies:

```bash
pip install pydantic
```

Or with requirements file:

```bash
pip install -r requirements.txt
```

---

# Examples

## 1. Basic Pydantic Models

Run:

```bash
python learn_pydantic.py
```

Covers:

- Creating models
- Type validation
- Default values
- Field constraints
- Parsing input data

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Abhi", age=25)
print(user)
```

---

## 2. Computed Fields

Run:

```bash
python computed_field.py
```

Demonstrates:

- `@computed_field`
- Derived properties
- Automatic calculated values

Example:

```python
from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    tax: float

    @computed_field
    @property
    def total(self):
        return self.price + self.tax
```

---

## 3. Model Validators

Run:

```bash
python model_validator.py
```

Demonstrates:

- `@model_validator`
- Pre-validation
- Post-validation
- Cross-field validation

Example:

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

---

## 4. Nested Models

Run:

```bash
python nested_models.py
```

Demonstrates:

- Nested schemas
- Relationships between models
- Complex structured data

Example:

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    address: Address
```

---

## Running All Examples

Run each file individually:

```bash
python learn_pydantic.py
python computed_field.py
python model_validator.py
python nested_models.py
```

---

## Learning Goals

This project helps you understand:

- Data validation
- Type-safe models
- Custom validation logic
- Derived fields
- Nested object structures

---

## Future Improvements

Possible additions:

- Field serializers
- `field_validator`
- Settings management
- API schema examples
- FastAPI integration
- Advanced Pydantic patterns

---

## Resources

- Pydantic Documentation: https://docs.pydantic.dev/
- Python Documentation: https://docs.python.org/

---

## License

abhijit pise (Abhi-ai2975) MIT License 
