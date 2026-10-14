class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a restaurant")
        print(f"{self.cuisine_type.title()} is a cuisine")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening now")
    def restaurant(self):
        print(f"{self.number_served} person eat in {self.restaurant_name.title()}")
    def set_number_served(self,number_served):
        self.number_served = number_served
        Restaurant.restaurant(self)
    def increment_number_served(self,number_served):
        self.number_served += number_served
        Restaurant.restaurant(self)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,*flavors,number_served=0):
        super().__init__(restaurant_name,"ice cream",number_served)
        self.flavors = flavors
    def get_flavors(self):
        print("Here are all icecream flavors")
        for flavor in self.flavors:
            print(flavor)

def userestaurant(name1):
    name1.describe_restaurant()
    name1.open_restaurant()
