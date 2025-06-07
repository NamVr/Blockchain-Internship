import random

# ----- MOCK SETUP: Validators -----

# Simulate a miner for PoW with random "computational power"
miner = {
    "name": "Miner_1",
    "power": random.randint(50, 100)  # Higher power = more likely to win PoW
}

# Simulate a staker for PoS with random "coin stake"
staker = {
    "name": "Staker_1",
    "stake": random.randint(50, 100)  # Higher stake = more likely to be selected
}

# Simulate 3 voters voting in DPoS
voters = {
    "voter_1": "Validator_A",
    "voter_2": "Validator_B",
    "voter_3": "Validator_A"
}
# Count votes to find the most voted delegate
vote_counts = {}
for vote in voters.values():
    vote_counts[vote] = vote_counts.get(vote, 0) + 1

# -----------------------
# PROOF OF WORK SIMULATION
# -----------------------
print("Proof of Work (PoW) Simulation")
print(f"{miner['name']} has computational power: {miner['power']}")
print("In PoW, the miner with the highest computational power gets to validate the block.")
print(f"Selected Validator: {miner['name']} (based on highest power)\n")

# -----------------------
# PROOF OF STAKE SIMULATION
# -----------------------
print("Proof of Stake (PoS) Simulation")
print(f"{staker['name']} has staked coins: {staker['stake']}")
print("In PoS, the validator with the most stake gets to validate the block.")
print(f"Selected Validator: {staker['name']} (based on highest stake)\n")

# -----------------------
# DELEGATED PROOF OF STAKE SIMULATION
# -----------------------
print("Delegated Proof of Stake (DPoS) Simulation")
print("Votes from users:", voters)
print("In DPoS, token holders vote for delegates who validate blocks.")

# Find the validator with the highest number of votes
most_voted = max(vote_counts, key=vote_counts.get)
print(f"Selected Delegate: {most_voted} (based on most votes)")
print(f"Vote Count: {vote_counts}\n")
