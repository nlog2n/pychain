#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri July 6 10:48:12 2018
@author: nlog2n

  Wallets generation using Public/Private key encryption (based on RSA algorithm)

"""

import binascii

# require package: pycrypto

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def new_wallet():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()

    result = {
        'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
        'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    }

    return result