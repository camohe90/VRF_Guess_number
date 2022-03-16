#!/usr/bin/python3
from brownie import VRFConsumerV2, Wei
from scripts.helpful_scripts import  get_account


def main():
    account = get_account()
    vrf_contract = VRFConsumerV2[-1]
    try:
        transaction_details = {
            'from' : account,
            'value': Wei('0.1 ether')
        }
        guess_number_tx = vrf_contract.play(2, account.address, transaction_details)
        return guess_number_tx
    except:
        print("Tal vez no estas apostando la suficiente cantidad")
