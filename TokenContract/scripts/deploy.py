# deploy.py
from ape import project, accounts

def main():
    deployer = accounts.load("deployer")

    # Deploy the TokenContract with the given parameters
    token = deployer.deploy(
        project.TokenContract,
        "MyToken",
        "MTK"
    )

    print(f"Contract deployed to address: {token.address}")

