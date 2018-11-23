#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Block def
"""

import json
import hashlib as hasher
import datetime as date


# Define block
class Block():
    """
        定义区块链中每一个区块
        每个块都有一个 索引，一个 时间戳（Unix时间戳），一个事务列表， 一个校验(稍后详述) 和 前一个块的散列 。
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data # 包含 transactions, proof-of-work
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()

    def json(self):
        return {
            "index": self.index,
            "timestamp": str(self.timestamp),
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    def __str__(self):
        return json.dumps(self.json())
