class Atm:
    def __init__(self, account_holder: str):
        self.account_holder = account_holder
        self.pin = ''
        self.balance = 0

    def create_pin(self, new_pin: str, initial_deposit: int):
        self.pin = new_pin
        self.balance = initial_deposit
        print(f"[SYSTEM] Account initialized for {self.account_holder}. Balance: ${self.balance}")

    def change_pin(self, old_pin: str, new_pin: str) -> bool:
        if old_pin == self.pin:
            self.pin = new_pin
            print('-> [SUCCESS] PIN changed successfully.')
            return True
        else:
            print('-> [ERROR] PIN change failed: Incorrect current PIN.')
            return False

    def check_balance(self, entered_pin: str) -> int:
        if entered_pin == self.pin:
            return self.balance
        else:
            print('-> [ERROR] Access Denied: Invalid PIN.')
            return -1

    def withdraw(self, entered_pin: str, amount: int) -> bool:
        if entered_pin != self.pin:
            print('-> [ERROR] Withdrawal failed: Invalid PIN.')
            return False
            
        if amount <= self.balance:
            self.balance -= amount
            print(f'-> [SUCCESS] Withdrawal of ${amount} successful. Remaining Balance: ${self.balance}')
            return True
        else:
            print(f'-> [ERROR] Withdrawal of ${amount} failed: Insufficient funds.')
            return False
