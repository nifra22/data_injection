class Laptop:
    price = 0
    processor = ""
    ram = ""
hp = Laptop()
hp.price = 50000
hp.processor = "i5"
hp.ram = "256GB"

dell = Laptop()
dell.price = 200000
dell.processor = "i5"
dell.ram = "256GB"

lenovo = Laptop()
lenovo.price = 5410000
lenovo.processor = "i5"
lenovo.ram = "256GB"

print(hp.price)
print(hp.ram,dell.price)
