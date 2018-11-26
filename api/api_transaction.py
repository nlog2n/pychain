#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request, jsonify, Blueprint, current_app
from flask_cors import cross_origin

from flask_jwt_extended import (
    jwt_required
)


#from model.transaction import Transaction

apiTransaction = Blueprint('transaction', __name__, url_prefix='/pychain/api/v1/transaction')

# 创建一个交易并添加到区块
@apiTransaction.route('', methods=['POST'])
@cross_origin()
#@jwt_required
def transaction():
    # On each new POST request, we extract the transaction data
    values = request.get_json()
    if values is None:
        values = request.form

    required = ['from', 'to', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # TODO: 新的交易必须提供签名或者发送者私钥（代为签名)
    # xxx = ['signature', 'sender_private_key']
    # if not any(k in values for k in xxx):
    #     return 'transaction signature or sender_private_key must be provided', 400
    #
    # new_txion = Transaction(values['from'], values['to'], values['amount'])

    # Then we add the transaction to our list
    new_txion = values
    node = current_app.config["PYCHAIN_NODE"]
    node.add_transaction(new_txion) # add json directly

    response = {
        "transaction": {
            "from": new_txion['from'],
            "to": new_txion['to'],
            "amount": new_txion['amount']
        },
        "signature": "to be computed",
        'message': 'Transaction submitted successfully'
    }
    return jsonify(response), 200

# 显示该节点上那些等待加到区块的交易
@apiTransaction.route('', methods=['GET'])
@cross_origin()
#@jwt_required
def get_transactions():
    node = current_app.config["PYCHAIN_NODE"]
    #Get transactions from transactions pool of the node
    transactions = node.get_transactions()
    response = {'transactions': transactions}
    return jsonify(response), 200



# 返回整个区块链. 读取自己节点的 chain, 暴露给其他节点用以更新
@apiTransaction.route('/chain', methods=['GET'])
@cross_origin()
#@jwt_required
def get_blocks():
    node = current_app.config["PYCHAIN_NODE"]
    chain = node.blockchain.get_blocks()
    response = {
        'chain': chain,
        'length': len(chain),
    }
    return jsonify(response), 200


# 告诉服务器去挖掘新的一个区块
@apiTransaction.route('/mine', methods=['GET'])
@cross_origin()
#@jwt_required
def mine():
    node = current_app.config["PYCHAIN_NODE"]
    mined_block = node.mine()
    # Let the client know we mined a block
    response = mined_block.json()
    return jsonify(response), 200
