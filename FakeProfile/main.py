from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

def mainThing():
    #variables
    firstName = fake.first_name()
    lastName = fake.last_name()
    country = fake.country()
    city = fake.city()
    email = fake.email()
    address = fake.address()
    job = fake.job()
    phoneNumber = fake.phone_number()
    car_brand = fake.vehicle_make()
    car_year = fake.machine_year()
    fav_color = fake.color_name()

    def printInfos():
        print("Name:",firstName,lastName)
        print("Country:",country)
        print("City:",city)
        print("Address:",address)
        print("Car brand:",car_brand)
        print("Year of the car:",car_year)
        print("Email:",email)
        print("Job:",job)
        print("Phone number:",phoneNumber)
        print("Fav color:",fav_color)
    printInfos()


mainThing()