"""
Unit Tests for BankApplication

Tests cover:
- Account creation and management
- Customer operations
- Bank-level operations
- Transaction handling
- Error cases and edge cases
"""

import unittest
from datetime import datetime
from account import Account, SavingsAccount, CurrentAccount, Transaction
from customer import Customer
from bank import Bank


class TestTransaction(unittest.TestCase):
    """Test cases for Transaction class"""
    
    def test_transaction_creation(self):
        """Test basic transaction creation"""
        txn = Transaction("Deposit", 1000.0, 1000.0, "Initial deposit")
        
        self.assertEqual(txn.type, "Deposit")
        self.assertEqual(txn.amount, 1000.0)
        self.assertEqual(txn.balance_after, 1000.0)
        self.assertIsNotNone(txn.transaction_id)
        self.assertIsInstance(txn.timestamp, datetime)
    
    def test_transaction_id_format(self):
        """Test transaction ID format"""
        txn = Transaction("Withdrawal", 500.0, 500.0)
        self.assertTrue(txn.transaction_id.startswith("TXN"))
        self.assertEqual(len(txn.transaction_id), 9)  # TXN + 6 digits


class TestAccount(unittest.TestCase):
    """Test cases for Account class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.customer = Customer("John Doe", "john@example.com", "1234567890")
        self.account = Account(self.customer, account_type="Savings")
    
    def test_account_creation(self):
        """Test account creation with default values"""
        self.assertEqual(self.account.account_holder, self.customer)
        self.assertGreater(self.account.account_number, 0)
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.account_type, "Savings")
    
    def test_deposit(self):
        """Test deposit operation"""
        initial_balance = self.account.balance
        
        result = self.account.deposit(1000.0)
        
        self.assertTrue(result)
        self.assertEqual(self.account.balance, initial_balance + 1000.0)
        self.assertEqual(len(self.account.transactions), 1)
    
    def test_deposit_invalid_amount(self):
        """Test deposit with invalid amount"""
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)
        
        with self.assertRaises(ValueError):
            self.account.deposit(0.0)
    
    def test_withdraw_success(self):
        """Test successful withdrawal"""
        self.account.deposit(1000.0)
        
        result = self.account.withdraw(500.0)
        
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 500.0)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds"""
        self.account.deposit(500.0)
        
        result = self.account.withdraw(1000.0)
        
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 500.0)
    
    def test_withdraw_invalid_amount(self):
        """Test withdrawal with invalid amount"""
        self.account.deposit(1000.0)
        
        with self.assertRaises(ValueError):
            self.account.withdraw(-100.0)
    
    def test_get_balance(self):
        """Test balance inquiry"""
        self.account.deposit(1000.0)
        self.account.withdraw(300.0)
        
        self.assertEqual(self.account.get_balance(), 700.0)
    
    def test_get_transaction_history(self):
        """Test transaction history"""
        self.account.deposit(1000.0)
        self.account.withdraw(300.0)
        
        history = self.account.get_transaction_history()
        
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].type, "Deposit")
        self.assertEqual(history[1].type, "Withdrawal")


