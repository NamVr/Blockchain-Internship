# Mini Task 1: Submitted by Naman Vrati

## 1. Blockchain Basics
### Q: Define blockchain in your own words (100–150 words).

A blockchain is a **distributed**, **digital ledger** that stores data across multiple computers/systems in a **decentralized** manner. Each record, known as a block, contains a set of transactions or data, a timestamp, a unique hash, and a reference to the hash of the previous block, forming a secure and **immutable** chain.
The decentralized nature means no single entity controls the entire system, enhancing **transparency** and **trust**. Any attempt to alter data in one block would require changing all subsequent blocks, which is computationally infeasible.
Blockchain operates through **consensus mechanisms** like Proof of Work or Proof of Stake to ensure validity. It’s most commonly known as the backbone of cryptocurrencies, but its core principles extend far beyond finance.

### Q: List 2 real-life use cases of blockchain.

1. **Secured Voting Systems**
Blockchain can be used to create transparent and secure electronic voting platforms. It ensures that once a vote is cast, it cannot be altered or deleted, reducing the risk of fraud and increasing trust in electoral processes. For instance, countries like Sierra Leone and pilot projects in Utah County, USA have explored blockchain-based voting to enhance transparency and accessibility, especially for remote voters.

2. **Intellectual Property Protection**
Artists, musicians, and creators can use blockchain to timestamp and register their works, proving ownership and originality. Platforms like Audius and Ascribe allow content creators to distribute digital art or music directly, while protecting against unauthorized reproduction through immutable proof of creation and transfer.

---

## 2. Blockchain Anatomy
### Q: Draw a block showing — data, previous hash, timestamp, nonce and Merkle root.

![](https://raw.githubusercontent.com/NamVr/Blockchain-Internship/refs/heads/master/mini-task-1/merkle%20tree%20blockchain.png#_uDarkdata-hpc=true&class=Box-sc-g0xbh4-0+fzFXnm)

### Q: Explain with an example how the Merkle root helps verify data integrity.

The **Merkle root** is the **top hash** of a **binary tree structure** where each leaf node represents a transaction hash, and each non-leaf node is a hash of its children. This allows quick verification of whether a specific transaction exists in the block without revealing the full dataset.

**Example**: Suppose a block has 4 transactions: T1, T2, T3, and T4. Their individual hashes are combined pairwise:
```bash
H1 = hash(T1), H2 = hash(T2) → H12 = hash(H1 + H2)
H3 = hash(T3), H4 = hash(T4) → H34 = hash(H3 + H4)
Merkle Root = hash(H12 + H34)
```

If someone tampers with T3, its hash changes, which affects H34 and ultimately changes the Merkle root. This way, **any change in transaction data can be efficiently detected**, securing the integrity of the block.

---

## 3. Consensus Conceptualization

### Q: What is Proof of Work and why does it require energy?

**Proof of Work (PoW)** is a consensus mechanism where **miners compete to solve complex mathematical puzzles using computational power**. The first miner to find a valid solution gets to add the next block to the blockchain and earns a reward. This process ensures that adding a block is resource-intensive, deterring spam and tampering. The **reason** it requires so much energy is that miners use powerful hardware to perform millions of hash calculations per second, consuming large amounts of electricity. This high energy cost is what makes PoW secure—but also criticized for its environmental impact.

### Q: What is Proof of Stake and how does it differ?

**Proof of Stake (PoS)** selects validators based on the number of coins they hold and are willing to *“stake”* or lock up as **collateral**. Instead of mining, validators are chosen pseudo-randomly to propose or validate new blocks, depending on their stake size. **This method consumes significantly less energy than PoW because it doesn't require intense computation**. It also incentivizes good behavior—if a validator tries to cheat, they risk losing their stake. Unlike PoW, PoS rewards participants for wealth (stake) rather than computation power.

### Q: What is Delegated Proof of Stake and how are validators selected?

**Delegated Proof of Stake (DPoS)** is a variation of PoS where coin holders vote to **elect** a small number of trusted delegates (or validators) to create and validate blocks. Each holder’s vote is **weighted** by the amount of stake they hold, and delegates can be re-elected or replaced. This system allows for faster block production and greater scalability while still maintaining decentralization through democratic voting. Validators are selected based on the number of votes they receive, not just their stake. DPoS is used in networks like EOS and Tron.

---

Mini Task - 1 | Submitted by Naman Vrati | info@namanvrati.me
