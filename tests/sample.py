import xml.etree.ElementTree as ET
import xmltodict

myTree = ET.parse('/home/excellence/PycharmProjects/gitAutomation/ZipCodes.xml')
myRoot = myTree.getroot()
for x in range(2):
    y = myRoot[x].find('item').get('name')
    # z = myRoot[x].find('description').text
    # v = myRoot[x].find('li').text
    # print(y, z)

food = ['grocery', 'food', 'Roti Kit', 'Catering', 'Organic Grocery', 'Meal Basket', 'Tiffin Services', 'Meal Kit', 'Instant Pot Kits', 'Recipes']
# print(food[1])

# if food[1] == myRoot[1].find('food'):
#     print('true')
# else:
#     print('false')

xml_data = """
    <department>
        <item name="60070"> Departments: </item>
            <description1>grocery</description1>
            <description2>food</description2>
            <description3>Roti kit</description3>
            <description4>Catering</description4>
            <description5>Organic Grocery</description5>
            <description6>Meal Basket</description6>
            <description7>Tiffin Services</description7>
           <description8> Meal Kit</description8>
            <description9>Instant Pot Kit</description9>
            <description10>Recipes
        </description10>

    </department>
"""
my_dict = xmltodict.parse(xml_data)
print("The type is: ", type(my_dict))

print(my_dict['department']['description1'])

if my_dict['department']['description2'] == food[1]:
    print('true')
else:
    print('false')

d = {'C  14': ['15263808', '13210478'], 'W   1': ['13122205']}
d = {k.translate({32: None}): v for k, v in d.items()}
print(d)

