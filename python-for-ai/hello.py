"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dg1=Dog("Buddy", "Golden Retriever")
dg2=Dog("Max", "German Shepherd")
dg3=Dog("Bella", "Labrador Retriever")

print("DOG NAME 1:", dg1.name,dg1.breed)
print("DOG NAME 2:", dg2.name,dg2.breed)
print("DOG NAME 3:", dg3.name,dg3.breed)
------------------------------------------------------------------

class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client

# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://avlsoft.netlify.app")
client2 = APIClient(api_key="key2", base_url="https://api2.com")

print("Client 1 API Key:", client1.api_key)
print("Client 1 Base URL:", client1.base_url)

-----------------------------------------------------------------------

class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

---------------------------------------------------------

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def bark(self):
        print(f"{self.name} is barking.")


dg1=Dog("Buddy")
dg1.eat()
dg1.sleep()
dg1.bark()

"""

