cars = 100  #汽车数
space_in_a_car = 4.0 #每辆车可乘坐的人数,我觉得用4更好，总不能把人掰开吧
drivers = 30  #司机数
passengers = 90  # 乘客
cars_not_driver = cars - drivers  #没有司机的车辆数
cars_driver = drivers
carpool_capacity =cars_driver * space_in_a_car
average_passengers_per_car = passengers / cars_driver


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driver,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("But we have only",passengers,"to carpool today.")  #改了下，和课本中的不一样，英文不好，见谅
print("We need to put about",average_passengers_per_car,"in each car.")
