#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Flask server
"""

from flask import Flask, jsonify, request
import json
import datetime as date
from pprint import pprint

from pyblock import Block
from pychain import Blockchain
from pynode import Node
import wallet

app = Flask(__name__)

# A completely random address of the owner of this node
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

node = Node(miner_address)


@app.route('/transaction/new', methods=['POST'])
def transaction():
    # On each new POST request,
    # we extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    node.add_transaction(new_txion)

    # Because the transaction was successfully
    # submitted, we log it to our console
    print "New transaction"
    print "FROM: {}".format(new_txion['from'].encode('ascii', 'replace'))
    print "TO: {}".format(new_txion['to'].encode('ascii', 'replace'))
    print "AMOUNT: {}\n".format(new_txion['amount'])
    # Then we let the client know it worked out
    return "Transaction submission successful\n"


@app.route('/chain', methods=['GET'])
def get_blocks():
    chain = node.blockchain.get_blocks()
    response = {
        'chain': chain,
        'length': len(chain),
    }
    return jsonify(response), 200


@app.route('/mine', methods=['GET'])
def mine():
    mined_block = node.mine()
    # Let the client know we mined a block
    response = mined_block.json()
    return jsonify(response), 200


@app.route('/nodes/', methods=['GET'])
def get_nodes():
    response = {
        "nodes": node.peer_nodes
    }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    neighbors = values.get('nodes')
    if neighbors is None:
        return "Error: Please supply a valid list of nodes", 400

    for n in neighbors:
        node.register_nodes(n)

    response = {
        'message': 'New neighbors have been added',
        'nodes': node.peer_nodes,
    }
    return jsonify(response), 201


@app.route('/wallet/new', methods=['GET'])
def new_wallet():
    response = wallet.new_wallet()
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
