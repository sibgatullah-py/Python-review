family = {
    'child1': {
        'name': 'mofiz',
        'age' : 12,
    },
    'child2' : {
        'name':'mokles',
        'age' :20,
    },
    'child3' : {
        'name':'kuddus',
        'age' :21,
    }
    
}
print(family['child1']['name'])

# Loop through the nested dictionary
for x,obj in family.items():
    for y in obj:
        print(y + ' ' , obj[y])