"""
Main Banking Application - Demonstrates all OOP concepts in action
This is a comprehensive banking system showcasing:
- Encapsulation, Inheritance, Polymorphism, Abstraction
- Composition, Aggregation
- Design Patterns (Singleton, Factory, Facade)
- Property decorators, Static/Class methods
- Operator overloading
- Exception handling
"""

from bank import Bank, BankService
from customer import Customer, PremiumCustomer, Address, ContactInfo
from account import SavingsAccount, CurrentAccount, FixedDepositAccount
import sys


class BankingApp:
    """Main application class demonstrating OOP concepts"""
    
    def __init__(self):
        # Singleton Bank instance
        self.bank_service = BankService()
        self.bank = self.bank_service.bank
        self.current_customer_id = None
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print(f"  {self.bank.bank_name} - Banking Application")
        print("="*60)
        print("1.  Register New Customer")
        print("2.  Open New Account")
        print("3.  Deposit Money")
        print("4.  Withdraw Money")
        print("5.  Transfer Money")
        print("6.  Check Balance")
        print("7.  View Account Statement")
        print("8.  View Customer Details")
        print("9.  List All Customers")
        print("10. Search Customer")
        print("11. Calculate Interest (Savings)")
        print("12. Mature Fixed Deposit")
        print("13. Bank Report")
        print("14. Demo - Create Sample Data")
        print("0.  Exit")
        print("="*60)
    
    def register_customer(self):
        """Register new customer"""
        print("\n--- Register New Customer ---")
        
        try:
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            
            print("\nAddress Details:")
            street = input("Street: ").strip()
            city = input("City: ").strip()
            state = input("State: ").strip()
            zip_code = input("ZIP Code: ").strip()
            
            print("\nContact Details:")
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            
            id_proof = input("\nID Proof Number: ").strip()
            
            is_premium = input("Premium Customer? (y/n): ").strip().lower() == 'y'
            relationship_manager = None
            if is_premium:
                relationship_manager = input("Relationship Manager Name: ").strip()
            
            customer = self.bank.register_customer(
                first_name, last_name, dob,
                street, city, state, zip_code,
                email, phone, id_proof,
                is_premium, relationship_manager
            )
            
            print(f"\n✓ Customer registered successfully!")
            print(f"Customer ID: {customer.customer_id}")
            print(f"Name: {customer.full_name}")
            
            self.current_customer_id = customer.customer_id
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def open_account(self):
        """Open new account"""
        print("\n--- Open New Account ---")
        
        try:
            customer_id = input("Customer ID: ").strip()
            customer = self.bank.get_customer(customer_id)
            
            if not customer:
                print("✗ Customer not found!")
                return
            
            print(f"\nCustomer: {customer.full_name}")
            print("\nAccount Types:")
            print("1. Savings Account")
            print("2. Current Account")
            print("3. Fixed Deposit")
            
            choice = input("\nSelect account type (1-3): ").strip()
            initial_balance = float(input("Initial deposit amount: $").strip())
            
            kwargs = {}
            
            if choice == '1':
                account_type = "SAVINGS"
                interest_rate = input("Interest rate (default 3.5%): ").strip()
                if interest_rate:
                    kwargs['interest_rate'] = float(interest_rate)
            
            elif choice == '2':
                account_type = "CURRENT"
                overdraft = input("Overdraft limit (default $1000): ").strip()
                if overdraft:
                    kwargs['overdraft_limit'] = float(overdraft)
            
            elif choice == '3':
                account_type = "FD"
                tenure = int(input("Tenure in months: ").strip())
                interest_rate = input("Interest rate (default 7.0%): ").strip()
                kwargs['tenure_months'] = tenure
                if interest_rate:
                    kwargs['interest_rate'] = float(interest_rate)
            
            else:
                print("✗ Invalid choice!")
                return
            
            account = self.bank.open_account(customer_id, account_type, initial_balance, **kwargs)
            
            print(f"\n✓ Account opened successfully!")
            print(f"Account Number: {account.account_number}")
            print(f"Account Type: {account.get_account_type()}")
            print(f"Balance: ${account.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def deposit_money(self):
        """Deposit money"""
        print("\n--- Deposit Money ---")
        
        try:
            account_number = input("Account Number: ").strip()
            amount = float(input("Amount to deposit: $").strip())
            description = input("Description (optional): ").strip() or "Deposit"
            
            self.bank_service.perform_transaction(account_number, "DEPOSIT", amount, description=description)
            
            account = self.bank.get_account(account_number)
            print(f"\n✓ Deposit successful!")
            print(f"New Balance: ${account.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def withdraw_money(self):
        """Withdraw money"""
        print("\n--- Withdraw Money ---")
        
        try:
            account_number = input("Account Number: ").strip()
            amount = float(input("Amount to withdraw: $").strip())
            description = input("Description (optional): ").strip() or "Withdrawal"
            
            self.bank_service.perform_transaction(account_number, "WITHDRAW", amount, description=description)
            
            account = self.bank.get_account(account_number)
            print(f"\n✓ Withdrawal successful!")
            print(f"New Balance: ${account.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def transfer_money(self):
        """Transfer money between accounts"""
        print("\n--- Transfer Money ---")
        
        try:
            from_account = input("From Account Number: ").strip()
            to_account = input("To Account Number: ").strip()
            amount = float(input("Amount to transfer: $").strip())
            
            self.bank_service.perform_transaction(
                from_account, "TRANSFER", amount, to_account=to_account
            )
            
            from_acc = self.bank.get_account(from_account)
            to_acc = self.bank.get_account(to_account)
            
            print(f"\n✓ Transfer successful!")
            print(f"From Account Balance: ${from_acc.balance:.2f}")
            print(f"To Account Balance: ${to_acc.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def check_balance(self):
        """Check account balance"""
        print("\n--- Check Balance ---")
        
        try:
            account_number = input("Account Number: ").strip()
            account = self.bank.get_account(account_number)
            
            if not account:
                print("✗ Account not found!")
                return
            
            print(f"\nAccount Details:")
            print(account)
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def view_statement(self):
        """View account statement"""
        print("\n--- Account Statement ---")
        
        try:
            account_number = input("Account Number: ").strip()
            last_n = input("Number of transactions (press Enter for all): ").strip()
            
            last_n = int(last_n) if last_n else None
            self.bank_service.get_account_statement(account_number, last_n)
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def view_customer_details(self):
        """View customer details"""
        print("\n--- Customer Details ---")
        
        try:
            customer_id = input("Customer ID: ").strip()
            customer = self.bank.get_customer(customer_id)
            
            if not customer:
                print("✗ Customer not found!")
                return
            
            print(f"\n{customer}")
            
            if customer.accounts:
                print("\nAccounts:")
                for account in customer.accounts:
                    print(f"  • {account.account_number} - {account.get_account_type()} - ${account.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def list_customers(self):
        """List all customers"""
        print("\n--- All Customers ---\n")
        
        customers = self.bank.get_all_customers()
        
        if not customers:
            print("No customers found.")
            return
        
        print(f"{'Customer ID':<12} {'Name':<25} {'Age':<5} {'Accounts':<10} {'Total Balance':<15}")
        print("-" * 80)
        
        for customer in customers:
            print(f"{customer.customer_id:<12} {customer.full_name:<25} {customer.age:<5} "
                  f"{len(customer.accounts):<10} ${customer.get_total_balance():<14.2f}")
    
    def search_customer(self):
        """Search customer"""
        print("\n--- Search Customer ---")
        
        try:
            query = input("Enter customer name or ID: ").strip()
            customers = self.bank.search_customers(query)
            
            if not customers:
                print("✗ No customers found!")
                return
            
            print(f"\nFound {len(customers)} customer(s):\n")
            for customer in customers:
                print(f"ID: {customer.customer_id} | Name: {customer.full_name} | "
                      f"Accounts: {len(customer.accounts)} | Balance: ${customer.get_total_balance():.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def calculate_interest(self):
        """Calculate and credit interest for savings account"""
        print("\n--- Calculate Interest ---")
        
        try:
            account_number = input("Savings Account Number: ").strip()
            account = self.bank.get_account(account_number)
            
            if not account:
                print("✗ Account not found!")
                return
            
            if not isinstance(account, SavingsAccount):
                print("✗ This is not a savings account!")
                return
            
            interest = account.calculate_interest()
            print(f"\nInterest calculated: ${interest:.2f}")
            
            credit = input("Credit interest to account? (y/n): ").strip().lower()
            if credit == 'y':
                account.credit_interest()
                print(f"✓ Interest credited!")
                print(f"New Balance: ${account.balance:.2f}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def mature_fd(self):
        """Mature fixed deposit"""
        print("\n--- Mature Fixed Deposit ---")
        
        try:
            account_number = input("FD Account Number: ").strip()
            account = self.bank.get_account(account_number)
            
            if not account:
                print("✗ Account not found!")
                return
            
            if not isinstance(account, FixedDepositAccount):
                print("✗ This is not a fixed deposit account!")
                return
            
            print(f"\nMaturity Date: {account.maturity_date.strftime('%Y-%m-%d')}")
            print(f"Is Matured: {'Yes' if account.is_matured else 'No'}")
            
            if account.is_matured:
                interest = account.calculate_interest()
                print(f"Interest Amount: ${interest:.2f}")
                
                mature = input("Mature the FD? (y/n): ").strip().lower()
                if mature == 'y':
                    maturity_amount = account.mature_fd()
                    print(f"✓ FD matured successfully!")
                    print(f"Maturity Amount: ${maturity_amount:.2f}")
            else:
                print("FD has not matured yet!")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def bank_report(self):
        """Generate bank report"""
        self.bank_service.generate_bank_report()
    
    def create_demo_data(self):
        """Create sample data for demonstration"""
        print("\n--- Creating Demo Data ---")
        
        try:
            # Create customers with accounts
            customer1_data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'date_of_birth': '1990-05-15',
                'street': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'zip_code': '10001',
                'email': 'john.doe@email.com',
                'phone': '555-0101',
                'id_proof': 'DL123456'
            }
            
            account1_data = {
                'account_type': 'SAVINGS',
                'initial_balance': 5000.0,
                'additional_params': {'interest_rate': 4.0}
            }
            
            customer1, account1 = self.bank_service.create_new_customer_with_account(
                customer1_data, account1_data
            )
            
            # Create premium customer
            customer2_data = {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'date_of_birth': '1985-08-20',
                'street': '456 Park Ave',
                'city': 'Los Angeles',
                'state': 'CA',
                'zip_code': '90001',
                'email': 'jane.smith@email.com',
                'phone': '555-0102',
                'id_proof': 'DL789012',
                'is_premium': True,
                'relationship_manager': 'Robert Johnson'
            }
            
            account2_data = {
                'account_type': 'CURRENT',
                'initial_balance': 10000.0,
                'additional_params': {'overdraft_limit': 5000.0}
            }
            
            customer2, account2 = self.bank_service.create_new_customer_with_account(
                customer2_data, account2_data
            )
            
            # Create FD account for customer 1
            fd_account = self.bank.open_account(
                customer1.customer_id,
                "FD",
                15000.0,
                tenure_months=12,
                interest_rate=7.5
            )
            
            # Perform some transactions
            account1.deposit(1000, "Salary credit")
            account1.withdraw(500, "ATM withdrawal")
            account2.deposit(5000, "Business income")
            
            # Transfer between accounts
            self.bank.transfer(account1.account_number, account2.account_number, 500)
            
            print(f"✓ Demo data created successfully!")
            print(f"\nCustomer 1: {customer1.customer_id} - {customer1.full_name}")
            print(f"  Savings Account: {account1.account_number}")
            print(f"  FD Account: {fd_account.account_number}")
            print(f"\nCustomer 2: {customer2.customer_id} - {customer2.full_name} (Premium)")
            print(f"  Current Account: {account2.account_number}")
            
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*60)
        print("  Welcome to the Banking System")
        print("  Demonstrating OOP Concepts in Python")
        print("="*60)
        
        while True:
            try:
                self.display_menu()
                choice = input("\nEnter your choice (0-14): ").strip()
                
                if choice == '0':
                    print("\nThank you for using our banking system!")
                    print("Goodbye!")
                    break
                
                elif choice == '1':
                    self.register_customer()
                elif choice == '2':
                    self.open_account()
                elif choice == '3':
                    self.deposit_money()
                elif choice == '4':
                    self.withdraw_money()
                elif choice == '5':
                    self.transfer_money()
                elif choice == '6':
                    self.check_balance()
                elif choice == '7':
                    self.view_statement()
                elif choice == '8':
                    self.view_customer_details()
                elif choice == '9':
                    self.list_customers()
                elif choice == '10':
                    self.search_customer()
                elif choice == '11':
                    self.calculate_interest()
                elif choice == '12':
                    self.mature_fd()
                elif choice == '13':
                    self.bank_report()
                elif choice == '14':
                    self.create_demo_data()
                else:
                    print("\n✗ Invalid choice! Please try again.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                break
            except Exception as e:
                print(f"\n✗ Unexpected error: {str(e)}")
                input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    app = BankingApp()
    app.run()


if __name__ == "__main__":
    main()
