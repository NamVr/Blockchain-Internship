# Task 2: Submitted by Naman Vrati

This task compares three different types of blockchain platforms — one each from public, private, and consortium categories.

---

## 1. Comparison Table

| Feature                     | Ethereum (Public)           | Hyperledger Fabric (Private)     | Quorum (Consortium)               |
|-----------------------------|-----------------------------|----------------------------------|-----------------------------------|
| **Consensus Mechanism**     | Proof of Stake (Casper)     | Pluggable (default: Raft)        | Istanbul BFT, Raft                |
| **Permission Model**        | Open                        | Permissioned                     | Permissioned                      |
| **Speed / Throughput**      | 15–30 TPS                   | 3,000+ TPS                       | 100–200 TPS                       |
| **Smart Contract Support**  | Yes (Solidity)              | Yes (Go, JavaScript)             | Yes (Solidity)                    |
| **Token Support**           | Native (ETH)                | No                               | Optional                          |
| **Typical Use Case**        | Decentralized Applications  | Supply Chains, Private Networks  | Financial Transactions, Voting    |
| **Notable Technical Feature** | EVM, High Decentralization | Channel-based privacy, Modular   | Private Transactions, Ethereum-based |

---

## 2. Comparative Summary

Ethereum, Hyperledger Fabric, and Quorum each serve different needs in the blockchain world.

**Ethereum** is a fully public blockchain and great for building open decentralized applications. It has a massive developer community and supports powerful smart contracts via Solidity. But, it’s not the fastest — processing around 15–30 transactions per second — so it may not suit use cases needing high speed.

**Hyperledger Fabric** is more suited for private, enterprise-level projects. It’s permissioned, highly modular, and performs much faster (thousands of TPS). It doesn’t support tokens by default, but its strengths lie in privacy and flexible architecture, like using channels for confidential communication.

**Quorum**, on the other hand, blends the two worlds. It’s based on Ethereum but tailored for consortium use — like in finance or voting systems between known organizations. It supports private smart contracts and allows you to choose between consensus types like Raft or Istanbul BFT.

### 2.1 Platform Recommendations:
- **Decentralized App**: Go with **Ethereum** for openness and ecosystem support  
- **Supply Chain (Known Partners)**: Choose **Hyperledger Fabric** for privacy and performance  
- **Inter-bank Finance App**: Use **Quorum** for its Ethereum-compatibility and private transaction support  

---

Task - 2 | Submitted by Naman Vrati | info@namanvrati.me
