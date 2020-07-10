import abc
class MyABC(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition"""

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""

class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value):
        self._myprop = value
    
    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop

if __name__ == '__main__':
    c1 = MyClass(5) #Object of child class
    c1.do_something(5)
    print('This actual class object behaves as expected')
    print(c1.some_property)
    print('The following attempt to create object of abstract class \
            errors the program out')
    c2 = MyABC() #Object of Abstract class
    c2.do_something()