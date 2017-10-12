
# Create a dictionary
# literal
people = [
    {
    "name": "Richard",
    "age": 43,
    "favourite colour": ["Blue", "Green"] 
    },
    {
    "name": "Tom",
    "age": 33,
    "favourite colour": []
    },
    {
    "name": "Harry",
    "age": 23,
    "favourite colour": ["Green", "White", "Purple"] 
    }
]

print(people[-1]["favourite colour"][1])



# Dictionary comprehension
print("Dictionary of words and their lengths")
message = "Hello there everyone, my name is python"
words = message.split(" ")
print({ w: len(w) for w in words})


#Dictionary comprehension with if
print("Dictionary of words containing 3 and their lengths")
message = "Hello there everyone my name is python"
words = message.split(" ")
print({ w: len(w) for w in words if "e" in w })


# Zip
# Combine countries and cities to create a dictionary
countries = ["France", "Germany", "Ireland", "England", "USA"]
cities = ["Paris", "Berlin", "Dublin", "London", "Washington DC"]
capitals = zip(countries, cities)
capital_of = dict(capitals)

print(capital_of['Ireland'])
