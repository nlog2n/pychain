#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Chain structure
"""

import datetime as date

from model.pyblock import Block


class Blockchain(object):
    """
        Blockchain 类负责管理链式数据，它会添加新的区块到链式数据, 查询所有区块，最后一个区块
    """

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

    def json(self):
        chain_to_send = []
        # Convert our blocks into dictionaries
        # so we can send them as json objects later
        for i in range(len(self.chain)):
            block = self.chain[i]
            b = block.json()
            chain_to_send.append(b)

        return chain_to_send

    def from_json(self, j):
        chain = []
        for i in range(len(j)):
            block = Block()
            block.from_json(j[i])
            chain.append(block)

        self.chain = chain

    @property
    def last_block(self):
        return self.chain[-1]
