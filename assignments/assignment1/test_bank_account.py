"""
Tests for Assignment 1: OOP Basics
"""
import pytest
from bank_account import BankAccount, SavingsAccount, CheckingAccount


class TestBankAccount:
    def test_initial_balance(self):
        acc = BankAccount("Alice", 500.0)
        assert acc.balance == 500.0

    def test_deposit(self):
        acc = BankAccount("Alice", 100.0)
        acc.deposit(50.0)
        assert acc.balance == 150.0

    def test_deposit_negative_raises(self):
        acc = BankAccount("Alice", 100.0)
        with pytest.raises(ValueError):
            acc.deposit(-10.0)

    def test_withdraw(self):
        acc = BankAccount("Alice", 100.0)
        acc.withdraw(40.0)
        assert acc.balance == 60.0

    def test_withdraw_insufficient_raises(self):
        acc = BankAccount("Alice", 50.0)
        with pytest.raises(ValueError):
            acc.withdraw(100.0)

    def test_str(self):
        acc = BankAccount("Alice", 100.0)
        assert "Alice" in str(acc)
        assert "100.00" in str(acc)


class TestSavingsAccount:
    def test_apply_interest(self):
        acc = SavingsAccount("Bob", 1000.0, interest_rate=0.10)
        acc.apply_interest()
        assert acc.balance == pytest.approx(1100.0)

    def test_inherits_deposit(self):
        acc = SavingsAccount("Bob", 200.0)
        acc.deposit(100.0)
        assert acc.balance == 300.0

    def test_str_contains_interest_rate(self):
        acc = SavingsAccount("Bob", 500.0, interest_rate=0.05)
        assert "5.00%" in str(acc)


class TestCheckingAccount:
    def test_withdraw_within_overdraft(self):
        acc = CheckingAccount("Carol", 50.0, overdraft_limit=200.0)
        acc.withdraw(100.0)
        assert acc.balance == pytest.approx(-50.0)

    def test_withdraw_exceeds_overdraft_raises(self):
        acc = CheckingAccount("Carol", 50.0, overdraft_limit=100.0)
        with pytest.raises(ValueError):
            acc.withdraw(200.0)

    def test_str_contains_overdraft_limit(self):
        acc = CheckingAccount("Carol", 0.0, overdraft_limit=150.0)
        assert "150.00" in str(acc)
