#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri July 6 10:48:12 2018
@author: nlog2n

  Wallets generation using Public/Private key encryption (based on RSA algorithm)

"""

import binascii
import json

# require package: pycrypto

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



class Wallet():

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def json(self):
        return {
            'private_key': self.private_key,
            'public_key': self.public_key
        }

    def __str__(self):
        return json.dumps(self.json())


def new_wallet():
    # generate a random key pair
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()

    # convert to string format
    private_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    public_key = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')

    wallet = Wallet()
    wallet.private_key, wallet.public_key = private_key, public_key

    return wallet