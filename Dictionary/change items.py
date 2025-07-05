car = {
    'brand' : 'toyota',
    'model' : 'civik',
    'year'  : 2018,
}
car['year'] = 2020
print(car['year'])
# using update() method to update the whole dictionary 
car.update({'brand':'BMW','model': 'mussle','year':2010})# update() can be used to add new items in dictionary
print(car.items())