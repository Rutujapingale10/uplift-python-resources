# 2nd Step
def myDecorator(function):
    # 3rd Step
    def innerFunction1():
        # 4th Step
        print("Hello this is before we called the function argument")
        # 5th Step
        function()
        # 7th Step
        print("Hello this is after we called the function argument")
    # 8th Step
    return innerFunction1

# 6th Step


def theFunctionWeWillBePassing():
    print("Hey, I am inside the function")


# 1st Step
x = myDecorator(theFunctionWeWillBePassing)
# 9th / Final Step
x()
