import enum
import time
from typing import Optional
from src.server.client import ZerePyClient

from dotenv import load_dotenv
import os

# Load environment variables from .env.test
load_dotenv(".env.test")


class TransferActions(enum.Enum):
    WITHDRAW = "withdraw"
    SWEEP = "sweep"
    SWAP = "swap"
    CHAT = "chat"


BURN_ADDRESS = os.getenv("BURN_ADDRESS")
USDC_ADDRESS = os.getenv("USDC_ADDRESS")
PRIVATE_KEY = os.getenv("EVM_PRIVATE_KEY")
AFTER_BROADCAST = int(os.getenv("AFTER_BROADCAST"))
AMOUNT = os.getenv("AMOUNT")


if not BURN_ADDRESS or not USDC_ADDRESS or not PRIVATE_KEY or not AFTER_BROADCAST:
    raise ValueError("Missing environment variables")


client = ZerePyClient("http://localhost:8000")


def get_address():
    res = client.perform_action(
        connection="evm",
        action="get-address",
    )
    print(res)
    return res


def get_balance(token_address: Optional[str] = None):
    print("get_balance", token_address)
    res = client.perform_action(
        connection="evm",
        action="get-balance",
        params=[token_address],
    )
    print(res)
    return res


def sonic_get_balance(address: str, token_address: str = "0xnative"):
    print("sonic_get_balance", address, token_address)
    res = client.perform_action(
        connection="sonic",
        action="get-balance",
        params=[address, token_address],
    )
    print(res)
    return res


def sonic_custom_swap(
    token_in: str,
    token_out: str,
    amount: str,
    private_key: str,
    slippage: str = "0.5",
):
    print("sonic_custom_swap", token_in, token_out, amount, private_key, slippage)
    res = client.perform_action(
        connection="sonic",
        action="custom-swap",
        params=[token_in, token_out, amount, private_key, slippage],
    )
    print(res)
    return res


# List available agents
agents = client.list_agents()

client.load_agent("etheth")

# List connections
connections = client.list_connections()


# res = client.perform_action(
#     connection="evm",
#     action="get-address",
# )
# print(res)

sonic_get_balance(BURN_ADDRESS)
sonic_custom_swap(
    "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
    "0x29219dd400f2Bf60E5a23d13Be72B486D4038894",
    "0.1",
    PRIVATE_KEY,
)

# print("transfer-custom")
# res = client.perform_action(
#     connection="evm",
#     action="transfer-custom",
#     params=[
#         BURN_ADDRESS,
#         AMOUNT,
#         PRIVATE_KEY,
#         USDC_ADDRESS,
#     ],
# )
# print(res)
# time.sleep(AFTER_BROADCAST)
# get_balance(USDC_ADDRESS)


# # Start/stop agent loop
# # client.start_agent()
# # client.stop_agent()


# res = client.perform_action(
#     connection="openai",
#     action="chat",
#     params=[
#         "Hello, how are you?",
#     ],
# )
# print(res)
