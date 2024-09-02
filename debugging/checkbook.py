#!/usr/bin/python3


class Checkbook:
    """
    A simple checkbook class to manage bank account balance with basic operations.

    Attributes
    ----------
    balance : float
        The current balance in the checkbook account.
    """

    def __init__(self):
        """Initialize a new Checkbook instance with a balance of $0.00."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook account.

        Parameters
        ----------
        amount : float
            The amount of money to deposit into the account. Must be a positive value.

        Raises
        ------
        ValueError
            If the amount is negative, an error is raised.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook account if sufficient funds are available.

        Parameters
        ----------
        amount : float
            The amount of money to withdraw from the account. Must be a positive value.

        Raises
        ------
        ValueError
            If the amount is negative, an error is raised.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance of the checkbook account."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Interact with the user and perform checkbook operations.

    The user can choose to deposit money, withdraw money, check the balance,
    or exit the program. User inputs are processed in a loop until 'exit' is selected.
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        )
        action = action.lower()

        if action == "exit":
            print("Exiting the program.")
            break

        if action in ["deposit", "withdraw"]:
            try:
                amount_str = input("Enter the amount: $")
                if amount_str.strip() == "":  # Handle empty input
                    raise ValueError("Amount cannot be empty.")

                amount = float(amount_str)

                if amount < 0:
                    raise ValueError("The amount must be a positive number.")

                if action == "deposit":
                    cb.deposit(amount)
                elif action == "withdraw":
                    cb.withdraw(amount)
            except ValueError as e:
                print(f"Error: {e}")

        elif action == "balance":
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
