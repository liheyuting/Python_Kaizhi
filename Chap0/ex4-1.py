#定义 cars = 100
cars = 100
#定义space_in_a_car =4.0
space_in_a_car =4.0
#定义drivers = 30 
drivers = 30 
#定义passengers = 90
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven *space_in_a_car
average_passenger_per_car = passengers / cars_driven
#car_pool_capacity 没有定义 

print "There are", cars, "cars available."
print "There are only", drivers, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passenger_per_car, "in each car."

x=2
y=4
z=x+y
print z