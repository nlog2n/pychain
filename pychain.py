#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Chain structure
"""

import json
import hashlib as hasher
import datetime as date
from pprint import pprint

from pyblock import Block

class Blockchain(object):

  def __init__(self):
    self.chain = []
    block0 = Blockchain.create_genesis_block()
    self.chain.append(block0)

  # Generate genesis block
  @staticmethod
  def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, 
      date.datetime.now(), 
      {
      "proof-of-work": 9,
      "transactions": None
      }, 
      "0")

  def get_blocks(self):
    chain_to_send = []
    # Convert our blocks into dictionaries
    # so we can send them as json objects later
    for i in range(len(self.chain)):
      block = self.chain[i]
      block_index = str(block.index)
      block_timestamp = str(block.timestamp)
      block_data = str(block.data)
      block_hash = block.hash

      b = {
        "index": block_index,
        "timestamp": block_timestamp,
        "data": block_data,
        "hash": block_hash
      }
      chain_to_send.append(b)

    return json.dumps(chain_to_send)


  @property
  def last_block(self):
    return self.chain[-1]