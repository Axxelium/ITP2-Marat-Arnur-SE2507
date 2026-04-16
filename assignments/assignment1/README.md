# Assignment 1: OOP Basics — Classes, Objects, and Inheritance

## Description

Implement a simple banking system using object-oriented programming concepts:
classes, objects, encapsulation, and inheritance.

## Tasks

1. Create a `BankAccount` base class with:
   - `owner` and `balance` attributes
   - `deposit(amount)` and `withdraw(amount)` methods
   - `__str__` method for string representation

2. Create a `SavingsAccount` subclass that:
   - Adds an `interest_rate` attribute
   - Adds an `apply_interest()` method

3. Create a `CheckingAccount` subclass that:
   - Adds an `overdraft_limit` attribute
   - Overrides `withdraw` to allow overdraft up to the limit

## How to Run

```bash
python bank_account.py
```
