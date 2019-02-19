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

from model.pyblock import Block
from model.pychain import Blockchain
from model.pywallet import Wallet
import pow


class Node:

    def __init__(self, miner_address=None):
        # This node's blockchain copy
        self.blockchain = Blockchain()

        # A variable to deciding if we're mining or not
        self.mining = True
        self.miner_address = miner_address

        # wallet for this node
        self.this_node_wallet = Wallet()

        # Store the transactions that
        # this node has in a list
        self.this_nodes_transactions = []

        # Store the url data of every other node in the network
        # so that we can communicate with them
        self.peer_nodes = []

    def register_nodes(self, neighbors):
        self.peer_nodes.append(neighbors)

    def consensus(self):
        """
        Resolve conflicts between blockchain's nodes
        by replacing our chain with the longest one in the network.
        """
        changed = False

        # Get the blockchains of every other node
        other_chains = []
        for node_url in self.peer_nodes:
            try:
                # Get their chains using a GET request
                chainOne = requests.get(node_url + "/pychain/api/v1/transaction/chain").content
                # Convert the JSON object to a Python dictionary
                chainOne = json.loads(chainOne)
                # Add it to our list
                other_chains.append(chainOne)
            except Exception as ex:
                print "probing node failed: " + str(node_url)
                # TODO: remove this node_url from my peer_nodes?

        # If our chain isn't longest, then we store the longest chain
        longest_chain = self.blockchain.chain
        for chain in other_chains:
            chain = chain["chain"]
            cc = Blockchain()
            cc.from_json(chain)
            chain = cc.chain

            if len(longest_chain) < len(chain):
                ## TODO: 这里还需要validate other chain data
                longest_chain = chain
                changed = True

        # If the longest chain isn't ours,
        # then we stop mining and set
        # our chain to the longest one
        self.blockchain.chain = longest_chain
        return changed

    def add_transaction(self, new_transaction):
        # add the transaction to our list
        self.this_nodes_transactions.append(new_transaction)
        return True

    def get_transactions(self):
        return self.this_nodes_transactions

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
        new_block_timestamp = date.datetime.now()
        last_block_hash = last_block.hash

        # 现在创建一个新的block
        mined_block = Block(
            new_block_index,
            new_block_timestamp,
            new_block_data,
            last_block_hash
        )
        self.blockchain.chain.append(mined_block)

        # 既然将本地所有transactions添加到block, 让我们清空本地transaction list
        self.this_nodes_transactions[:] = []

        return mined_block
