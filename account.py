"""
Account Module - Demonstrates Encapsulation, Inheritance, Abstraction, and Property Decorators
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
import json


class Transaction:
    """Transaction class demonstrating Encapsulation"""
    
    # Class variable (shared by all instances)
    transaction_count = 0
    
    def __init__(self, transaction_type: str, amount: float, balance_after: float, description: str = ""):
        # Private attributes (name mangling)
        self.__transaction_id = Transaction._generate_transaction_id()
        self.__timestamp = datetime.now()
        self.__type = transaction_type
        self.__amount = amount
        self.__balance_after = balance_after
        self.__description = description
        Transaction.transaction_count += 1
    
    @staticmethod
    def _generate_transaction_id():
        """Static method - doesn't need instance or class"""
        return f"TXN{Transaction.transaction_count + 1:06d}"
    
    # Property decorators for controlled access (Getters)
    @property
    def transaction_id(self):
        return self.__transaction_id
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @property
    def type(self):
        return self.__type
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def balance_after(self):
        return self.__balance_after
    
    @property
    def description(self):
        return self.__description
    
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.__type:12} | ${self.__amount:10.2f} | Balance: ${self.__balance_after:10.2f}"
    
    def __repr__(self):
        """Developer-friendly string representation"""
        return f"Transaction(id={self.__transaction_id}, type={self.__type}, amount={self.__amount})"
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'transaction_id': self.__transaction_id,
            'timestamp': self.__timestamp.isoformat(),
            'type': self.__type,
            'amount': self.__amount,
            'balance_after': self.__balance_after,
            'description': self.__description
        }


