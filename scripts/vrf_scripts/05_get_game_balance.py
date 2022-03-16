#!/usr/bin/python3
from brownie import VRFConsumerV2


def main():
    vrf_contract = VRFConsumerV2[-1]
    try:
        print(f"El balance del juego es {vrf_contract.balance()}")
    except:
        print("Debes esperar por lo menos un minuto a menos que estes en local chain!")
