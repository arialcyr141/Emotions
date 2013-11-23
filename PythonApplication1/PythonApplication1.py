from module1 import main1

class class1:
    value = 0
    def __init__(self):
        self.value = 4

def main():
    print('Hello World')
    fauna = {}
    fauna["fruits"] = ["apple", "grape"]
    fauna["vegetables"] = ["cucumber", "tomato"]
    fruits = fauna["fruits"]
    for fruit in fruits:
      print(fruit)

    c = class1()
    print(c.value)
    s = input('>')
    s1 = s
    if s == "hi":
        s1 = 44
     



if __name__ == "__main__":
    main1()

