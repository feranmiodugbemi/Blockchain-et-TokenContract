# Mini Blockchain with python

### Questions

1. Provide Test Cases for Implemented Blockchain
2. Document Design choice of Blockchain
3. Explain the poW and Consensus mechanism 


### Answer
1. **Below is an example on how the blockchain works**
 ```python
 # Example usage
blockchain = Blockchain()

# Create transaction 1, adds ransaction to the pending transaction list on the blockchain, lastly mines the transaction
transactsion1 = "Ali sends 2 coins to Ola"
blockchain.create_transaction(transaction1)
blockchain.mine_pending_transactions("Ali")

# Create transaction 2, adds ransaction to the pending transaction list on the blockchain, lastly mines the transaction
transaction2 = "Bolu sends 1 coin to Ayo"
blockchain.create_transaction(transaction2)
blockchain.mine_pending_transactions("Bolu")

# Create transaction 3 and 4 in the same block, adds ransaction to the pending transaction list on the blockchain, lastly mines the transaction
transaction3 = "Dammy sends 1 coin to Ayo"
transaction4 = "Feranmi Sends 20 coins to dola"
blockchain.create_transaction(transaction3)
blockchain.create_transaction(transaction4)
blockchain.mine_pending_transactions("Dammy, Feranmi")

 ```
*The Example usage are commented in the python code above.*


2. **Document Design choice of Blockhain** 

    1. Block Structure:

        - Each block in the blockchain consists of an index (block number), a list of transactions, the hash of the previous block, a nonce (a number used for PoW mining), and a timestamp.
        - The hash of the block is calculated based on the combination of these properties using the SHA-256 hashing algorithm.


    2. Blockchain Structure:

        - The blockchain is implemented as a list of blocks, with the first block being the genesis block (block with index 0, no transactions, and a predefined hash).
        - Each subsequent block is linked to the previous block through the inclusion of the previous block's hash, forming an immutable chain of blocks.


    3. Consensus Mechanism:

        - The chosen consensus mechanism is Proof-of-Work (PoW), which is a widely used mechanism in many blockchain systems, including Bitcoin.


    4. Mining Process:

        - New blocks are added to the blockchain through a mining process, which involves solving a computationally intensive puzzle (PoW).
        - The mining difficulty is adjustable by setting the required number of leading zeros in the block hash.


    5. Transaction Management:

        - Transactions are stored in a pending list before being included in a new block.
        - Once a block is mined, the pending transactions are added to the block, and the pending list is cleared.

3. **PoW consensus mechanism:**
    The PoW consensus mechanism is a core component of the blockchain implementation and is responsible for ensuring the integrity and security of the blockchain. Here's how it works:

    1. Mining Process:

        - When a new block needs to be added to the blockchain, miners (nodes in the network) compete to solve a complex mathematical puzzle.
        - The puzzle involves finding a nonce value that, when combined with the block data (transactions, previous hash, etc.), produces a hash that starts with a certain number of leading zeros (the difficulty level).


    2. Difficulty Adjustment:

        - The difficulty level determines how many leading zeros are required in the block hash.
        - A higher difficulty level means more leading zeros are required, making the puzzle more computationally intensive to solve.
        - The difficulty can be adjusted to control the rate at which new blocks are added to the blockchain.


    3. Consensus and Validity:

        - The first miner to solve the puzzle and broadcast the valid block to the network is rewarded (e.g., with cryptocurrency in the case of Bitcoin).
        - Other nodes in the network can easily verify the validity of the new block by checking that the block's hash meets the difficulty requirement and that the block is correctly linked to the previous block.
        - Once a valid block is accepted by the majority of nodes, it is added to the blockchain, and the mining process starts again for the next block.


    4. Security and Immutability:

        - PoW ensures that it is computationally expensive to modify or tamper with existing blocks in the blockchain, as doing so would require recalculating the PoW for all subsequent blocks, which is computationally infeasible.
        - This computational effort, combined with the distributed nature of the blockchain network, makes it extremely difficult for a single entity to gain control or manipulate the blockchain.

