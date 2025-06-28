
'''
To simulate method overloading, we use default arguments or *args:

✅ Here, the same method show() behaves differently based on the number of arguments passed.


'''

class Example:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a)
        else:
            print("No arguments passed")

# Usage
obj = Example()
obj.show(10)        # Output: 10
obj.show(10, 20)    # Output: 10 20
obj.show()          # Output: No arguments passed
