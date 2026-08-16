class Vehicle_Name:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Name of the vehicle is {self.name}")
class Vehicle_Type:
    def __init__(self,wheeler):
        self.wheeler=wheeler
    def show(self):
            print(f"Type of the vehicle is {self.wheeler}")
class Vehicle(Vehicle_Type,Vehicle_Name):
    def __init__(self, name,wheeler):
         self.name=name
         self.wheeler=wheeler


a=Vehicle("Thar","Fourwheeler")
print(a.name)
a.show()