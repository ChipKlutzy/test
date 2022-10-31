from brownie import LiquidityValueCalculator, accounts

def main():
    acct = accounts.load("testAccount1")
    LiquidityValueCalculator.deploy("0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f", {'from' : acct})