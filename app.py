# app.py

from customers import Customer
from restaurants import Restaurant

customer1 = Customer("Abdirahman", "Diis") 
restaurant1 = Restaurant("The Cafe Java")

print(customer1.full_name())
print(restaurant1.name)