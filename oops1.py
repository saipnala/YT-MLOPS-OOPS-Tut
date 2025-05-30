class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

sam = employee()
#print(sam.id)
#sam.travel("Kerala")
print(type(sam))