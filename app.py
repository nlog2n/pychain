#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Flask server
"""


from flask import Flask
from flask import request
import json
import requests
import datetime as date
from pprint import pprint

from pyblock import Block
from pychain import Blockchain
from pynode import Node

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
  print "FROM: {}".format(new_txion['from'].encode('ascii','replace'))
  print "TO: {}".format(new_txion['to'].encode('ascii','replace'))
  print "AMOUNT: {}\n".format(new_txion['amount'])
  # Then we let the client know it worked out
  return "Transaction submission successful\n"

@app.route('/chain', methods=['GET'])
def get_blocks():
  return node.blockchain.get_blocks()

@app.route('/mine', methods = ['GET'])
def mine():
  mined_block = node.mine()
  # Let the client know we mined a block
  return str(mined_block)

if __name__ == '__main__':
  app.run(debug=True, port=8000)

