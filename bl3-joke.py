import time

def start_game():
    print("--- BORDERLANDS 3: MAYHEM EDITION ---")
    
    # The 'Evil' Plan
    print("\nInitializing Vault Hunter mode...")
    time.sleep(1)
    print("Locating Gearbox servers...")
    time.sleep(1)
    print("CRITICAL ERROR: Claptrap accidentally tripped over the power cord.")
    print("Servers status: 🔥 ABSOLUTE CHAOS 🔥")
    
    # The Joke
    print("\nWhy don't the Children of the Vault use bookmarks?")
    time.sleep(2)
    print("Because they prefer 'Burning' through the pages! Hahaha... get it? No? Okay.")
    
    # Interaction
    user_name = input("\nAnyway, before the sirens catch us, what's your name, Vault Hunter? ")
    
    # Final Response
    if user_name.lower() == "claptrap":
        print("\nMy apologies, Master! Please don't delete my personality subroutines!")
    else:
        print(f"\nWelcome to Pandora, {user_name}!")
        print("Now go find some loot before the server-fire reaches the snack room.")

if __name__ == "__main__":
    start_game()
