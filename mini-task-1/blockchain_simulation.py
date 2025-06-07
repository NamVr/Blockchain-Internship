# Objective: Block Simulation in Code 
# Build a basic blockchain with 3 limited blocks using code.

import hashlib
import datetime

# Block class definition
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                          # Block number
        self.timestamp = timestamp                  # When block was created
        self.data = data                            # Transaction or data in block
        self.previous_hash = previous_hash          # Hash of the previous block
        self.nonce = 0                              # Used later for mining (not used here yet)
        self.hash = self.calculate_hash()           # Current block's hash

    def calculate_hash(self):
        # Combine block content into a single string and return its SHA-256 hash
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        # Neat string representation for printing
        return f"Block {self.index}:\n  Timestamp: {self.timestamp}\n  Data: {self.data}\n  Prev Hash: {self.previous_hash}\n  Hash: {self.hash}\n"

# Function to create the blockchain with 3 blocks
def create_blockchain():
    blockchain = []

    # Genesis block
    genesis_block = Block(0, datetime.datetime.now(), "Genesis Block", "0")
    blockchain.append(genesis_block)

    # Add second and third blocks, linking with previous block hash
    block1 = Block(1, datetime.datetime.now(), "Transaction: Alice → Bob", genesis_block.hash)
    blockchain.append(block1)

    block2 = Block(2, datetime.datetime.now(), "Transaction: Bob → Charlie", block1.hash)
    blockchain.append(block2)

    return blockchain

# Function to display the full blockchain
def display_blockchain(chain):
    print("📦 Blockchain Structure:\n")
    for block in chain:
        print(block)

# Function to check integrity (chain validation)
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]

        # Check if current block's hash is correct
        if current.hash != current.calculate_hash():
            return False

        # Check if current block's previous_hash matches previous block's hash
        if current.previous_hash != previous.hash:
            return False

    return True

# ---- MAIN LOGIC ----

# Step 1: Create blockchain with 3 blocks
blockchain = create_blockchain()

# Step 2: Display original blockchain
display_blockchain(blockchain)

# Step 3: Validate original blockchain
print("✅ Is blockchain valid?", is_chain_valid(blockchain))

##########################################################

# ---- CHALLENGE: Tamper with Block 1 ----
print("\n⚠️ Tampering with Block 1's data...\n")
blockchain[1].data = "Transaction: Alice → Eve"  # Changing data
blockchain[1].hash = blockchain[1].calculate_hash()  # Recalculate hash only for Block 1

# Step 4: Display tampered blockchain
display_blockchain(blockchain)

# Step 5: Revalidate chain
print("❌ Is blockchain valid after tampering?", is_chain_valid(blockchain))
