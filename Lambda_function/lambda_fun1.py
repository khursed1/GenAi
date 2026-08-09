square = lambda x: x * x
print(square(5))

# lambda input:output

# multiple inputs

add = lambda a, b: a + b
print(add(1, 2))

# lambda with dictionary
# suppose
data = {
    "name": "khursed",
    "age": 23,
}

# lambda x:x['key']
# you can write
get_data = lambda x: (x["name"], x["age"])
print(get_data(data))
