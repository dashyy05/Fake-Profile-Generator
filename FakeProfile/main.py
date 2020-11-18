from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

def printInfos():
    #variables
    name = fake.name()
    country = fake.country()
    email = fake.email()
    address = fake.address()
    job = fake.job()
    car_brand = fake.vehicle_make()
    car_year = fake.machine_year()

    #infos
    print("Name:",name)
    print("Country:",country)
    print("Address:",address)
    print("Car brand:",car_brand)
    print("Year of the car:",car_year)
    print("Email:",email)
    print("Job:",job)
printInfos()