class Account(ABC):
    """
    Abstract Base Class demonstrating Abstraction
    Cannot be instantiated directly - must be subclassed
    """
    
    # Class variable
    total_accounts = 0
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        # Protected attributes (convention: use single underscore)
        self._account_number = self._generate_account_number()
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._is_active = True
        self._created_date = datetime.now()
        Account.total_accounts += 1
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._add_transaction("DEPOSIT", initial_balance, "Initial deposit")
    
    @classmethod
    def _generate_account_number(cls):
        """Class method - has access to class but not instance"""
        return f"ACC{cls.total_accounts + 1:08d}"
    
    @classmethod
    def get_total_accounts(cls):
        """Class method to get total accounts"""
        return cls.total_accounts
    
    # Property decorator with getter and setter
    @property
    def balance(self):
        """Getter for balance - controlled access"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Setter with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def account_holder(self):
        return self._account_holder
    
    @property
    def is_active(self):
        return self._is_active
    
    @property
    def transactions(self):
        return self._transactions.copy()  # Return copy to prevent external modification
    
    def _add_transaction(self, trans_type: str, amount: float, description: str = ""):
        """Protected method - internal use only"""
        transaction = Transaction(trans_type, amount, self._balance, description)
        self._transactions.append(transaction)
    
    def deposit(self, amount: float, description: str = "Deposit"):
        """Deposit money into account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if not self._is_active:
            raise Exception("Account is not active")
        
        self._balance += amount
        self._add_transaction("DEPOSIT", amount, description)
        return self._balance
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        """Withdraw money - to be overridden by subclasses"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if not self._is_active:
            raise Exception("Account is not active")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        
        self._balance -= amount
        self._add_transaction("WITHDRAWAL", amount, description)
        return self._balance
    
    @abstractmethod
    def calculate_interest(self) -> float:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_account_type(self) -> str:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def get_statement(self, last_n: Optional[int] = None) -> List[Transaction]:
        """Get transaction statement"""
        if last_n:
            return self._transactions[-last_n:]
        return self._transactions
    
    def close_account(self):
        """Close the account"""
        if self._balance > 0:
            raise Exception("Cannot close account with remaining balance")
        self._is_active = False
    
    def __str__(self):
        """String representation"""
        return (f"{self.get_account_type()} Account\n"
                f"Account Number: {self._account_number}\n"
                f"Holder: {self._account_holder}\n"
                f"Balance: ${self._balance:.2f}\n"
                f"Status: {'Active' if self._is_active else 'Closed'}")
    
    def __repr__(self):
        return f"{self.__class__.__name__}(number={self._account_number}, holder={self._account_holder}, balance={self._balance})"
    
    # Operator overloading
    def __eq__(self, other):
        """Check equality based on account number"""
        if isinstance(other, Account):
            return self._account_number == other._account_number
        return False
    
    def __lt__(self, other):
        """Compare accounts by balance"""
        if isinstance(other, Account):
            return self._balance < other._balance
        return NotImplemented
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'account_number': self._account_number,
            'account_type': self.get_account_type(),
            'account_holder': self._account_holder,
            'balance': self._balance,
            'is_active': self._is_active,
            'created_date': self._created_date.isoformat(),
            'transactions': [t.to_dict() for t in self._transactions]
        }


class SavingsAccount(Account):
    """
    Savings Account - Demonstrates Inheritance
    Inherits from Account and adds specific features
    """
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 3.5):
        super().__init__(account_holder, initial_balance)
        self.__interest_rate = interest_rate  # Private to SavingsAccount
        self.__withdrawal_limit = 5000.0  # Daily withdrawal limit
        self.__withdrawals_today = 0
    
    @property
    def interest_rate(self):
        return self.__interest_rate
    
    @interest_rate.setter
    def interest_rate(self, rate):
        if rate < 0 or rate > 20:
            raise ValueError("Interest rate must be between 0 and 20")
        self.__interest_rate = rate
    
    def calculate_interest(self) -> float:
        """Implementation of abstract method"""
        return self._balance * (self.__interest_rate / 100)
    
    def get_account_type(self) -> str:
        """Implementation of abstract method"""
        return "Savings"
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        """Override withdraw with additional validation"""
        if amount > self.__withdrawal_limit:
            raise ValueError(f"Withdrawal amount exceeds daily limit of ${self.__withdrawal_limit}")
        
        # Call parent class method
        return super().withdraw(amount, description)
    
    def credit_interest(self):
        """Credit interest to account"""
        interest = self.calculate_interest()
        self.deposit(interest, "Interest credited")
        return interest


class CurrentAccount(Account):
    """
    Current Account - Demonstrates Inheritance and Method Overriding
    """
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0, overdraft_limit: float = 1000.0):
        super().__init__(account_holder, initial_balance)
        self.__overdraft_limit = overdraft_limit
        self.__monthly_fee = 10.0
    
    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
    
    def calculate_interest(self) -> float:
        """Current accounts don't earn interest"""
        return 0.0
    
    def get_account_type(self) -> str:
        return "Current"
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        """Override to allow overdraft"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if not self._is_active:
            raise Exception("Account is not active")
        
        # Allow overdraft
        if amount > (self._balance + self.__overdraft_limit):
            raise ValueError(f"Insufficient balance. Overdraft limit: ${self.__overdraft_limit}")
        
        self._balance -= amount
        self._add_transaction("WITHDRAWAL", amount, description)
        return self._balance
    
    def charge_monthly_fee(self):
        """Charge monthly maintenance fee"""
        self._balance -= self.__monthly_fee
        self._add_transaction("FEE", self.__monthly_fee, "Monthly maintenance fee")


class FixedDepositAccount(Account):
    """
    Fixed Deposit Account - Demonstrates Inheritance
    """
    
    def __init__(self, account_holder: str, deposit_amount: float, tenure_months: int, interest_rate: float = 7.0):
        if deposit_amount < 1000:
            raise ValueError("Minimum deposit for FD is $1000")
        
        super().__init__(account_holder, deposit_amount)
        self.__tenure_months = tenure_months
        self.__interest_rate = interest_rate
        self.__maturity_date = self._calculate_maturity_date()
        self.__is_matured = False
    
    def _calculate_maturity_date(self):
        """Calculate maturity date"""
        from dateutil.relativedelta import relativedelta
        return self._created_date + relativedelta(months=self.__tenure_months)
    
    @property
    def maturity_date(self):
        return self.__maturity_date
    
    @property
    def is_matured(self):
        return datetime.now() >= self.__maturity_date
    
    def calculate_interest(self) -> float:
        """Calculate compound interest"""
        # Compound interest: A = P(1 + r/n)^(nt)
        # Here n=12 (monthly compounding), t=tenure in years
        principal = self._balance
        rate = self.__interest_rate / 100
        time = self.__tenure_months / 12
        maturity_amount = principal * ((1 + rate/12) ** (12 * time))
        return maturity_amount - principal
    
    def get_account_type(self) -> str:
        return "Fixed Deposit"
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        """FD doesn't allow withdrawal before maturity"""
        if not self.is_matured:
            raise Exception("Cannot withdraw before maturity date")
        
        return super().withdraw(amount, description)
    
    def mature_fd(self):
        """Mature the FD and credit interest"""
        if self.is_matured and not self.__is_matured:
            interest = self.calculate_interest()
            self.deposit(interest, "FD maturity interest")
            self.__is_matured = True
            return self._balance
        raise Exception("FD already matured or not yet matured")
