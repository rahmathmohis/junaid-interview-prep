# 🏦 Comprehensive Banking System - OOP Demonstration

## Overview

This is a **complete banking application** built in Python that demonstrates **all major Object-Oriented Programming (OOP) concepts**. It's designed as a learning resource for understanding how OOP principles are applied in real-world applications.

## 🎯 OOP Concepts Demonstrated

### 1. **Encapsulation** ✅
- **Private attributes** using name mangling (`__attribute`)
- **Protected attributes** using single underscore (`_attribute`)
- **Property decorators** (@property) for controlled access
- **Getters and setters** with validation
- Data hiding and abstraction barriers

**Examples:**
```python
class Transaction:
    def __init__(self, amount):
        self.__amount = amount  # Private attribute
    
    @property
    def amount(self):
        return self.__amount  # Controlled access via property
```

### 2. **Inheritance** ✅
- **Single inheritance**: SavingsAccount, CurrentAccount, FixedDepositAccount inherit from Account
- **Method overriding**: Each account type overrides `calculate_interest()` and `withdraw()`
- **super()** usage for calling parent class methods
- **is-a relationship**: SavingsAccount IS-A Account

**Examples:**
```python
class SavingsAccount(Account):  # Inheritance
    def withdraw(self, amount):
        # Additional validation
        if amount > self.__withdrawal_limit:
            raise ValueError("Exceeds limit")
        return super().withdraw(amount)  # Call parent method
```

### 3. **Polymorphism** ✅
- **Method overriding**: Different account types have different `withdraw()` behaviors
- **Duck typing**: Any object with required methods can be used
- **Operator overloading**: `__eq__`, `__lt__`, `__str__`, `__repr__`

**Examples:**
```python
# Same interface, different implementations
savings.calculate_interest()  # Returns 3.5% interest
current.calculate_interest()   # Returns 0% interest
fd.calculate_interest()        # Returns 7.5% compound interest
```

### 4. **Abstraction** ✅
- **Abstract Base Classes (ABC)**: Account is abstract and cannot be instantiated
- **Abstract methods**: `calculate_interest()` and `get_account_type()` must be implemented by subclasses
- Hiding implementation details from users

**Examples:**
```python
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass  # Must be implemented by subclasses
```

### 5. **Composition** ✅
- **Strong ownership**: Customer HAS-A Address, Customer HAS-A ContactInfo
- When Customer is deleted, Address and ContactInfo are also deleted
- Parts cannot exist without the whole

**Examples:**
```python
class Customer:
    def __init__(self, address: Address, contact: ContactInfo):
        self.__address = address      # Composition
        self.__contact = contact      # Composition
```

### 6. **Aggregation** ✅
- **Weak association**: Customer HAS-A Account
- Accounts can exist independently of customers
- Parts can outlive the whole

**Examples:**
```python
class Customer:
    def __init__(self):
        self.__accounts = []  # Aggregation - accounts exist independently
    
    def add_account(self, account):
        self.__accounts.append(account)
```

### 7. **Class Methods & Static Methods** ✅
- **@classmethod**: Methods that work with class rather than instance
- **@staticmethod**: Methods that don't need class or instance
- **Class variables**: Shared across all instances

**Examples:**
```python
class Account:
    total_accounts = 0  # Class variable
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @staticmethod
    def _generate_id():
        return f"ACC{Account.total_accounts + 1}"
```

### 8. **Property Decorators** ✅
- **@property**: Define getters
- **@property.setter**: Define setters with validation
- Calculated properties
- Read-only properties

**Examples:**
```python
@property
def balance(self):
    return self._balance

@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("Balance cannot be negative")
    self._balance = value
```

### 9. **Design Patterns** ✅

#### **Singleton Pattern**
- Only one Bank instance can exist
```python
class Bank:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

#### **Factory Method Pattern**
- `open_account()` creates different account types
```python
def open_account(self, account_type):
    if account_type == "SAVINGS":
        return SavingsAccount(...)
    elif account_type == "CURRENT":
        return CurrentAccount(...)
