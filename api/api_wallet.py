#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, Blueprint, current_app, request
from flask_cors import cross_origin

from model import pywallet

apiWallet = Blueprint('wallet', __name__, url_prefix='/pychain/api/v1/wallet')


@apiWallet.route('/new', methods=['GET'])
@cross_origin()
#@jwt_required
def new_wallet():
    """
    创建一个新的钱包秘药，并挂到当前node下面
    :return:
    """
    wallet = pywallet.new_wallet()

    node = current_app.config["PYCHAIN_NODE"]
    node.this_node_wallet = wallet

    response = wallet.json()
    return jsonify(response), 200


@apiWallet.route('', methods=['GET'])
@cross_origin()
def get_wallet():
    """
    读取当前node挂在下面的钱包秘药
    :return:
    """
    node = current_app.config["PYCHAIN_NODE"]

    wallet = node.this_node_wallet
    response = wallet.json()

    return jsonify(response), 200

