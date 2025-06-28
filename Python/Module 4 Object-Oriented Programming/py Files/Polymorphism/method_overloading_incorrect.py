
class Example:
    def show(self, a):
        print(a)

    def show(self, a, b):  # Overwrites the previous method
        print(a, b)



obj = Example()
obj.show(10)  # ❌ ERROR: TypeError (because show() expects 2 arguments)
obj.show(10, 20)  # ✅ Works
