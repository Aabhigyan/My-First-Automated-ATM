# Dusri file se Atm class ko import kiya
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
