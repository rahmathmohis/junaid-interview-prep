"""
Bank Module - Demonstrates Singleton Pattern, Facade Pattern, and Complex System Management
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
from account import Account, SavingsAccount, CurrentAccount, FixedDepositAccount
from customer import Customer, Address, ContactInfo, PremiumCustomer


class Bank:
    """
    Bank class - Demonstrates Singleton Pattern
    Only one instance of Bank should exist
    """
    
    # Singleton instance
    _instance = None
    _initialized = False
    
    def __new__(cls, bank_name: str = "MyBank"):
        """Override __new__ to implement Singleton"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, bank_name: str = "MyBank"):
        """Initialize only once"""
        if not Bank._initialized:
            self.__bank_name = bank_name
            self.__bank_code = "MYBANK001"
            self.__customers: Dict[str, Customer] = {}
            self.__accounts: Dict[str, Account] = {}
            self.__established_date = datetime.now()
            Bank._initialized = True
    
    @property
    def bank_name(self):
        return self.__bank_name
    
    @property
    def bank_code(self):
        return self.__bank_code
    
    @property
    def total_customers(self):
        return len(self.__customers)
    
    @property
    def total_accounts(self):
        return len(self.__accounts)
    
    def register_customer(self, first_name: str, last_name: str, date_of_birth: str,
                         street: str, city: str, state: str, zip_code: str,
                         email: str, phone: str, id_proof: str,
                         is_premium: bool = False, relationship_manager: str = None) -> Customer:
        """Register a new customer - Factory Method Pattern"""
        
        # Create address and contact (Composition)
        address = Address(street, city, state, zip_code)
        contact = ContactInfo(email, phone)
        
        # Create appropriate customer type
        if is_premium:
            if not relationship_manager:
                raise ValueError("Relationship manager required for premium customers")
            customer = PremiumCustomer(first_name, last_name, date_of_birth, 
                                      address, contact, id_proof, relationship_manager)
        else:
            customer = Customer(first_name, last_name, date_of_birth, 
                              address, contact, id_proof)
        
        self.__customers[customer.customer_id] = customer
        return customer
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        return self.__customers.get(customer_id)
    
    def get_all_customers(self) -> List[Customer]:
        """Get all customers"""
        return list(self.__customers.values())
    
    def open_account(self, customer_id: str, account_type: str, 
                    initial_balance: float = 0.0, **kwargs) -> Account:
        """
        Open new account - Factory Method Pattern
        Demonstrates polymorphism through different account types
        """
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        if not customer.is_active:
            raise Exception("Customer account is not active")
        
        # Factory pattern for creating different account types
        account = None
        account_type = account_type.upper()
        
        if account_type == "SAVINGS":
            interest_rate = kwargs.get('interest_rate', 3.5)
            account = SavingsAccount(customer.full_name, initial_balance, interest_rate)
        
        elif account_type == "CURRENT":
            overdraft_limit = kwargs.get('overdraft_limit', 1000.0)
            account = CurrentAccount(customer.full_name, initial_balance, overdraft_limit)
        
        elif account_type == "FD" or account_type == "FIXED_DEPOSIT":
            tenure_months = kwargs.get('tenure_months')
            interest_rate = kwargs.get('interest_rate', 7.0)
            if not tenure_months:
                raise ValueError("Tenure months required for FD account")
            account = FixedDepositAccount(customer.full_name, initial_balance, 
                                         tenure_months, interest_rate)
        else:
            raise ValueError(f"Invalid account type: {account_type}")
        
        # Add account to customer and bank
        customer.add_account(account)
        self.__accounts[account.account_number] = account
        
        return account
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Get account by number"""
        return self.__accounts.get(account_number)
    
    def close_account(self, account_number: str):
        """Close an account"""
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        account.close_account()
    
    def transfer(self, from_account_number: str, to_account_number: str, amount: float):
        """Transfer money between accounts"""
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        
        if not from_account or not to_account:
            raise ValueError("Invalid account number")
        
        # Perform transfer (atomic operation)
        from_account.withdraw(amount, f"Transfer to {to_account_number}")
        to_account.deposit(amount, f"Transfer from {from_account_number}")
    
    def get_total_deposits(self) -> float:
        """Calculate total deposits in the bank"""
        return sum(account.balance for account in self.__accounts.values() 
                  if account.is_active)
    
    def get_customer_report(self, customer_id: str) -> dict:
        """Generate customer report"""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        accounts_info = []
        for account in customer.accounts:
            accounts_info.append({
                'account_number': account.account_number,
                'account_type': account.get_account_type(),
                'balance': account.balance,
                'is_active': account.is_active
            })
        
        return {
            'customer_info': customer.to_dict(),
            'accounts': accounts_info,
            'total_balance': customer.get_total_balance()
        }
    
    def search_customers(self, query: str) -> List[Customer]:
        """Search customers by name"""
        results = []
        query_lower = query.lower()
        for customer in self.__customers.values():
            if (query_lower in customer.full_name.lower() or 
                query_lower in customer.customer_id.lower()):
                results.append(customer)
        return results
    
    def get_high_value_customers(self, min_balance: float = 100000) -> List[Customer]:
        """Get customers with high total balance"""
        return [customer for customer in self.__customers.values() 
                if customer.get_total_balance() >= min_balance]
    
    def __str__(self):
        return (f"{self.__bank_name} (Code: {self.__bank_code})\n"
                f"Total Customers: {self.total_customers}\n"
                f"Total Accounts: {self.total_accounts}\n"
                f"Total Deposits: ${self.get_total_deposits():.2f}")
    
    def __repr__(self):
        return f"Bank(name={self.__bank_name}, customers={self.total_customers}, accounts={self.total_accounts})"


class BankService:
    """
    Bank Service - Demonstrates Facade Pattern
    Provides simplified interface to complex bank operations
    """
    
    def __init__(self):
        self.__bank = Bank("Global Trust Bank")
    
    @property
    def bank(self):
        return self.__bank
    
    def create_new_customer_with_account(self, customer_data: dict, account_data: dict) -> tuple:
        """
        Simplified method to create customer and open account in one call
        Demonstrates Facade Pattern
        """
        # Register customer
        customer = self.__bank.register_customer(
            first_name=customer_data['first_name'],
            last_name=customer_data['last_name'],
            date_of_birth=customer_data['date_of_birth'],
            street=customer_data['street'],
            city=customer_data['city'],
            state=customer_data['state'],
            zip_code=customer_data['zip_code'],
            email=customer_data['email'],
            phone=customer_data['phone'],
            id_proof=customer_data['id_proof'],
            is_premium=customer_data.get('is_premium', False),
            relationship_manager=customer_data.get('relationship_manager')
        )
        
        # Open account
        account = self.__bank.open_account(
            customer_id=customer.customer_id,
            account_type=account_data['account_type'],
            initial_balance=account_data.get('initial_balance', 0.0),
            **account_data.get('additional_params', {})
        )
        
        return customer, account
    
    def perform_transaction(self, account_number: str, transaction_type: str, 
                          amount: float, **kwargs):
        """Perform various transactions"""
        account = self.__bank.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        transaction_type = transaction_type.upper()
        
        if transaction_type == "DEPOSIT":
            return account.deposit(amount, kwargs.get('description', 'Deposit'))
        
        elif transaction_type == "WITHDRAW":
            return account.withdraw(amount, kwargs.get('description', 'Withdrawal'))
        
        elif transaction_type == "TRANSFER":
            to_account = kwargs.get('to_account')
            if not to_account:
                raise ValueError("Destination account required for transfer")
            return self.__bank.transfer(account_number, to_account, amount)
        
        else:
            raise ValueError(f"Invalid transaction type: {transaction_type}")
    
    def get_account_statement(self, account_number: str, last_n: Optional[int] = None):
        """Get account statement"""
        account = self.__bank.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        transactions = account.get_statement(last_n)
        
        print(f"\n{'='*80}")
        print(f"Account Statement - {account.get_account_type()} Account")
        print(f"Account Number: {account_number}")
        print(f"Account Holder: {account.account_holder}")
        print(f"Current Balance: ${account.balance:.2f}")
        print(f"{'='*80}\n")
        print(f"{'Date & Time':<20} {'Type':<12} {'Amount':>12} {'Balance':>12}")
        print(f"{'-'*80}")
        
        for transaction in transactions:
            print(transaction)
        
        print(f"{'='*80}\n")
    
    def generate_bank_report(self):
        """Generate comprehensive bank report"""
        print(f"\n{'='*80}")
        print(f"BANK REPORT - {self.__bank.bank_name}")
        print(f"{'='*80}")
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"Total Customers: {self.__bank.total_customers}")
        print(f"Total Accounts: {self.__bank.total_accounts}")
        print(f"Total Deposits: ${self.__bank.get_total_deposits():.2f}\n")
        
        # High value customers
        high_value = self.__bank.get_high_value_customers(50000)
        print(f"High Value Customers (>$50,000): {len(high_value)}")
        
        # Account type distribution
        savings_count = sum(1 for acc in self.__bank.get_all_customers() 
                          for a in acc.accounts if a.get_account_type() == "Savings")
        current_count = sum(1 for acc in self.__bank.get_all_customers() 
                          for a in acc.accounts if a.get_account_type() == "Current")
        fd_count = sum(1 for acc in self.__bank.get_all_customers() 
                      for a in acc.accounts if a.get_account_type() == "Fixed Deposit")
        
        print(f"\nAccount Type Distribution:")
        print(f"  Savings Accounts: {savings_count}")
        print(f"  Current Accounts: {current_count}")
        print(f"  Fixed Deposits: {fd_count}")
        print(f"{'='*80}\n")
