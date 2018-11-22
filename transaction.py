#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri July 6 10:48:12 2018
@author: nlog2n

  Transaction in Pychain
"""

from collections import OrderedDict

import binascii
import json

# require package: pycrypto

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Transaction:
    """
        定义Transaction, 包含发送方地址，接受方地址，和金额
    """

    def __init__(self, sender_address, receiver_address, value):
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.value = value

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'from': self.sender_address,
                            'to': self.receiver_address,
                            'amount': self.value})

    def json(self):
        return {
            'from': self.sender_address,
            'to': self.receiver_address,
            'amount': self.value
        }

    def __str__(self):
        return json.dumps(self.json())

    def sign_transaction(self, sender_private_key):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')