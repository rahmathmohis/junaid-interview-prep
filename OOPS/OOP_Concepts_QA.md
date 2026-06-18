# OOP Concepts Interview Q&A - Python

## Interview Preparation Guide for Campus Placement
**Dayanand Sagar Engineering - 4th Year**

---

## 📑 Table of Contents

**Legend:** 🟢 Easy | 🟡 Medium | 🔴 Hard | ⏱️ Estimated Time

### BASIC LEVEL (Q1-Q7) ⏱️ 30-40 min
1. [🟢 What are the Four Pillars of OOP?](#q1-what-are-the-four-pillars-of-oop-explain-briefly) ⏱️ 5 min
2. [🟢 Classes and Objects - Relationship](#q2-what-are-classes-and-objects-in-python-explain-their-relationship) ⏱️ 4 min
3. [🟢 What is Abstraction in OOP?](#q3-what-is-abstraction-in-oop) ⏱️ 5 min
4. [🟢 What is Encapsulation?](#q4-what-is-encapsulation-how-does-python-implement-it) ⏱️ 5 min
5. [🟢 Explain Inheritance and its types](#q5-explain-inheritance-and-its-types-in-python) ⏱️ 5 min
6. [🟢 Different types of Inheritance](#q6-what-are-the-different-types-of-inheritance-explain-with-examples) ⏱️ 6 min
7. [🟢 Abstraction vs Encapsulation](#q7-what-is-the-difference-between-abstraction-and-encapsulation) ⏱️ 4 min

### INTERMEDIATE LEVEL (Q8-Q20) ⏱️ 60-75 min
8. [🟡 Types of Polymorphism](#q8-what-are-the-types-of-polymorphism-in-oop) ⏱️ 5 min
9. [🟡 Magic Methods (Dunder Methods)](#q9-what-are-magic-methods-dunder-methods-in-python-give-examples) ⏱️ 5 min
10. [🟡 `__init__` vs `__new__`](#q10-what-is-the-__init__-method-how-is-it-different-from-__new__) ⏱️ 5 min
11. [🟡 Class vs Instance Variables](#q11-whats-the-difference-between-class-variables-and-instance-variables) ⏱️ 4 min
12. [🟡 @staticmethod, @classmethod, instance methods](#q12-what-are-staticmethod-classmethod-and-instance-methods) ⏱️ 5 min
13. [🟡 Method Overriding](#q13-explain-method-overriding-with-an-example) ⏱️ 4 min
14. [🟡 The super() function](#q14-what-is-the-super-function-and-when-do-you-use-it) ⏱️ 5 min
15. [🟡 Duck Typing in Python](#q15-what-is-duck-typing-in-python) ⏱️ 4 min
16. [🟡 Access Modifiers (public, protected, private)](#q16-what-are-access-modifiers-in-python-explain-public-protected-and-private) ⏱️ 5 min
17. [🟡 Name Mangling](#q17-what-is-name-mangling-in-python) ⏱️ 4 min
18. [🟡 is-a vs has-a relationships](#q18-what-is-the-difference-between-is-a-and-has-a-relationships) ⏱️ 5 min
19. [🟡 Operator Overloading](#q19-what-is-operator-overloading-give-examples) ⏱️ 5 min
20. [🟡 `__str__` vs `__repr__`](#q20-what-is-the-difference-between-__str__-and-__repr__) ⏱️ 4 min

### ADVANCED LEVEL (Q21-Q30) ⏱️ 60-70 min
21. [🔴 Method Resolution Order (MRO) & Diamond Problem](#q21-what-is-method-resolution-order-mro-and-the-diamond-problem) ⏱️ 6 min
22. [🔴 Composition over Inheritance](#q22-when-should-you-use-composition-over-inheritance) ⏱️ 5 min
23. [🔴 @property decorator](#q23-what-is-the-property-decorator-and-why-use-it) ⏱️ 6 min
24. [🔴 Getters and Setters](#q24-what-are-getters-and-setters-why-use-them) ⏱️ 5 min
25. [🔴 Abstract Class vs Interface](#q25-what-is-an-abstract-class-how-is-it-different-from-an-interface) ⏱️ 6 min
26. [🔴 Singleton Pattern](#q26-what-is-the-singleton-pattern-implement-it-in-python) ⏱️ 6 min
27. [🔴 Shallow Copy vs Deep Copy](#q27-what-is-the-difference-between-shallow-copy-and-deep-copy) ⏱️ 6 min
28. [🔴 Aggregation vs Composition](#q28-what-is-aggregation-how-is-it-different-from-composition) ⏱️ 6 min
29. [🔴 Multiple Inheritance Pros & Cons](#q29-what-is-multiple-inheritance-what-are-its-advantages-and-disadvantages) ⏱️ 6 min
30. [🔴 Design Patterns in OOP](#q30-what-are-some-common-design-patterns-in-oop) ⏱️ 7 min

### 📚 Quick Reference Sections
- [Key Comparison Tables](#-key-comparison-tables)
- [Top 10 Most Asked Questions](#-top-10-most-asked-questions)
- [Quick Reference Cheat Sheet](#-quick-reference-cheat-sheet)

[⬆️ Back to Top](#-table-of-contents)

---

## BASIC LEVEL QUESTIONS

### Q1. What are the Four Pillars of OOP? Explain briefly. 🟢

**Definition:**
The four pillars of Object-Oriented Programming are Encapsulation, Inheritance, Polymorphism, and Abstraction. These fundamental concepts form the foundation of OOP and enable us to write modular, reusable, and maintainable code. Together, they help in modeling real-world problems effectively.

**Why it matters:**
Understanding these pillars is essential for any OOP interview. They provide the conceptual framework for designing robust software systems and are universally applied across all OOP languages.

**Code Example:**
```python
# Brief demonstration of all four pillars
from abc import ABC, abstractmethod

# 1. Encapsulation - data hiding
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def get_balance(self):
        return self.__balance

# 2. Inheritance - code reuse
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

# 3. Polymorphism - same interface, different behavior
class Dog:
    def sound(self): return "Bark"

class Cat:
    def sound(self): return "Meow"

# 4. Abstraction - hiding complexity
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

**Key Takeaway:**
Encapsulation protects data, Inheritance reuses code, Polymorphism provides flexibility, Abstraction hides complexity.
**Benefits of OOP:**
- **Modularity**: Objects are standalone entities communicating through public interfaces, promoting code separation and easier maintenance
- **Reusability**: Class hierarchies and objects can be reused across projects; inheritance allows acquiring attributes from parent classes
- **Extensibility**: New features can be added through inheritance and interfaces without modifying existing code
- **Flexibility**: Polymorphism enables objects to adapt behavior based on context with the same interface


---

### Q2. What are Classes and Objects in Python? Explain their relationship. 🟢

**Definition:**
A class is a blueprint or template that defines the structure and behavior of objects. An object is an instance of a class - a concrete realization with actual values. Think of a class as a cookie cutter and objects as the cookies made from it.

**Why it matters:**
Classes allow us to model real-world entities and create reusable code. Instead of writing repetitive code, we define once and create multiple instances.

**Code Example:**
```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display(self):
        print(f"Student: {self.name}, Roll: {self.roll_no}")

# Creating objects
student1 = Student("Amit", 101)
student2 = Student("Priya", 102)
student1.display()  # Output: Student: Amit, Roll: 101
```

**Key Takeaway:**
Class is the design; object is the actual entity created from that design.

---

### Q3. What is Abstraction in OOP?

**Definition:**
Abstraction is the process of hiding complex implementation details and showing only the essential features to the user. It focuses on what an object does rather than how it does it. In Python, abstraction is achieved using abstract classes and interfaces through the ABC (Abstract Base Class) module.

**Why it matters:**
Abstraction reduces complexity by allowing users to work with simplified interfaces. It helps in managing large codebases by hiding unnecessary details and focusing on high-level functionality.

**Code Example:**
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")
    
    def execute_query(self, query):
        print(f"Executing MySQL query: {query}")

class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")
    
    def execute_query(self, query):
        print(f"Executing MongoDB query: {query}")

# db = Database()  # Error: Can't instantiate abstract class
db = MySQL()
db.connect()  # User doesn't need to know connection details
```

**Key Takeaway:**
Abstraction defines "what to do" through abstract methods; concrete classes define "how to do it."

---

### Q4. What is Encapsulation? How does Python implement it?

**Definition:**
Encapsulation is the concept of bundling data (attributes) and methods that operate on that data within a single unit (class), and restricting direct access to some components. It's about data hiding and providing controlled access through methods.

**Why it matters:**
Encapsulation protects data from accidental modification and makes code more maintainable. We can change internal implementation without affecting external code.

**Code Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # AttributeError - cannot access directly
```

**Key Takeaway:**
Use double underscore (`__`) for private members and provide public methods for controlled access.

---

### Q5. Explain Inheritance and its types in Python.

**Definition:**
Inheritance allows a class (child/derived) to inherit properties and methods from another class (parent/base). It promotes code reusability and establishes a relationship between classes. Python supports single, multiple, and multilevel inheritance.

**Why it matters:**
Instead of duplicating code, we can extend existing classes and add specialized functionality, following the DRY (Don't Repeat Yourself) principle.

**Code Example:**
```python
# Single Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        print(f"Driving {self.brand} {self.model}")

my_car = Car("Toyota", "Camry")
my_car.start()   # Inherited method
my_car.drive()   # Own method
```

**Key Takeaway:**
Child class inherits all accessible members from parent and can override or extend functionality.

---

### Q6. What are the different types of Inheritance? Explain with examples.

**Definition:**
Python supports five types of inheritance: Single (one parent, one child), Multiple (multiple parents, one child), Multilevel (chain of inheritance), Hierarchical (one parent, multiple children), and Hybrid (combination of two or more types). Each serves different design needs.

**Why it matters:**
Choosing the right inheritance type affects code organization, maintainability, and complexity. Understanding types helps in designing class hierarchies effectively.

**Code Example:**
```python
# 1. Single Inheritance
class Animal:
    def eat(self): print("Eating")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self): print("Barking")

# 2. Multiple Inheritance
class Father:
    def skills(self): print("Programming")

class Mother:
    def skills(self): print("Dancing")

class Child(Father, Mother):  # Inherits from both
    pass

# 3. Multilevel Inheritance
class GrandParent:
    def show(self): print("GrandParent")

class Parent(GrandParent):  # Parent inherits GrandParent
    pass

class Child(Parent):  # Child inherits Parent (chain)
    pass

# 4. Hierarchical Inheritance
class Vehicle:
    def type(self): print("Vehicle")

class Car(Vehicle):  # Multiple children
    pass

class Bike(Vehicle):  # from same parent
    pass
```

**Key Takeaway:**
Single for simple extension, Multiple for combining features, Multilevel for layered hierarchy, Hierarchical for shared base.

---

### Q7. What is the difference between Abstraction and Encapsulation? 🟢

**Definition:**
Abstraction is hiding complex implementation details and showing only essential features to the user. Encapsulation is hiding data and providing methods to access it. Abstraction focuses on "what" an object does; encapsulation focuses on "how" it's protected.

**Why it matters:**
Abstraction reduces complexity by hiding unnecessary details. Users interact with simple interfaces without needing to understand internal workings.

**Code Example:**
```python
from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract class
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Processing ${amount} via UPI")

# payment = Payment()  # Error: Can't instantiate abstract class
cc = CreditCard()
cc.process_payment(100)  # User doesn't know internal implementation
```

**Key Takeaway:**
Abstraction hides complexity; encapsulation hides data. Both promote security and modularity.

---

## INTERMEDIATE LEVEL QUESTIONS

### Q8. What are the types of Polymorphism in OOP? 🟡

**Definition:**
Polymorphism has two main types: Compile-time Polymorphism (Method Overloading - same method name, different parameters) and Runtime Polymorphism (Method Overriding - child class redefines parent method). Python primarily supports runtime polymorphism, while compile-time is achieved through default arguments or *args.

**Why it matters:**
Understanding polymorphism types helps in designing flexible APIs and choosing the right approach for different scenarios.

**Code Example:**
```python
# Runtime Polymorphism (Method Overriding)
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):  # Override
        print("Bark")

class Cat(Animal):
    def sound(self):  # Override
        print("Meow")

# Compile-time Polymorphism (Method Overloading via default args)
class Calculator:
    def add(self, a, b=0, c=0):  # Same method, variable params
        return a + b + c

calc = Calculator()
print(calc.add(5))        # 5
print(calc.add(5, 3))     # 8
print(calc.add(5, 3, 2))  # 10

# Duck typing (Python's polymorphism)
def make_sound(animal):
    animal.sound()  # Works with any object having sound()

make_sound(Dog())  # Bark
make_sound(Cat())  # Meow
```

**Key Takeaway:**
Runtime polymorphism uses method overriding; Python achieves compile-time polymorphism through default arguments and duck typing.

---

### Q9. What are Magic Methods (Dunder Methods) in Python? Give examples.

**Definition:**
Magic methods, also called dunder methods (double underscore), are special methods with names surrounded by double underscores like `__init__`, `__str__`. They enable operator overloading and define how objects behave with built-in operations.

**Why it matters:**
They make custom classes behave like built-in types, enabling intuitive syntax like `obj1 + obj2` or `len(obj)`.

**Code Example:**
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"Book: {self.title}"
    
    def __len__(self):
        return self.pages
    
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 400)
print(book1)           # Output: Book: Python Basics
print(len(book1))      # Output: 300
print(book1 + book2)   # Output: 700
```

**Key Takeaway:**
Magic methods let you customize how your objects work with Python's built-in operations and functions.

---

### Q10. What is the __init__ method? How is it different from __new__?

**Definition:**
`__init__` is an initializer method that sets up the object's initial state after it's created. `__new__` is a constructor method that actually creates and returns the instance before `__init__` is called. `__new__` is a static method that receives the class as first argument, while `__init__` receives the instance (`self`).

**Why it matters:**
Understanding this distinction is important for advanced scenarios like implementing singletons, customizing immutable object creation, or metaclass programming.

**Code Example:**
```python
class Person:
    def __new__(cls, name):
        print(f"Creating instance with __new__")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print(f"Initializing instance with __init__")
        self.name = name

# Output when creating object:
p = Person("Alice")
# Creating instance with __new__
# Initializing instance with __init__

# Singleton pattern using __new__
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - same instance
```

**Key Takeaway:**
`__new__` creates the object; `__init__` initializes it. `__new__` runs first and must return an instance.

---

### Q11. What's the difference between Class Variables and Instance Variables?

**Definition:**
Class variables are shared among all instances of a class and defined at the class level. Instance variables are unique to each object and defined in the `__init__` method using `self`. Modifying a class variable affects all instances unless overridden.

**Why it matters:**
Understanding this prevents bugs where you accidentally share data across instances or fail to share data that should be common.

**Code Example:**
```python
class Employee:
    company = "TechCorp"  # Class variable
    
    def __init__(self, name, salary):
        self.name = name      # Instance variable
        self.salary = salary  # Instance variable

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.company)  # TechCorp
print(emp2.company)  # TechCorp

Employee.company = "NewTech"  # Changes for all instances
print(emp1.company)  # NewTech
print(emp2.company)  # NewTech

print(emp1.name)     # Alice (unique to emp1)
print(emp2.name)     # Bob (unique to emp2)
```

**Key Takeaway:**
Class variables are shared; instance variables are unique to each object.

---

### Q12. What are @staticmethod, @classmethod, and instance methods?

**Definition:**
Instance methods take `self` as first parameter and can access/modify object state. Class methods take `cls` as first parameter and can access/modify class state. Static methods take neither and are just utility functions that belong to the class namespace.

**Why it matters:**
Choosing the right method type makes code clearer and more maintainable, showing intent about what data the method needs.

**Code Example:**
```python
class MathOperations:
    pi = 3.14159
    
    def __init__(self, number):
        self.number = number
    
    def square(self):  # Instance method
        return self.number ** 2
    
    @classmethod
    def get_pi(cls):  # Class method
        return cls.pi
    
    @staticmethod
    def add(x, y):  # Static method
        return x + y

obj = MathOperations(5)
print(obj.square())              # 25 (uses instance data)
print(MathOperations.get_pi())   # 3.14159 (uses class data)
print(MathOperations.add(3, 4))  # 7 (no instance/class data)
```

**Key Takeaway:**
Use instance methods for object-specific operations, class methods for class-level operations, and static methods for utilities.

---

### Q13. Explain Method Overriding with an example.

**Definition:**
Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. The child's version replaces the parent's version for objects of the child class.

**Why it matters:**
Overriding allows customizing inherited behavior while maintaining the same interface, essential for polymorphism.

**Code Example:**
```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Overriding parent method
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Overriding parent method
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 3)
circle = Circle(7)
print(rect.area())    # 15
print(circle.area())  # 153.86
```

**Key Takeaway:**
Child class can override parent methods to provide specialized implementation while keeping the same method signature.

---

### Q14. What is the super() function and when do you use it? 🟡

**Definition:**
The `super()` function returns a proxy object that allows you to call methods of the parent class. It's commonly used in `__init__` to call the parent's constructor and in method overriding to extend rather than completely replace parent functionality. It handles multiple inheritance correctly using MRO.

**Why it matters:**
Using `super()` ensures proper initialization of parent classes and maintains the inheritance chain, especially crucial in multiple inheritance scenarios.

**Code Example:**
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle init: {brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
        print(f"Car init: {model}")
    
    def display(self):
        super().display() if hasattr(Vehicle, 'display') else None
        print(f"Car: {self.brand} {self.model}")

# Multiple inheritance example
class Electric:
    def charge(self):
        print("Charging battery")

class Hybrid(Car, Electric):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Follows MRO
        self.battery = battery

car = Hybrid("Toyota", "Prius", "50kWh")
# Output: Vehicle init: Toyota
#         Car init: Prius
```

**Key Takeaway:**
`super()` enables proper parent method calling and is essential for cooperative multiple inheritance.

---

### Q15. What is Duck Typing in Python?

**Definition:**
Duck typing is a programming concept where the type or class of an object is less important than the methods it defines. If an object walks like a duck and quacks like a duck, it's treated as a duck. Python checks what an object can do (methods/attributes) rather than what it is (type).

**Why it matters:**
Duck typing makes Python flexible and enables polymorphism without explicit inheritance or interfaces, leading to more concise code.

**Code Example:**
```python
class Duck:
    def swim(self):
        print("Duck swimming")
    
    def fly(self):
        print("Duck flying")

class Airplane:
    def swim(self):
        print("Airplane on water")
    
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def make_it_fly(entity):
    entity.fly()  # Don't care about type, just that it has fly()

make_it_fly(Duck())      # Works
make_it_fly(Airplane())  # Works
# make_it_fly(Whale())   # AttributeError - no fly() method
```

**Key Takeaway:**
"If it looks like a duck and quacks like a duck, it must be a duck" - Python cares about capability, not type.

---

### Q16. What are Access Modifiers in Python? Explain public, protected, and private.

**Definition:**
Access modifiers control the accessibility of class members. Python uses naming conventions: public (no underscore), protected (single underscore `_`), and private (double underscore `__`). Unlike Java/C++, Python doesn't enforce strict access control but relies on conventions and name mangling for private members.

**Why it matters:**
Access modifiers help implement encapsulation and signal intended usage to other developers, preventing accidental modification of internal implementation.

**Code Example:**
```python
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no       # Public
        self._interest_rate = 0.03         # Protected (convention)
        self.__balance = balance           # Private (name mangled)
    
    def get_balance(self):
        return self.__balance
    
    def _calculate_interest(self):         # Protected method
        return self.__balance * self._interest_rate

account = BankAccount("ACC001", 10000)
print(account.account_no)           # 10000 - accessible
print(account._interest_rate)       # 0.03 - accessible but shouldn't use
# print(account.__balance)          # AttributeError
print(account.get_balance())        # 10000 - proper access
print(account._BankAccount__balance)  # 10000 - name mangling workaround
```

**Key Takeaway:**
Public: no underscore; Protected: single `_`; Private: double `__` (name mangled to `_ClassName__attribute`).

---

### Q17. What is Name Mangling in Python?

**Definition:**
Name mangling is Python's mechanism to make class members private by internally renaming them. When you use double underscore `__` prefix, Python transforms the name to `_ClassName__attribute` to avoid naming conflicts in inheritance and provide pseudo-private access.

**Why it matters:**
Name mangling prevents accidental overriding in subclasses and signals that an attribute is internal implementation detail, though it's not truly private.

**Code Example:**
```python
class Parent:
    def __init__(self):
        self.__private = "Parent's private"
    
    def show(self):
        print(self.__private)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = "Child's private"  # Doesn't override parent's
    
    def show_both(self):
        self.show()  # Parent's private
        print(self.__private)  # Child's private

c = Child()
c.show_both()
# Output:
# Parent's private
# Child's private

# Accessing mangled names
print(c._Parent__private)  # Parent's private
print(c._Child__private)   # Child's private
```

**Key Takeaway:**
Name mangling transforms `__attr` to `_ClassName__attr` to prevent conflicts, but it's still accessible if you know the mangled name.

---

### Q18. What is the difference between is-a and has-a relationships?

**Definition:**
"Is-a" relationship represents inheritance where a subclass is a type of the parent class (e.g., Dog is an Animal). "Has-a" relationship represents composition where a class contains instances of other classes (e.g., Car has an Engine). Is-a uses inheritance; has-a uses composition.

**Why it matters:**
Choosing the right relationship affects code design, flexibility, and maintainability. Misusing inheritance leads to tight coupling and rigid hierarchies.

**Code Example:**
```python
# Is-a relationship (Inheritance)
class Animal:
    def breathe(self):
        print("Breathing")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Barking")

dog = Dog()
dog.breathe()  # Inherited from Animal

# Has-a relationship (Composition)
class Engine:
    def start(self):
        print("Engine started")

class Car:  # Car HAS-A Engine
    def __init__(self):
        self.engine = Engine()  # Composition
        self.wheels = 4
    
    def start(self):
        self.engine.start()
        print("Car moving")

car = Car()
car.start()
```

**Key Takeaway:**
Use "is-a" (inheritance) for type relationships; use "has-a" (composition) for part-whole relationships.

---

### Q19. What is Operator Overloading? Give examples.

**Definition:**
Operator overloading allows you to define custom behavior for operators (+, -, *, ==, etc.) when used with user-defined objects. This is achieved by implementing magic methods like `__add__`, `__sub__`, `__eq__`, etc.

**Why it matters:**
Operator overloading makes custom classes intuitive to use, allowing them to behave like built-in types with natural syntax.

**Code Example:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  # Overload + operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):  # Overload - operator
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):  # Overload * operator
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):  # Overload == operator
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2          # Uses __add__
print(v3)             # Vector(6, 8)
print(v1 == v2)       # False
print(v1 * 3)         # Vector(6, 9)
```

**Key Takeaway:**
Magic methods enable operator overloading: `__add__` for +, `__sub__` for -, `__mul__` for *, `__eq__` for ==, etc.

---

### Q20. What is the difference between __str__ and __repr__?

**Definition:**
`__str__` returns a user-friendly string representation for end-users (used by `str()` and `print()`). `__repr__` returns an unambiguous, developer-friendly representation for debugging (used by `repr()` and in interactive shell). `__repr__` should ideally be a valid Python expression to recreate the object.

**Why it matters:**
Good `__str__` and `__repr__` implementations make objects easier to debug and display, following Python's philosophy of readability.

**Code Example:**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        # User-friendly representation
        return f"{self.name} - ${self.price}"
    
    def __repr__(self):
        # Developer-friendly, recreatable representation
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 999)
print(str(p))    # Laptop - $999 (calls __str__)
print(repr(p))   # Product('Laptop', 999) (calls __repr__)
print(p)         # Laptop - $999 (print uses __str__)

# In interactive shell
>>> p
Product('Laptop', 999)  # Uses __repr__
```

**Key Takeaway:**
`__str__` for human-readable output; `__repr__` for unambiguous developer representation. If only one, define `__repr__`.

---

## ADVANCED LEVEL QUESTIONS

### Q21. What is Method Resolution Order (MRO) and the Diamond Problem? 🔴

**Definition:**
MRO is the order in which Python searches for methods in a hierarchy of classes, especially important in multiple inheritance. The diamond problem occurs when a class inherits from two classes that share a common parent, creating ambiguity about which parent's method to call.

**Why it matters:**
Understanding MRO prevents confusion in complex inheritance hierarchies and helps debug method lookup issues.

**Code Example:**
```python
class A:
    def show(self):
        print("A's method")

class B(A):
    def show(self):
        print("B's method")

class C(A):
    def show(self):
        print("C's method")

class D(B, C):  # Multiple inheritance
    pass

obj = D()
obj.show()  # Output: B's method
print(D.mro())  # [D, B, C, A, object]
# Python uses C3 linearization algorithm
```

**Key Takeaway:**
Python follows C3 linearization for MRO: left-to-right, depth-first, but ensuring each class appears before its parents.

---

### Q22. When should you use Composition over Inheritance?

**Definition:**
Composition is a "has-a" relationship where a class contains instances of other classes. Inheritance is an "is-a" relationship. The principle "favor composition over inheritance" suggests using composition when you need functionality from other classes without creating a tight parent-child bond.

**Why it matters:**
Composition provides more flexibility, reduces coupling, and avoids problems with deep inheritance hierarchies. It's easier to change and test.

**Code Example:**
```python
# Inheritance approach (tight coupling)
class Engine:
    def start(self):
        print("Engine started")

# Composition approach (loose coupling)
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        self.engine.start()
        print("Car is ready to drive")

car = Car()
car.start()
# Output:
# Engine started
# Car is ready to drive
```

**Key Takeaway:**
Use inheritance for "is-a" relationships and composition for "has-a" relationships; composition offers better flexibility.

---

### Q23. What is the @property decorator and why use it?

**Definition:**
The `@property` decorator allows you to define methods that can be accessed like attributes. It provides a pythonic way to implement getters, setters, and deleters, enabling computed attributes and validation while maintaining clean syntax.

**Why it matters:**
Properties provide encapsulation with clean syntax - you can add validation or computation logic later without changing how users access the attribute.

**Code Example:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)     # 25 (looks like attribute access)
print(temp.fahrenheit)  # 77.0 (computed property)
temp.celsius = 30       # 30 (setter with validation)
# temp.celsius = -300   # ValueError
```

**Key Takeaway:**
Properties let you add logic to attribute access without changing the interface - maintaining backward compatibility.

---

### Q24. What are Getters and Setters? Why use them?

**Definition:**
Getters and setters are methods used to access (get) and modify (set) private attributes of a class. They provide controlled access to class members, enabling validation, computation, or logging when attributes are accessed or modified. In Python, we use `@property` for getters and `@property_name.setter` for setters.

**Why it matters:**
Getters and setters maintain encapsulation, allow adding validation logic, and enable changing internal implementation without breaking external code.

**Code Example:**
```python
class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):  # Getter
        print("Getting age")
        return self._age
    
    @age.setter
    def age(self, value):  # Setter
        print("Setting age")
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value
    
    @age.deleter
    def age(self):  # Deleter
        print("Deleting age")
        del self._age

p = Person(25)
print(p.age)    # Getting age -> 25
p.age = 30      # Setting age
# p.age = -5    # ValueError: Invalid age
```

**Key Takeaway:**
Use `@property` for getters, `@property_name.setter` for setters - provides encapsulation with Pythonic syntax.

---

### Q25. What is an Abstract Class? How is it different from an Interface?

**Definition:**
An abstract class is a class that cannot be instantiated and contains one or more abstract methods (methods declared but not implemented). It serves as a blueprint for other classes. Interfaces (in Python, purely abstract classes) contain only abstract methods with no implementation. Abstract classes can have both abstract and concrete methods.

**Why it matters:**
Abstract classes enforce a contract for subclasses, ensuring they implement required methods. They enable designing common interfaces while allowing partial implementation.

**Code Example:**
```python
from abc import ABC, abstractmethod

# Abstract class with both abstract and concrete methods
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):  # Abstract method - must be implemented
        pass
    
    def sleep(self):  # Concrete method - optional to override
        print(f"{self.name} is sleeping")

# Interface (purely abstract)
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def land(self):
        pass

class Dog(Animal):
    def sound(self):  # Must implement
        return "Bark"

# animal = Animal("Generic")  # Error: Can't instantiate
dog = Dog("Buddy")
print(dog.sound())  # Bark
dog.sleep()         # Buddy is sleeping
```

**Key Takeaway:**
Abstract class: can have both abstract and concrete methods. Interface: only abstract methods (pure contract).

---

### Q26. What is the Singleton Pattern? Implement it in Python. 🔴

**Definition:**
Singleton is a design pattern that restricts a class to have only one instance throughout the application. All requests return the same instance. It's useful for resources like database connections, configuration managers, or logging where only one instance should exist.

**Why it matters:**
Singleton ensures controlled access to shared resources, prevents multiple instances that could cause conflicts, and provides a global access point.

**Code Example:**
```python
# Method 1: Using __new__
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

s1 = Singleton(10)
s2 = Singleton(20)
print(s1 is s2)      # True - same instance
print(s1.value)      # 20 - shared state
print(s2.value)      # 20

# Method 2: Using decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, host):
        self.host = host

db1 = DatabaseConnection("localhost")
db2 = DatabaseConnection("remote")
print(db1 is db2)  # True
```

**Key Takeaway:**
Singleton ensures one instance per class using `__new__` or decorator pattern - useful for shared resources.

---

### Q27. What is the difference between Shallow Copy and Deep Copy?

**Definition:**
Shallow copy creates a new object but inserts references to the objects found in the original (copies references). Deep copy creates a new object and recursively copies all objects found in the original (copies values). Shallow copy doesn't copy nested objects; deep copy does.

**Why it matters:**
Understanding copy types prevents bugs when working with mutable nested objects. Wrong choice can lead to unintended data sharing or modification.

**Code Example:**
```python
import copy

class Address:
    def __init__(self, city):
        self.city = city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

# Original
addr = Address("Mumbai")
p1 = Person("Amit", addr)

# Shallow copy
p2 = copy.copy(p1)
p2.name = "Priya"           # Different name
p2.address.city = "Delhi"   # CHANGES BOTH!

print(p1.name)         # Amit (different)
print(p1.address.city) # Delhi (shared!)
print(p2.address.city) # Delhi

# Deep copy
p3 = copy.deepcopy(p1)
p3.address.city = "Bangalore"

print(p1.address.city)  # Delhi (unchanged)
print(p3.address.city)  # Bangalore (independent)
```

**Key Takeaway:**
Shallow copy: copies object, shares nested objects. Deep copy: copies everything independently.

---

### Q28. What is Aggregation? How is it different from Composition?

**Definition:**
Both aggregation and composition represent "has-a" relationships. Composition is strong ownership - the child cannot exist without the parent (e.g., Room in House). Aggregation is weak ownership - the child can exist independently (e.g., Student in Department). When parent is destroyed, in composition child dies; in aggregation child survives.

**Why it matters:**
Choosing between aggregation and composition affects object lifecycle management and memory handling, impacting design decisions.

**Code Example:**
```python
# Composition - Engine cannot exist without Car
class Engine:
    def __init__(self, hp):
        self.horsepower = hp

class Car:
    def __init__(self, brand, hp):
        self.brand = brand
        self.engine = Engine(hp)  # Car creates and owns Engine
    
    def __del__(self):
        print(f"{self.brand} destroyed with its engine")

car = Car("Toyota", 150)
del car  # Engine is also destroyed

# Aggregation - Student can exist without Department
class Student:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

# Students exist independently
s1 = Student("Alice")
s2 = Student("Bob")

dept = Department("CS")
dept.add_student(s1)
dept.add_student(s2)

del dept  # Students still exist
print(s1.name)  # Alice - still accessible
```

**Key Takeaway:**
Composition: strong ownership, child dies with parent. Aggregation: weak ownership, child survives independently.

---

### Q29. What is Multiple Inheritance? What are its advantages and disadvantages?

**Definition:**
Multiple inheritance allows a class to inherit from more than one parent class, combining features from multiple sources. The child class has access to methods and attributes from all parent classes. Python supports multiple inheritance through the MRO (Method Resolution Order).

**Why it matters:**
Multiple inheritance enables code reuse from multiple sources but can lead to complexity and the diamond problem if not used carefully.

**Code Example:**
```python
class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):  # Multiple inheritance
    def quack(self):
        print("Quack quack")

duck = Duck()
duck.fly()    # From Flyer
duck.swim()   # From Swimmer
duck.quack()  # Own method

# Diamond problem example
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.method()  # B's method (follows MRO: D -> B -> C -> A)
print(D.__mro__)  # Shows resolution order
```

**Key Takeaway:**
**Advantages**: Code reuse, combining features. **Disadvantages**: Complexity, diamond problem, harder to maintain. Use carefully with MRO awareness.

---

### Q30. What are some common Design Patterns in OOP?

**Definition:**
Design patterns are reusable solutions to common software design problems. Key OOP patterns include: Singleton (one instance), Factory (object creation), Observer (event notification), Strategy (interchangeable algorithms), Decorator (add functionality), and Adapter (interface conversion).

**Why it matters:**
Design patterns provide proven solutions, improve code maintainability, and enable better communication among developers using common vocabulary.

**Code Example:**
```python
# 1. Factory Pattern
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Woof

# 2. Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")

subject = Subject()
obs1 = Observer("Observer1")
obs2 = Observer("Observer2")
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Event occurred!")
# Output:
# Observer1 received: Event occurred!
# Observer2 received: Event occurred!
```

**Key Takeaway:**
Common patterns: Singleton, Factory, Observer, Strategy, Decorator, Adapter - learn and apply based on problem context.

---

## What Interviewers Look For

✅ **Clear Communication**: Can you explain concepts simply without jargon overload?  
✅ **Practical Understanding**: Do you know when and why to use each concept?  
✅ **Code Quality**: Are your examples clean, working, and relevant?  
✅ **Depth**: Can you go deeper when asked follow-up questions?  
✅ **Confidence**: Do you sound sure of what you know, and honest about what you don't?

## Common Pitfalls to Avoid

❌ **Memorizing definitions verbatim** - Explain in your own words  
❌ **Code without explanation** - Always connect code to concept  
❌ **Too theoretical** - Always give real-world context  
❌ **Saying "I don't know"** - Try to reason it out, show your thought process  
❌ **Going off-topic** - Stay focused on what's asked

---

## 📊 Key Comparison Tables

### Abstraction vs Encapsulation

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| **Purpose** | Hide complexity, show only essentials | Hide data, provide controlled access |
| **Focus** | What an object does | How data is protected |
| **Implementation** | Abstract classes, interfaces (ABC) | Access modifiers (public, protected, private) |
| **Example** | Payment interface with process_payment() | BankAccount with private __balance |
| **Level** | Design level | Implementation level |
| **Goal** | Reduce complexity | Data security and integrity |

### `__str__` vs `__repr__`

| Aspect | `__str__` | `__repr__` |
|--------|-----------|------------|
| **Purpose** | User-friendly display | Developer-friendly, unambiguous |
| **Target Audience** | End users | Developers/debugging |
| **Used By** | `print()`, `str()` | `repr()`, interactive shell |
| **Goal** | Readability | Recreate object (if possible) |
| **Example** | "Laptop - $999" | "Product('Laptop', 999)" |
| **Fallback** | Falls back to `__repr__` if not defined | Must be defined or uses default |

### Class vs Instance vs Static Methods

| Method Type | First Parameter | Access To | Use Case | Decorator |
|-------------|----------------|-----------|----------|-----------|
| **Instance** | `self` | Instance & class data | Object-specific operations | None |
| **Class** | `cls` | Only class data | Factory methods, class-level ops | `@classmethod` |
| **Static** | None | No instance/class data | Utility functions in class namespace | `@staticmethod` |

### Inheritance vs Composition

| Aspect | Inheritance (is-a) | Composition (has-a) |
|--------|-------------------|---------------------|
| **Relationship** | Child IS-A parent | Container HAS-A component |
| **Coupling** | Tight coupling | Loose coupling |
| **Flexibility** | Less flexible | More flexible |
| **Example** | Dog is-a Animal | Car has-a Engine |
| **When to Use** | Clear hierarchical relationship | Need functionality without relationship |
| **Modification** | Harder to change parent | Easy to swap components |

### Shallow Copy vs Deep Copy

| Aspect | Shallow Copy | Deep Copy |
|--------|--------------|-----------|
| **Method** | `copy.copy()` | `copy.deepcopy()` |
| **Copies** | Top-level object | All nested objects recursively |
| **Nested Objects** | Shares references | Creates new copies |
| **Speed** | Faster | Slower |
| **Memory** | Less memory | More memory |
| **Use Case** | When nested objects shouldn't be copied | When complete independence needed |

### Aggregation vs Composition

| Aspect | Aggregation | Composition |
|--------|-------------|-------------|
| **Ownership** | Weak (child can exist independently) | Strong (child cannot exist without parent) |
| **Lifecycle** | Child survives parent deletion | Child dies with parent |
| **Example** | Student in Department | Engine in Car |
| **Relationship Strength** | "uses-a" | "owns-a" |
| **Dependency** | Low | High |

---

## 🎯 Top 10 Most Asked Questions

These questions appear in 80%+ of OOP interviews. Master these first:

1. **🟢 Four Pillars of OOP** - The foundation question in every interview
2. **🟡 Inheritance Types** - Very commonly asked with diagram expectations
3. **🟡 Polymorphism Types** - Often followed by "give real example from your project"
4. **🟢 Abstraction vs Encapsulation** - Most confusing pair, frequently asked
5. **🟡 Method Overriding vs Overloading** - Python-specific nuances matter
6. **🔴 MRO & Diamond Problem** - Advanced but very popular for senior positions
7. **🟡 `super()` function** - Usage in multiple inheritance contexts
8. **🟡 Class vs Instance Variables** - Common pitfall question
9. **🔴 Composition vs Inheritance** - Design pattern preference question
10. **🟡 `__init__` vs `__new__`** - Python-specific, tests deep understanding

**Quick Study Strategy**: Focus on Q1, Q4, Q5, Q6, Q7, Q8, Q13, Q14, Q21, Q22 for 90% coverage.

---

## 📝 Quick Reference Cheat Sheet

### Four Pillars (Remember: EIPA)
- **E**ncapsulation → Data hiding with `__private`
- **I**nheritance → Code reuse via `class Child(Parent)`
- **P**olymorphism → Same interface, different behavior
- **A**bstraction → Hide complexity with ABC

### Method Types (Remember: ICS)
- **I**nstance methods → `def method(self):`
- **C**lass methods → `@classmethod def method(cls):`
- **S**tatic methods → `@staticmethod def method():`

### Access Modifiers (Remember: PPP)
- **P**ublic → `name` (accessible everywhere)
- **P**rotected → `_name` (convention, use internally)
- **P**rivate → `__name` (name mangled)

### Magic Methods (Most Important)
```python
__init__      # Constructor/Initializer
__new__       # Actual constructor (before __init__)
__str__       # User-friendly string
__repr__      # Developer-friendly representation
__add__       # + operator
__eq__        # == operator
__len__       # len() function
__getitem__   # [] indexing
__call__      # Make object callable like function
```

### Inheritance Syntax Quick Reference
```python
# Single
class Child(Parent):
    pass

# Multiple
class Child(Parent1, Parent2):
    pass

# Call parent
super().__init__()

# Check MRO
ClassName.mro()
```

### Common Interview Code Templates

**1. Property with Getter/Setter:**
```python
class Example:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError()
        self._value = val
```

**2. Singleton Pattern:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**3. Abstract Class:**
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        pass
```

### Interview Answer Framework

**Structure every answer as:**
1. **Definition** (1-2 sentences)
2. **Why it matters** (real-world context)
3. **Code example** (short, working code)
4. **Key takeaway** (one-liner to remember)

---

[⬆️ Back to Table of Contents](#-table-of-contents)

---

**Good luck with your interviews! 🚀**tions from References)

### Q35. What is a Destructor? How does it work in Python? 🟡

**Definition:**
A destructor is a special method called `__del__` in Python that is invoked when an object is about to be destroyed or garbage collected. It's used to perform cleanup operations like closing file handles, releasing resources, or cleaning up network connections before the object is removed from memory.

**Why it matters:**
Understanding destructors helps manage resources properly, though Python's garbage collector usually handles memory automatically. Explicit cleanup is sometimes needed for external resources.

**Code Example:**
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        print(f"File {filename} opened")
    
    def write_data(self, data):
        self.file.write(data)
    
    def __del__(self):
        self.file.close()
        print(f"File {self.filename} closed - Destructor called")

# Usage
fm = FileManager("test.txt")
fm.write_data("Hello World")
del fm  # Explicitly call destructor
# Output: File test.txt closed - Destructor called

# Note: Prefer context managers for resource management
class BetterFileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with BetterFileManager("better.txt") as bfm:
    bfm.file.write("Using context manager")
```

**Key Takeaway:**
`__del__` is Python's destructor - called when object is garbage collected. Prefer context managers (`with` statement) for resource management.

---

### Q36. What is Cohesion in OOP? 🟡

**Definition:**
Cohesion refers to how closely the methods and data within a single class are related to one another. High cohesion means a class is focused on a specific task or responsibility. Low cohesion indicates a class has multiple, often unrelated responsibilities. Functional cohesion (all methods contribute to single task) is most desirable.

**Why it matters:**
High cohesion aligns with the Single Responsibility Principle (SRP), making classes more maintainable, testable, and easier to understand.

**Code Example:**
```python
# LOW COHESION - Class doing unrelated things
class BadFileUtility:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()
    
    def write_to_database(self, data):
        print(f"Writing {data} to database")
    
    def send_email(self, recipient):
        print(f"Email sent to {recipient}")
    
    def calculate_tax(self, amount):
        return amount * 0.15

# HIGH COHESION - Focused classes
class FileReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()
    
    def read_lines(self):
        with open(self.filename, 'r') as f:
            return f.readlines()

class DatabaseWriter:
    def __init__(self, connection):
        self.connection = connection
    
    def write(self, data):
        print(f"Writing {data} to database")

class EmailSender:
    def send(self, recipient, message):
        print(f"Email sent to {recipient}: {message}")
```

**Key Takeaway:**
High cohesion = focused class with related methods. Low cohesion = class with unrelated responsibilities. Aim for functional cohesion following SRP.

---

### Q37. What is Coupling in OOP? 🟡

**Definition:**
Coupling describes the degree of interdependence between classes or modules. Loose coupling is preferred as it makes systems flexible and maintainable. Types range from content coupling (worst) to message coupling (best).

**Why it matters:**
Loose coupling enables independent development, testing, and modification of classes. It aligns with SOLID principles, particularly the Dependency Inversion Principle.

**Code Example:**
```python
# TIGHT COUPLING - Hard dependency
class TightEmailService:
    def send(self, recipient, message):
        print(f"Email: {recipient} - {message}")

class TightNotifier:
    def __init__(self):
        self.service = TightEmailService()  # Hard-coded!
    
    def notify(self, user, msg):
        self.service.send(user, msg)

# Problem: Cannot switch to SMS without changing TightNotifier

# LOOSE COUPLING - Dependency injection
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailService(NotificationService):
    def send(self, recipient, message):
        print(f"Email: {recipient} - {message}")

class SMSService(NotificationService):
    def send(self, recipient, message):
        print(f"SMS: {recipient} - {message}")

class LooseNotifier:
    def __init__(self, service: NotificationService):
        self.service = service  # Injected dependency
    
    def notify(self, user, msg):
        self.service.send(user, msg)

# Easy to switch implementations
email_notifier = LooseNotifier(EmailService())
email_notifier.notify("user@example.com", "Hello")

sms_notifier = LooseNotifier(SMSService())
sms_notifier.notify("+123", "Hello")
```

**Key Takeaway:**
Loose coupling = minimal dependencies via abstraction and dependency injection. Tight coupling = hard-coded dependencies. Favor loose coupling for flexibility.

---

### Q38. What is the difference between Procedural and OOP? 🟡

**Definition:**
Procedural programming is linear and task-centric, organizing code as functions that operate on data. OOP organizes code into objects that bundle data and methods together. Procedural emphasizes procedures/functions; OOP emphasizes objects and their interactions.

**Why it matters:**
Understanding paradigm differences helps choose the right approach for different problems and appreciate OOP's benefits in managing complexity and large-scale systems.

**Code Example:**
```python
# PROCEDURAL APPROACH
def calculate_gross_salary(base, bonus):
    return base + bonus

def calculate_tax(gross, rate):
    return gross * rate

def calculate_net_salary(base, bonus, tax_rate):
    gross = calculate_gross_salary(base, bonus)
    tax = calculate_tax(gross, tax_rate)
    return gross - tax

# Data separate from functions
employee_base = 50000
employee_bonus = 5000
tax_rate = 0.2

net = calculate_net_salary(employee_base, employee_bonus, tax_rate)
print(f"Net Salary: {net}")

# OBJECT-ORIENTED APPROACH
class Employee:
    def __init__(self, name, base_salary, bonus=0):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_gross(self):
        return self.base_salary + self.bonus
    
    def calculate_tax(self, tax_rate):
        return self.calculate_gross() * tax_rate
    
    def calculate_net_salary(self, tax_rate):
        gross = self.calculate_gross()
        tax = self.calculate_tax(tax_rate)
        return gross - tax

# Data and methods bundled together
emp = Employee("John", 50000, 5000)
net = emp.calculate_net_salary(0.2)
print(f"{emp.name}'s Net Salary: {net}")
```

**Key Takeaway:**
Procedural = functions operate on data (separated). OOP = data and methods bundled in objects (encapsulated). OOP provides better modularity, reusability, and maintainability for complex systems.

---

### Q39. What are Constructor Types in Python? 🟡

**Definition:**
Python constructors initialize objects. There are three main types: Default Constructor (no parameters except self), Parameterized Constructor (accepts arguments), and Copy Constructor pattern (creates object from existing object). Python uses `__init__` for initialization and `__new__` for actual object creation.

**Why it matters:**
Understanding constructor types helps in proper object initialization and copying mechanisms, preventing common bugs with mutable default arguments.

**Code Example:**
```python
import copy

class Student:
    # Class variable
    school = "Dayanand Sagar Engineering"
    
    # Default Constructor
    def __init__(self):
        self.name = "Unknown"
        self.roll_no = 0
        print("Default constructor called")

class ParameterizedStudent:
    # Parameterized Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        print(f"Parameterized constructor: {name}")

# Copy Constructor Pattern in Python
class Person:
    def __init__(self, name=None, age=None, person_obj=None):
        if person_obj:  # Copy from existing object
            self.name = person_obj.name
            self.age = person_obj.age
        else:
            self.name = name
            self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Usage
s1 = Student()  # Default
s2 = ParameterizedStudent("Amit", 101, [85, 90, 88])

# Copy constructor pattern
p1 = Person("Priya", 22)
p2 = Person(person_obj=p1)  # Copy from p1
p2.display()  # Name: Priya, Age: 22

# Alternative: Using copy module
p3 = copy.copy(p1)  # Shallow copy
p4 = copy.deepcopy(p1)  # Deep copy
```

**Key Takeaway:**
Python supports default and parameterized constructors via `__init__`. For copying, use copy constructor pattern or `copy` module. Avoid mutable default arguments.

---

## 📊 Additional Comparison Tables

### Procedural vs OOP Programming

| Aspect | Procedural | Object-Oriented |
|--------|-----------|-----------------|
| **Focus** | Functions/procedures | Objects and classes |
| **Data & Functions** | Separated | Bundled together (encapsulation) |
| **Data Access** | Often global | Controlled via access modifiers |
| **Code Reuse** | Function calls | Inheritance, polymorphism |
| **Approach** | Top-down | Bottom-up |
| **Security** | Less secure (exposed data) | More secure (data hiding) |
| **Modification** | Difficult (affects multiple places) | Easier (localized in classes) |
| **Real-world Modeling** | Difficult | Natural and intuitive |
| **Scalability** | Harder for large systems | Better for complex systems |
| **Examples** | C, Pascal | Java, Python, C++ |

### Cohesion Levels (Worst to Best)

| Level | Description | Desirability |
|-------|-------------|--------------|
| **Coincidental** | Random, unrelated methods | ❌ Worst |
| **Logical** | Methods grouped by logic type | ❌ Poor |
| **Temporal** | Methods executed at same time | ⚠️ Acceptable |
| **Procedural** | Methods in execution sequence | ⚠️ Acceptable |
| **Communicational** | Methods work on same data | ✅ Good |
| **Sequential** | Output of one = input of next | ✅ Good |
| **Functional** | All contribute to single task | ✅✅ Best |

### Coupling Types (Worst to Best)

| Type | Description | Level |
|------|-------------|-------|
| **Content Coupling** | One module modifies another's internals | ❌ Worst |
| **Common Coupling** | Modules share global data | ❌ Very Bad |
| **Control Coupling** | One module controls another's flow | ⚠️ Bad |
| **Stamp Coupling** | Modules share composite data | ⚠️ Moderate |
| **Data Coupling** | Modules share simple data | ✅ Good |
| **Message Coupling** | Communicate via interfaces only | ✅✅ Best |

### Constructor Types Comparison

| Type | Parameters | Use Case | Example |
|------|-----------|----------|---------|
| **Default** | None (only self) | Simple initialization | `def __init__(self):` |
| **Parameterized** | Accepts arguments | Custom initialization | `def __init__(self, name, age):` |
| **Copy** | Another object | Clone existing object | Use `copy` module or custom logic |

---

## 💡 Interview Pro Tips

### Based on Reference Materials

1. **Understand C++ vs Python differences**: Many OOP concepts originated in C++. Know how Python adapts them (e.g., no true private members, duck typing).

2. **Real-world analogies help**: Use examples like Bank Account (encapsulation), Vehicle inheritance, Payment systems (abstraction).

3. **Know when NOT to use OOP**: For simple scripts, procedural is fine. Don't over-engineer.

4. **SOLID principles connection**: Link your answers to SOLID when discussing coupling, cohesion, and design patterns.

5. **Memory management awareness**: Understand destructor differences - Python has garbage collection, unlike C++.

6. **Context managers over destructors**: In Python interviews, emphasize `with` statement and context managers for resource management.

---

**Good luck with your interviews! 🚀**

**Note:** This document has been enhanced with content from multiple OOP references, focusing on Python implementations while maintaining clarity and practical examples for campus placement interviews.