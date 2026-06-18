"""
Customer Module - Demonstrates Composition, Aggregation, and Has-A relationships
"""

from datetime import datetime
from typing import List, Optional
from account import Account, SavingsAccount, CurrentAccount, FixedDepositAccount


class Address:
    """Address class - demonstrates encapsulation"""
    
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str = "USA"):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
    
    @property
    def street(self):
        return self.__street
    
    @property
    def city(self):
        return self.__city
    
    @property
    def state(self):
        return self.__state
    
    @property
    def zip_code(self):
        return self.__zip_code
    
    @property
    def country(self):
        return self.__country
    
    def __str__(self):
        return f"{self.__street}, {self.__city}, {self.__state} {self.__zip_code}, {self.__country}"
    
    def to_dict(self):
        return {
            'street': self.__street,
            'city': self.__city,
            'state': self.__state,
            'zip_code': self.__zip_code,
            'country': self.__country
        }


class ContactInfo:
    """Contact Information - demonstrates encapsulation"""
    
    def __init__(self, email: str, phone: str, alternate_phone: Optional[str] = None):
        self.__email = email
        self.__phone = phone
        self.__alternate_phone = alternate_phone
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        self.__email = value
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    @property
    def alternate_phone(self):
        return self.__alternate_phone
    
    def __str__(self):
        return f"Email: {self.__email}, Phone: {self.__phone}"
    
    def to_dict(self):
        return {
            'email': self.__email,
            'phone': self.__phone,
            'alternate_phone': self.__alternate_phone
        }


class Customer:
    """
    Customer class - Demonstrates Composition and Aggregation
    
    Composition: Customer HAS-A Address, ContactInfo (owned by Customer)
    Aggregation: Customer HAS-A Account (can exist independently)
    """
    
    # Class variable
    customer_count = 0
    
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, 
                 address: Address, contact: ContactInfo, id_proof: str):
        # Private attributes
        self.__customer_id = self._generate_customer_id()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.__id_proof = id_proof
        self.__created_date = datetime.now()
        self.__is_active = True
        
        # Composition: Customer owns Address and ContactInfo
        # If Customer is deleted, these are also deleted
        self.__address = address
        self.__contact = contact
        
        # Aggregation: Customer has accounts, but accounts can exist independently
        self.__accounts: List[Account] = []
        
        Customer.customer_count += 1
    
    @staticmethod
    def _generate_customer_id():
        """Static method to generate customer ID"""
        return f"CUST{Customer.customer_count + 1:06d}"
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def date_of_birth(self):
        return self.__date_of_birth
    
    @property
    def age(self):
        """Calculated property"""
        today = datetime.now()
        age = today.year - self.__date_of_birth.year
        if today.month < self.__date_of_birth.month or \
           (today.month == self.__date_of_birth.month and today.day < self.__date_of_birth.day):
            age -= 1
        return age
    
    @property
    def address(self):
        return self.__address
    
    @property
    def contact(self):
        return self.__contact
    
    @property
    def accounts(self):
        return self.__accounts.copy()
    
    @property
    def is_active(self):
        return self.__is_active
    
    def add_account(self, account: Account):
        """Add account to customer - demonstrates aggregation"""
        if account not in self.__accounts:
            self.__accounts.append(account)
    
    def remove_account(self, account_number: str):
        """Remove account from customer"""
        for account in self.__accounts:
            if account.account_number == account_number:
                if account.balance > 0:
                    raise Exception("Cannot remove account with balance")
                self.__accounts.remove(account)
                return
        raise ValueError("Account not found")
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Get specific account"""
        for account in self.__accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def get_total_balance(self) -> float:
        """Calculate total balance across all accounts"""
        return sum(account.balance for account in self.__accounts if account.is_active)
    
    def update_address(self, new_address: Address):
        """Update customer address"""
        self.__address = new_address
    
    def update_contact(self, new_contact: ContactInfo):
        """Update customer contact"""
        self.__contact = new_contact
    
    def deactivate(self):
        """Deactivate customer"""
        if any(account.balance > 0 for account in self.__accounts):
            raise Exception("Cannot deactivate customer with active account balances")
        self.__is_active = False
    
    def __str__(self):
        return (f"Customer: {self.full_name} (ID: {self.__customer_id})\n"
                f"Age: {self.age}\n"
                f"Address: {self.__address}\n"
                f"Contact: {self.__contact}\n"
                f"Accounts: {len(self.__accounts)}\n"
                f"Total Balance: ${self.get_total_balance():.2f}")
    
    def __repr__(self):
        return f"Customer(id={self.__customer_id}, name={self.full_name}, accounts={len(self.__accounts)})"
    
    def __eq__(self, other):
        """Check equality based on customer ID"""
        if isinstance(other, Customer):
            return self.__customer_id == other.__customer_id
        return False
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            'customer_id': self.__customer_id,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'date_of_birth': self.__date_of_birth.strftime("%Y-%m-%d"),
            'age': self.age,
            'address': self.__address.to_dict(),
            'contact': self.__contact.to_dict(),
            'id_proof': self.__id_proof,
            'is_active': self.__is_active,
            'created_date': self.__created_date.isoformat(),
            'accounts': [acc.account_number for acc in self.__accounts],
            'total_balance': self.get_total_balance()
        }


class PremiumCustomer(Customer):
    """
    Premium Customer - Demonstrates Inheritance
    Extends Customer with premium benefits
    """
    
    def __init__(self, first_name: str, last_name: str, date_of_birth: str,
                 address: Address, contact: ContactInfo, id_proof: str, 
                 relationship_manager: str):
        super().__init__(first_name, last_name, date_of_birth, address, contact, id_proof)
        self.__relationship_manager = relationship_manager
        self.__reward_points = 0
        self.__premium_since = datetime.now()
    
    @property
    def relationship_manager(self):
        return self.__relationship_manager
    
    @property
    def reward_points(self):
        return self.__reward_points
    
    def add_reward_points(self, points: int):
        """Add reward points"""
        self.__reward_points += points
    
    def redeem_reward_points(self, points: int):
        """Redeem reward points"""
        if points > self.__reward_points:
            raise ValueError("Insufficient reward points")
        self.__reward_points -= points
    
    def get_premium_benefits(self):
        """Get premium benefits"""
        benefits = [
            "Dedicated Relationship Manager",
            "Higher interest rates on savings",
            "Zero monthly fees",
            "Priority customer service",
            "Reward points on transactions",
            "Free insurance coverage"
        ]
        return benefits
    
    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Premium Customer\n"
                f"Relationship Manager: {self.__relationship_manager}\n"
                f"Reward Points: {self.__reward_points}")
