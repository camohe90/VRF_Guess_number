#!/usr/bin/python3
from brownie import VRFConsumerV2, config, network, Wei
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_vrf_consumer():
    account = get_account()
    print(f"On network {network.show_active()}")
    subscription_id = config["networks"][network.show_active()]["subscription_id"]
    gas_lane = config["networks"][network.show_active()][
        "gas_lane"
    ]  # Also known as keyhash
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")

    vrf_consumer = VRFConsumerV2.deploy(
        subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,  # Also known as keyhash
        {"from": account,'value': Wei('0.1 ether')},
    )
    if config["networks"][network.show_active()].get("verify", False):
        vrf_consumer.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        VRFConsumerV2.publish_source(vrf_consumer)
    else:
        vrf_consumer.tx.wait(1)
    return vrf_consumer


def add_vrf_consumer_to_subscription(subscription_id, vrf_consumer):
    vrf_coordinator = get_contract("vrf_coordinator")
    subscription_details = vrf_coordinator.getSubscription(subscription_id)
    if vrf_consumer in subscription_details[3]:
        print(f"{vrf_consumer} is already in the subscription")
    else:
        print(
            f"Adding consumer to subscription {subscription_id} on address {vrf_consumer}"
        )
        account = get_account()
        tx = vrf_coordinator.addConsumer.transact(
            subscription_id, vrf_consumer.address, {"from": account}
        )
        tx.wait(1)
        print("Consumer added to subscription!")


def main():
    vrf_consumer = deploy_vrf_consumer()
    vrf_consumer = VRFConsumerV2[-1]
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        add_vrf_consumer_to_subscription(
            config["networks"][network.show_active()]["subscription_id"], vrf_consumer
        )
