Data1 = (7, False, "Apple", True, 7, 98.6)

one = len(Data1)
seven = Data1.count(7)


print(one)
print(Data1[3])
print(seven)

Data2 = { "July", 4, 8, "Tango", 4.3, "Bingo"}

Data2.pop()
Data2.add("Alpha")

print(Data2)

Data3 = [ "A", 7, -1, 3.14, True, 7 ]


Data3.reverse()
Data3[1] = "B" 
Data3.pop(len(Data3)-1)

print(Data3)

Data4 = {"name" : "Joe", 
         "age" : 26, 
         "active" : True,  
         "hourly_wage" : 14.75}

Data4.update({"active" : False  })
address = Data4.setdefault("address", "123 West Main Street")
hpay = Data4.get("hourly_wage")
weeklySal = 40 * hpay

print(Data4)
print(address)
print(weeklySal)