class TestSavingsAccount(unittest.TestCase):
    """Test cases for SavingsAccount class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.customer = Customer("Jane Doe", "jane@example.com", "0987654321")
        self.account = SavingsAccount(self.customer, min_balance=500.0)
    
    def test_savings_account_creation(self):
        """Test savings account specific attributes"""
        self.assertEqual(self.account.min_balance, 500.0)
        self.assertEqual(self.account.interest_rate, 0.035)  # Default 3.5%
    
    def test_apply_interest(self):
        """Test interest application"""
        self.account.deposit(10000.0)
        
        self.account.apply_interest()
        
        # Balance should be 10000 + 3.5% interest = 10350
        self.assertAlmostEqual(self.account.balance, 10350.0, places=2)
    
    def test_withdraw_below_min_balance(self):
        """Test withdrawal that would go below minimum balance"""
        self.account.deposit(1000.0)
        
        # Try to withdraw so that balance goes below 500
        result = self.account.withdraw(600.0)
        
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)


class TestCurrentAccount(unittest.TestCase):
    """Test cases for CurrentAccount class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.customer = Customer("Business Corp", "business@example.com", "1111111111")
        self.account = CurrentAccount(self.customer, overdraft_limit=5000.0)
    
    def test_current_account_creation(self):
        """Test current account specific attributes"""
        self.assertEqual(self.account.overdraft_limit, 5000.0)
    
    def test_overdraft_withdrawal(self):
        """Test withdrawal using overdraft"""
        self.account.deposit(1000.0)
        
        # Withdraw more than balance but within overdraft limit
        result = self.account.withdraw(4000.0)
        
        self.assertTrue(result)
        self.assertEqual(self.account.balance, -3000.0)  # Negative balance allowed
    
    def test_exceed_overdraft_limit(self):
        """Test withdrawal exceeding overdraft limit"""
        self.account.deposit(1000.0)
        
        # Try to withdraw beyond overdraft limit
        result = self.account.withdraw(7000.0)
        
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class"""
    
    def test_customer_creation(self):
        """Test customer creation"""
        customer = Customer("Alice Smith", "alice@example.com", "1234567890")
        
        self.assertEqual(customer.name, "Alice Smith")
        self.assertEqual(customer.email, "alice@example.com")
        self.assertEqual(customer.phone, "1234567890")
        self.assertIsInstance(customer.created_at, datetime)
    
    def test_add_account(self):
        """Test adding account to customer"""
        customer = Customer("Bob Johnson", "bob@example.com", "9876543210")
        account = Account(customer)
        
        customer.add_account(account)
        
        self.assertEqual(len(customer.accounts), 1)
        self.assertIn(account, customer.accounts)
    
    def test_get_total_balance(self):
        """Test total balance calculation across accounts"""
        customer = Customer("Charlie Brown", "charlie@example.com", "5555555555")
        
        account1 = Account(customer)
        account2 = Account(customer)
        
        account1.deposit(1000.0)
        account2.deposit(2000.0)
        
        customer.add_account(account1)
        customer.add_account(account2)
        
        self.assertEqual(customer.get_total_balance(), 3000.0)


class TestBank(unittest.TestCase):
    """Test cases for Bank class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bank = Bank("Test Bank", "TB001")
        self.customer1 = Customer("Customer 1", "c1@example.com", "1111111111")
        self.customer2 = Customer("Customer 2", "c2@example.com", "2222222222")
    
    def test_bank_creation(self):
        """Test bank creation"""
        self.assertEqual(self.bank.name, "Test Bank")
        self.assertEqual(self.bank.bank_code, "TB001")
        self.assertEqual(len(self.bank.customers), 0)
    
    def test_add_customer(self):
        """Test adding customer to bank"""
        self.bank.add_customer(self.customer1)
        
        self.assertEqual(len(self.bank.customers), 1)
        self.assertIn(self.customer1, self.bank.customers)
    
    def test_create_account(self):
        """Test account creation through bank"""
        self.bank.add_customer(self.customer1)
        
        account = self.bank.create_account(self.customer1, "Savings")
        
        self.assertIsNotNone(account)
        self.assertEqual(account.account_holder, self.customer1)
        self.assertEqual(account.account_type, "Savings")
    
    def test_find_customer(self):
        """Test finding customer by name"""
        self.bank.add_customer(self.customer1)
        self.bank.add_customer(self.customer2)
        
        found = self.bank.find_customer("Customer 1")
        
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Customer 1")
    
    def test_get_total_deposits(self):
        """Test total deposits calculation"""
        self.bank.add_customer(self.customer1)
        
        account = self.bank.create_account(self.customer1, "Savings")
        account.deposit(5000.0)
        
        total = self.bank.get_total_deposits()
        
        self.assertEqual(total, 5000.0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    def test_multiple_transactions(self):
        """Test many transactions"""
        customer = Customer("Test User", "test@example.com", "9999999999")
        account = Account(customer)
        
        for i in range(100):
            account.deposit(100.0)
        
        self.assertEqual(account.balance, 10000.0)
        self.assertEqual(len(account.transactions), 100)
    
    def test_zero_balance_operations(self):
        """Test operations on zero-balance account"""
        customer = Customer("Zero Balance", "zero@example.com", "0000000000")
        account = Account(customer)
        
        # Withdraw from zero balance
        result = account.withdraw(1.0)
        self.assertFalse(result)
        
        # Deposit then withdraw exact amount
        account.deposit(100.0)
        account.withdraw(100.0)
        self.assertEqual(account.balance, 0.0)
    
    def test_large_amounts(self):
        """Test with very large amounts"""
        customer = Customer("Rich User", "rich@example.com", "1111111111")
        account = Account(customer)
        
        large_amount = 1_000_000_000.0  # 1 billion
        account.deposit(large_amount)
        
        self.assertEqual(account.balance, large_amount)
        account.withdraw(large_amount / 2)
        self.assertEqual(account.balance, large_amount / 2)


def run_tests():
    """Run all tests and print summary"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestTransaction))
    suite.addTests(loader.loadTestsFromTestCase(TestAccount))
    suite.addTests(loader.loadTestsFromTestCase(TestSavingsAccount))
    suite.addTests(loader.loadTestsFromTestCase(TestCurrentAccount))
    suite.addTests(loader.loadTestsFromTestCase(TestCustomer))
    suite.addTests(loader.loadTestsFromTestCase(TestBank))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
