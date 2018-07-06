#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Node def
"""

import json
import requests
import datetime as date
from pprint import pprint

from pyblock import Block
from pychain import Blockchain
import pow


class Node:

    def __init__(self, miner_address):
        # This node's blockchain copy
        self.blockchain = Blockchain()

        self.miner_address = miner_address
        # A variable to deciding if we're mining or not
        self.mining = True

        # Store the transactions that
        # this node has in a list
        self.this_nodes_transactions = []

        # Store the url data of every
        # other node in the network
        # so that we can communicate
        # with them
        self.peer_nodes = []

    def consensus(self):
        # Get the blockchains of every
        # other node
        other_chains = []
        for node_url in self.peer_nodes:
            # Get their chains using a GET request
            block = requests.get(node_url + "/chain").content
            # Convert the JSON object to a Python dictionary
            block = json.loads(block)
            # Add it to our list
            other_chains.append(block)

        # If our chain isn't longest,
        # then we store the longest chain
        longest_chain = self.blockchain.chain
        for chain in other_chains:
            if len(longest_chain) < len(chain):
                longest_chain = chain
        # If the longest chain isn't ours,
        # then we stop mining and set
        # our chain to the longest one
        self.blockchain.chain = longest_chain

    def add_transaction(self, new_transaction):
        # add the transaction to our list
        self.this_nodes_transactions.append(new_transaction)
        return True

    def mine(self):
        # Get the last proof of work
        last_block = self.blockchain.chain[len(self.blockchain.chain) - 1]
        last_proof = last_block.data['proof-of-work']
        # Find the proof of work for
        # the current block being mined
        # Note: The program will hang here until a new
        #       proof of work is found
        proof = pow.proof_of_work(last_proof)
        # Once we find a valid proof of work,
        # we know we can mine a block so
        # we reward the miner by adding a transaction
        self.this_nodes_transactions.append(
            {"from": "network", "to": self.miner_address, "amount": 1}
        )
        # Now we can gather the data needed
        # to create the new block
        new_block_data = {
            "proof-of-work": proof,
            "transactions": list(self.this_nodes_transactions)
        }
        new_block_index = last_block.index + 1
        new_block_timestamp = this_timestamp = date.datetime.now()
        last_block_hash = last_block.hash

        # Empty transaction list
        self.this_nodes_transactions[:] = []

        # Now create the
        # new block!
        mined_block = Block(
            new_block_index,
            new_block_timestamp,
            new_block_data,
            last_block_hash
        )
        self.blockchain.chain.append(mined_block)

        return mined_block
