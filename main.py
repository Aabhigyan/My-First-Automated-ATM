# ==========================================
# COLAB COMPATIBILITY CHECK
# ==========================================
# Agar koi aapka code Google Colab par chalayega, 
# toh yeh block automatically 'atm_account.py' file create kar dega.
try:
    import google.colab
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

if IN_COLAB:
    print("[INFO] Google Colab detected. Automatically creating 'atm_account.py' file...")
    with open("atm_account.py", "w") as f:
        f.write('''class Atm:
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
''')
    import sys
    sys.path.append('/content')

# ==========================================
# ACTUAL MAIN EXECUTION
# ==========================================
from atm_account import Atm

if __name__ == "__main__":
    print("=== STARTING AUTOMATED ATM TRANSACTION TESTING ===\n")
    
    rahul_atm = Atm(account_holder="Rahul")
    rahul_atm.create_pin(new_pin="4321", initial_deposit=3000)
    
    print("\n--- Test 1: Checking Balance with correct PIN ---")
    current_balance = rahul_atm.check_balance(entered_pin="4321")
    if current_balance != -1:
        print(f"Rahul's Balance is: ${current_balance}")
        
    print("\n--- Test 2: Withdrawing valid amount ($500) ---")
    rahul_atm.withdraw(entered_pin="4321", amount=500)
    
    print("\n--- Test 3: Unauthorized withdrawal attempt (Wrong PIN) ---")
    rahul_atm.withdraw(entered_pin="1111", amount=100)
    
    print("\n--- Test 4: Withdrawing more than available balance ($5000) ---")
    rahul_atm.withdraw(entered_pin="4321", amount=5000)
    
    print("\n--- Test 5: Changing PIN ---")
    rahul_atm.change_pin(old_pin="4321", new_pin="9999")
    
    print("\n=== ATM TRANSACTION TESTING COMPLETED ===")
