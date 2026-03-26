"""
Assignment 1: OOP Basics — Classes, Objects, and Inheritance
ITP2 | SE-2057 | Arnur & Marat
"""


class BankAccount:
    """Base class representing a generic bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


class SavingsAccount(BankAccount):
    """Savings account that earns interest."""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest applied: {interest:.2f}. New balance: {self._balance:.2f}")

    def __str__(self) -> str:
        return (
            f"SavingsAccount(owner={self.owner!r}, balance={self._balance:.2f}, "
            f"interest_rate={self.interest_rate:.2%})"
        )


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection."""

    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 100.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance + self.overdraft_limit:
            raise ValueError(
                f"Exceeds overdraft limit of {self.overdraft_limit:.2f}."
            )
        self._balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")

    def __str__(self) -> str:
        return (
            f"CheckingAccount(owner={self.owner!r}, balance={self._balance:.2f}, "
            f"overdraft_limit={self.overdraft_limit:.2f})"
        )


def main():
    print("=== Bank Account Demo ===\n")

    # BankAccount
    account = BankAccount("Alice", 500.0)
    print(account)
    account.deposit(200.0)
    account.withdraw(100.0)
    print()

    # SavingsAccount
    savings = SavingsAccount("Bob", 1000.0, interest_rate=0.03)
    print(savings)
    savings.apply_interest()
    print()

    # CheckingAccount
    checking = CheckingAccount("Carol", 50.0, overdraft_limit=200.0)
    print(checking)
    checking.withdraw(100.0)   # allowed: uses overdraft
    print()


if __name__ == "__main__":
    main()
