import random
animal_list = ["dog","cat","bee","a"]
colour_list = ["red","green","blue"]
even_list = [2,4,6,8,10]
print (animal_list[random.randint(0, 3)])
print (colour_list[random.randint(0, 2)])
print (even_list[random.randint(0, 4)])

print (animal_list[int(random.random()*4)])
print (colour_list[int(random.random()*3)])
print (even_list[int(random.random()*5)])

print (animal_list[random.randrange(0, 4,1)])
print (colour_list[random.randrange(0, 3,1)])
print (even_list[random.randrange(0, 5,1)])

input_value = int(input("Please input a value: "))
if(input_value < 60):
    print ("small")
elif ((input_value >= 60) and (input_value < 100)):
    print ("medium")
else:
    print ("large")