```

#### **Facade Pattern**
- BankService provides simplified interface
```python
class BankService:
    def create_new_customer_with_account(self, customer_data, account_data):
        # Simplifies complex operations
        customer = self.bank.register_customer(...)
        account = self.bank.open_account(...)
        return customer, account
```

### 10. **Operator Overloading** ✅
- `__str__`: User-friendly string representation
- `__repr__`: Developer-friendly representation
- `__eq__`: Equality comparison
- `__lt__`: Less than comparison

**Examples:**
```python
def __str__(self):
    return f"Account: {self.account_number}, Balance: ${self.balance}"

def __eq__(self, other):
    return self.account_number == other.account_number
```

---

## 📁 Project Structure

```
BankApplication/
│
├── account.py          # Account classes (Abstract base, Savings, Current, FD)
├── customer.py         # Customer classes (Customer, PremiumCustomer, Address, Contact)
├── bank.py            # Bank and BankService classes
├── main.py            # Main application with CLI interface
├── README.md          # This file
└── requirements.txt   # Dependencies
```

---

## 🏗️ Class Hierarchy

```
ABC (Abstract Base Class)
 └── Account (Abstract)
      ├── SavingsAccount
      ├── CurrentAccount
      └── FixedDepositAccount

Customer
 └── PremiumCustomer

Bank (Singleton)

BankService (Facade)

Address (Composition with Customer)
ContactInfo (Composition with Customer)
Transaction (Encapsulation)
```

---

## 🚀 Features

### Account Management
- ✅ Create Savings, Current, and Fixed Deposit accounts
- ✅ Deposit and withdraw money
- ✅ Transfer between accounts
- ✅ Calculate and credit interest
- ✅ Transaction history
- ✅ Account statements

### Customer Management
- ✅ Register regular and premium customers
- ✅ Multiple accounts per customer
- ✅ Customer search functionality
- ✅ Address and contact information
- ✅ Customer reports

### Banking Operations
- ✅ Real-time balance updates
- ✅ Transaction validation
- ✅ Overdraft facility (Current accounts)
- ✅ Withdrawal limits (Savings accounts)
- ✅ Fixed deposit maturity handling
- ✅ Interest calculations

### Reporting
- ✅ Account statements
- ✅ Customer reports
- ✅ Bank-wide reports
- ✅ High-value customer identification

---

## 🛠️ Installation & Usage

### Prerequisites
```bash
Python 3.7 or higher
```

### Installation
```bash
# Clone or download the project
cd BankApplication

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
python main.py
```

### Quick Start - Demo Data
1. Run the application
2. Select option **14** to create demo data
3. Explore the system with pre-populated customers and accounts

---

## 📖 Usage Examples

### Example 1: Create Customer and Account
```python
from bank import Bank, BankService
from customer import Address, ContactInfo

# Initialize bank service
service = BankService()

# Create customer
customer_data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'date_of_birth': '1990-01-01',
    'street': '123 Main St',
    'city': 'New York',
    'state': 'NY',
    'zip_code': '10001',
    'email': 'john@email.com',
    'phone': '555-0100',
    'id_proof': 'DL123456'
}

account_data = {
    'account_type': 'SAVINGS',
    'initial_balance': 5000.0
}

customer, account = service.create_new_customer_with_account(customer_data, account_data)
print(f"Account created: {account.account_number}")
```

### Example 2: Perform Transactions
```python
# Deposit
account.deposit(1000, "Salary")

# Withdraw
account.withdraw(500, "ATM withdrawal")

# Transfer
bank.transfer(from_account, to_account, 200)

# Check balance
print(f"Balance: ${account.balance:.2f}")
```

### Example 3: Calculate Interest
```python
# For Savings Account
interest = savings_account.calculate_interest()
savings_account.credit_interest()

# For Fixed Deposit
if fd_account.is_matured:
    maturity_amount = fd_account.mature_fd()
