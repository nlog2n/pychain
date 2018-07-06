#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Proof of Work
  PoW算法，规则是：寻找一个数 p，使得它与前一个区块的 proof 拼接成的字符串的 Hash 值以 4 个零开头
"""

import hashlib
import json
from time import time
from uuid import uuid4


def valid_proof(last_proof, proof):
    """
    验证证明: 是否hash(last_proof, proof)以4个0开头?
    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :return: <bool> True if correct, False if not.
    """
    guess = '{0}{1}'.format(last_proof, proof).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


def proof_of_work(last_proof):
    """
    简单的工作量证明:
     - 查找一个 p' 使得 hash(pp') 以4个0开头
     - p 是上一个块的证明,  p' 是当前的证明
    :param last_proof: <int>
    :return: <int>
    """
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1
    return proof
