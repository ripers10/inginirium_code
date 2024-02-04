class Human:
    age = 10
    height = 150
    weight = 50


    def say_hello(self):
        print('Hello!')
        print('I am a human.')

    def say_good_bye(self):
        print('See you!')

John = Human()
Frank = Human()
print(John.age)
John.say_hello()
print(Frank.height)
Frank.say_good_bye()