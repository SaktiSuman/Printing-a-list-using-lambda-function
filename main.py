lis = [
    { "name" : "Nandini", "age" : 20},
    { "name" : "Manjeet", "age" : 20 },
    { "name" : "Nikhil" , "age" : 19 }
]
print("Printing the list using lambda function")
print(sorted(lis, key = lambda i : i["age"]))