#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Flask server
"""

import os
from flask import Flask, jsonify, request
import json
import datetime as date
from pprint import pprint

from pyblock import Block
from pychain import Blockchain
from transaction import Transaction
from pynode import Node
import wallet

app = Flask(__name__)

# A completely random address of the owner of this node
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

node = Node(miner_address)

# 创建一个交易并添加到区块
@app.route('/transaction/new', methods=['POST'])
def transaction():
    # On each new POST request, we extract the transaction data
    values = request.get_json()
    required = ['from', 'to', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Then we add the transaction to our list
    #new_txion = Transaction(values['from'], values['to'], values['amount'])
    new_txion = values
    node.add_transaction(new_txion) # add json directly

    response = {'message': 'Transaction submitted successfully'}
    return jsonify(response), 200


# 返回整个区块链. 读取自己节点的 chain, 暴露给其他节点用以更新
@app.route('/chain', methods=['GET'])
def get_blocks():
    chain = node.blockchain.get_blocks()
    response = {
        'chain': chain,
        'length': len(chain),
    }
    return jsonify(response), 200


# 告诉服务器去挖掘新的一个区块
@app.route('/mine', methods=['GET'])
def mine():
    mined_block = node.mine()
    # Let the client know we mined a block
    response = mined_block.json()
    return jsonify(response), 200


# 返回所有的邻居节点
@app.route('/nodes/', methods=['GET'])
def get_nodes():
    response = {
        "nodes": node.peer_nodes
    }
    return jsonify(response), 200

# 添加一个新的邻居节点, 接收 URL 形式的新节点列表
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


@app.route('/', methods = ['GET'])
def hello():
    response = {'message': 'welcome to pychain!'}
    return jsonify(response), 200

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    # from argparse import ArgumentParser
    #
    # parser = ArgumentParser()
    # parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    # args = parser.parse_args()
    # port = args.port
    #
    # app.run(host='127.0.0.1', port=port, debug=True)