```

---

## 🧪 Testing OOP Concepts

### Test Encapsulation
```python
account = SavingsAccount("John Doe", 1000)
# account.__balance = 5000  # Error: Cannot access private attribute
print(account.balance)  # OK: Use property decorator
```

### Test Inheritance
```python
savings = SavingsAccount("John", 1000, interest_rate=4.0)
current = CurrentAccount("Jane", 2000, overdraft_limit=1000)

# Both inherit from Account but have different behaviors
savings.withdraw(500)   # Has withdrawal limits
current.withdraw(2500)  # Allows overdraft
```

### Test Polymorphism
```python
accounts = [savings, current, fd]

for account in accounts:
    # Same interface, different implementations
    print(account.calculate_interest())
```

### Test Abstraction
```python
# account = Account("John", 1000)  # Error: Cannot instantiate abstract class
savings = SavingsAccount("John", 1000)  # OK: Concrete class
```

### Test Singleton
```python
bank1 = Bank()
bank2 = Bank()
print(bank1 is bank2)  # True: Same instance
```

---

## 🎓 Learning Outcomes

After studying this project, you will understand:

1. ✅ How to design a real-world application using OOP
2. ✅ When to use inheritance vs composition
3. ✅ How to implement design patterns
4. ✅ Proper encapsulation and data hiding
5. ✅ Abstract classes and interfaces
6. ✅ Property decorators and controlled access
7. ✅ Class methods, static methods, and instance methods
8. ✅ Operator overloading
9. ✅ Exception handling in OOP context
10. ✅ How all OOP concepts work together in practice

---

## 📚 Code Quality Features

- ✅ **Type hints** for better code documentation
- ✅ **Docstrings** for all classes and methods
- ✅ **Exception handling** for robust error management
- ✅ **Input validation** at multiple levels
- ✅ **Consistent naming conventions**
- ✅ **Separation of concerns** across modules
- ✅ **DRY principle** (Don't Repeat Yourself)
- ✅ **SOLID principles** applied

---

## 🔍 Interview Preparation

This project covers questions like:

1. **"Explain the four pillars of OOP with examples"**
   - See Account hierarchy for Encapsulation, Inheritance, Polymorphism, Abstraction

2. **"What's the difference between composition and aggregation?"**
   - Customer-Address (Composition) vs Customer-Account (Aggregation)

3. **"Implement the Singleton pattern"**
   - See Bank class

4. **"Explain method overriding with examples"**
   - See `withdraw()` and `calculate_interest()` in account types

5. **"What are property decorators?"**
   - See balance property with getter/setter

6. **"Difference between @staticmethod and @classmethod?"**
   - See Account class for both

7. **"How to implement an abstract class in Python?"**
   - See Account abstract base class

---

## 💡 Best Practices Demonstrated

1. **Encapsulation**: Private attributes with property decorators
2. **Single Responsibility**: Each class has one clear purpose
3. **Open-Closed Principle**: Easy to extend (new account types) without modifying existing code
4. **Liskov Substitution**: Any Account subclass can replace Account
5. **Interface Segregation**: Abstract methods define minimal interface
6. **Dependency Inversion**: Depend on abstractions (Account) not concrete classes

---

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new account types
- Implement additional design patterns
- Add loan functionality
- Create a GUI interface
- Add database persistence
- Implement authentication

---

## 📞 Support

For questions or clarifications about OOP concepts demonstrated in this project, please refer to the inline comments and docstrings.

---

## ⚖️ License

This project is created for educational purposes. Free to use and modify.

---

## 🎯 Summary

This banking system is a **complete, production-quality demonstration** of OOP in Python. Every major concept is implemented with real-world use cases. It serves as both a learning resource and a reference implementation for interviews and projects.

**Key Features:**
- ✅ All 4 OOP pillars
- ✅ Multiple design patterns
- ✅ Composition & Aggregation
- ✅ Property decorators
- ✅ Abstract classes
- ✅ Operator overloading
- ✅ Exception handling
- ✅ Real-world banking operations

**Perfect for:**
- 🎓 Learning OOP concepts
- 💼 Interview preparation
- 📝 Portfolio projects
- 🏫 Teaching material

---

**Created for interview preparation and OOP learning.**
**Dayanand Sagar Engineering - 4th Year**
