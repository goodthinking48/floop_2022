class MyClass():

    def instance_method(self):
        print(self)

    @staticmethod
    def static_method():
        print("nothing")

    @classmethod
    def class_method(cls):
        print(cls)

my_object = MyClass()
my_object.instance_method()
MyClass.static_method()
MyClass.class_method()
