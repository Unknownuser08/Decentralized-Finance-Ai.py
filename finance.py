
import numpy as np
from typing import Any, Dict

class DeFiAgent:
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
        self.portfolio = {}
        self.governance_votes = {}

    def transact(self, token: str, amount: float, recipient: str):
        if token not in self.portfolio or self.portfolio[token] < amount:
            print(f"Insufficient {token} balance to transact {amount}.")
            return False
        print(f"Transacting {amount} {token} to {recipient}.")
        self.portfolio[token] -= amount
        return True

    def swap_tokens(self, token_in: str, token_out: str, amount_in: float):
        if token_in not in self.portfolio or self.portfolio[token_in] < amount_in:
            print(f"Insufficient {token_in} balance to swap {amount_in}.")
            return False
        exchange_rate = self._get_exchange_rate(token_in, token_out)
        amount_out = amount_in * exchange_rate
        print(f"Swapping {amount_in} {token_in} for {amount_out:.2f} {token_out}.")
        self.portfolio[token_in] -= amount_in
        self.portfolio[token_out] = self.portfolio.get(token_out, 0) + amount_out
        return True

    def provide_liquidity(self, pool: str, token_a: str, token_b: str, amount_a: float, amount_b: float):
        if self.portfolio.get(token_a, 0) < amount_a or self.portfolio.get(token_b, 0) < amount_b:
            print(f"Insufficient balance to provide liquidity with {amount_a} {token_a} and {amount_b} {token_b}.")
            return False
        print(f"Providing liquidity to {pool} with {amount_a} {token_a} and {amount_b} {token_b}.")
        self.portfolio[token_a] -= amount_a
        self.portfolio[token_b] -= amount_b
        return True

    def rebalance_portfolio(self):
        print("Rebalancing portfolio...")
        target_allocations = self._get_target_allocations()
        total_value = sum(self.portfolio.values())
        for token, target_percentage in target_allocations.items():
            target_value = total_value * target_percentage
            current_value = self.portfolio.get(token, 0)
            if current_value < target_value:
                print(f"Need to acquire {target_value - current_value:.2f} more {token}.")
            elif current_value > target_value:
                print(f"Consider reducing {current_value - target_value:.2f} {token}.")
        return True

    def participate_in_governance(self, proposal_id: str, vote: str):
        print(f"Voting {vote} on proposal {proposal_id}.")
        self.governance_votes[proposal_id] = vote
        return True

    def facilitate_lending_borrowing(self, token: str, amount: float, action: str):
        if action == "lend":
            if token in self.portfolio and self.portfolio[token] >= amount:
                print(f"Lending {amount} {token}.")
                self.portfolio[token] -= amount
                return True
            else:
                print(f"Insufficient {token} balance to lend {amount}.")
                return False
        elif action == "borrow":
            print(f"Borrowing {amount} {token}.")
            self.portfolio[token] = self.portfolio.get(token, 0) + amount
            return True
        else:
            print(f"Invalid action: {action}.")
            return False

    def _get_exchange_rate(self, token_in: str, token_out: str) -> float:
        return np.random.uniform(0.9, 1.1)

    def _get_target_allocations(self) -> Dict[str, float]:
        return {"ETH": 0.5, "BTC": 0.3, "USDC": 0.2}

# Testing the corrected program
def main():
    agent = DeFiAgent(wallet_address="0xABCDEF123456")
    agent.portfolio = {"ETH": 5, "BTC": 2, "USDC": 1000}

    # Perform actions and test functionality
    agent.transact(token="ETH", amount=0.5, recipient="0x123456789ABC")
    agent.swap_tokens(token_in="USDC", token_out="ETH", amount_in=500)
    agent.provide_liquidity(pool="ETH-USDC", token_a="ETH", token_b="USDC", amount_a=1, amount_b=500)
    agent.rebalance_portfolio()
    agent.participate_in_governance(proposal_id="123", vote="YES")
    agent.facilitate_lending_borrowing(token="BTC", amount=1, action="lend")

main()
