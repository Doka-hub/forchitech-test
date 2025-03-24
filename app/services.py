from tronpy import Tron

def get_tron_info(address: str) -> dict:
    client = Tron()
    account = client.get_account(address)

    print(account)
    return {
        "address": address,
        "bandwidth": account.get('acquired_delegated_frozen_balance_for_bandwidth'),
        "energy": account.get('account_resource', {}).get('energy_window_size'),
        "balance": account.get('balance'),
    }
