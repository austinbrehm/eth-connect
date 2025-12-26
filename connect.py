"""Connect to Infura and access Ethereum blockchain data.

This module is meant to be executed as a script. It will retrieve
an Infura API key, connect to Infura, and retrieve blockchain data.

Usage:
    python connect.py
    python connect.py --ens austin.eth

Options:
    -h, --help      Show the help menu.
    --ens           Show Ethereum address for a specific domain name.
"""

import argparse
import subprocess

import web3


def get_infura_key() -> str:
    """Get the Infura API key from .bashrc file.

    Returns:
        key: Infura API key, stored in .bashrc file.
    """
    subprocess.run("source ~/.bashrc", shell=True, check=True)
    key = subprocess.run(
        "echo $INFURA_KEY", shell=True, capture_output=True, text=True, check=True
    ).stdout.rstrip()

    return key


if __name__ == "__main__":
    # Implement argument parser to retrieve coffee size from the terminal.
    parser = argparse.ArgumentParser()
    parser.add_argument("--ens", help="Get address of ENS domain name")
    args = parser.parse_args()

    # Get Infura API key.
    api_key = get_infura_key()

    # Connect to Infura via HTTP.
    provider = web3.Web3(
        web3.Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{api_key}")
    )

    if provider.is_connected():
        # Get most recent block number.
        print(f"Latest Proposed Block Number: {provider.eth.get_block_number()}")

        # Get current gas price, in gwei.
        print(f"Current Gas Price: {round(provider.eth.gas_price * 10E-10, 3)} gwei")

        if args.ens:
            # Get address for ENS address.
            print(f"Address for {args.ens}: {provider.ens.address(args.ens)}")
    else:
        print("Unable to connect to Infura. Make sure API key is up to date.")
