#Blockchain Code
import json
from time import time
from hashlib import sha256
from textwrap import dedent
from uuid import uuid4

from flask import flask


class BlockChain(object):
    def __init__(self):
        #Initialize the blockchain
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)
    
    def new_block(self,proof, previous_hash=None):
        #Create a new block and add it to the chain
        block = {'index':len(self.chain) + 1, 
                 'timestamp':time(),
                 'transactions':self.current_transactions,
                 'proof':proof,
                 'previous_hash':previous_hash or self.hash(self.chain[-1]),
                }
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recepient, amount):
        #Create a new Transaction to the list of transactions
        self.current_transactions.append({'sender':sender, 'recepient':recepient, 'amount':amount})
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        #Hash a block
        block_string = json.dumps(block,sort_keys=true).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def last_block(self):
        #Returns the last block in a chain
        return self.chain[-1]
    
    def proof_of_work(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof) is false:
            proof += 1
            
        return proof
    
    @staticmethod
    def valid_proof(lastproof,proof):
        guess=f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
#Instantiate Blockchain Code
    
blockchain = BlockChain()
