# Objective: Nonce Mining Simulation
# Simulate Proof of Work by mining a block that satisfies a difficulty condition.

import hashlib         
import datetime       
import time           

# Define a Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # Set block properties when creating a new block
        self.index = index                      # Position in the blockchain
        self.timestamp = timestamp              # When the block was created
        self.data = data                        # The information stored in the block (e.g., a transaction)
        self.previous_hash = previous_hash      # Hash of the previous block
        self.nonce = 0                          # A number that we'll change to try and find a valid hash
        self.hash = self.calculate_hash()       # Calculate initial hash of the block (using nonce = 0)

    def calculate_hash(self):
        # Combine all block information into a single string
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        # Apply SHA-256 to generate a fixed-length 64-character hash
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # This function simulates Proof of Work. Keep changing nonce until the hash starts with `difficulty` number of 0s.
        target = "0" * difficulty  # The required pattern for the hash (e.g., "0000" if difficulty is 4)

        print(f"Mining block with difficulty {difficulty}... (looking for hash starting with {target})\n")

        start_time = time.time()  # Start timer to measure mining time
        attempts = 0              # Counter to track how many nonce values we tried

        # Repeat until the hash starts with the required number of zeroes
        while self.hash[:difficulty] != target:
            self.nonce += 1                       # Try a new nonce
            self.hash = self.calculate_hash()     # Recalculate the hash with the new nonce
            attempts += 1                         # Count this attempt

        end_time = time.time()                    # End timer when valid hash is found
        time_taken = round(end_time - start_time, 4)

        # Print results
        print(f"Block mined successfully!")
        print(f"Final Nonce: {self.nonce}")
        print(f"Valid Hash: {self.hash}")
        print(f"Attempts Made: {attempts}")
        print(f"Time Taken: {time_taken} seconds\n")

# ---- MAIN LOGIC ----

# STEP 1: Create a new block (you can think of this as block #1)
new_block = Block(
    index=1,
    timestamp=datetime.datetime.now(),
    data="Mining simulation data",
    previous_hash="0"  # Usually the hash of the previous block; "0" here for simplicity
)

# STEP 2: Define the mining difficulty (number of zeros at the beginning of the hash)
difficulty = 4  # You can change this to 5 or 6 to increase difficulty

# STEP 3: Start mining the block
new_block.mine_block(difficulty)
