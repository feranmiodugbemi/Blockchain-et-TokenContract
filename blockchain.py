import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.transactions) + str(self.previous_hash) + str(self.nonce) + str(self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while True:
            if str(self.hash)[:difficulty] == '0' * difficulty:
                break
            self.nonce += 1
            self.hash = self.calculate_hash()
        
    


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = []
        return True

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        return self.get_latest_block().index + 1

    def get_chain(self):
        return self.chain

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def get_previous_hash(self):
        return self.get_latest_block().previous_hash

    def get_blockchain_data(self):
        blockchain = []
        for block in self.get_chain():
            b = {
                "index" : block.index,
                "transaction" : block.transactions,
                "nonce" : block.nonce,
                "time" : block.timestamp,
                "hash" : block.hash
            }
            
            blockchain.append(b)

        return blockchain


    

# Example usage
blockchain = Blockchain()

# Create transaction 1, add ransaction to pending transaction list, mine transaction
transaction1 = "Ali sends 2 coins to Ola"
blockchain.create_transaction(transaction1)
blockchain.mine_pending_transactions("Ali")

# Create transaction 2, add ransaction to pending transaction list, mine transaction
transaction2 = "Bolu sends 1 coin to Ayo"
blockchain.create_transaction(transaction2)
blockchain.mine_pending_transactions("Bolu")

# Create transaction 3 and 4 in the same block, add ransaction to pending transaction list, mine transaction
transaction3 = "Dammy sends 1 coin to Ayo"
transaction4 = "Feranmi Sends 20 coins to dola"
blockchain.create_transaction(transaction3)
blockchain.create_transaction(transaction4)
blockchain.mine_pending_transactions("Dammy, Feranmi")


#Print the blockchain
print(blockchain.get_blockchain_data())