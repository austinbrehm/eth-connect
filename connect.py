"""Connect to Infura and access Ethereum blockchain data.

This module is meant to be executed as a script. It will retrieve
an Infura API key, connect to Infura, and retrieve data. 
"""

import subprocess

import ens
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
    # Get Infura API key.
    api_key = get_infura_key()

    # Connect to Infura via HTTP.
    provider = web3.Web3(
        web3.Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{api_key}")
    )

    # Get ENS address.
    ens = ens.ENS.from_web3(provider)
    NAME = "ens.eth"
    print(f"{NAME}'s Address: {ens.address(NAME)}")

    # Get most recent block number.
    print(f"Latest Block Number: {provider.eth.get_block_number()}")

    # Get current gas price, in gwei.
    print(f"Gas Price: {round(provider.eth.gas_price * 10E-10, 3)} gwei")
