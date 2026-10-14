from class1 import Restaurant
from class1 import IceCreamStand
from class1 import userestaurant

r1 = Restaurant("ccc","baozi")
r2 = Restaurant("ddd","hundun")
r3 = Restaurant("eee","xianbing")

userestaurant(r1)
userestaurant(r2)
userestaurant(r3)

r1.restaurant()
r1.set_number_served(5)
r1.increment_number_served(2)

r4 = IceCreamStand("fff","chocolate_icecream","strawberry_icecream","banana_icecream")
userestaurant(r4)
r4.get_flavors()