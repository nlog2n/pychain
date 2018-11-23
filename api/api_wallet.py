#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, Blueprint
from flask_cors import cross_origin

from model import pywallet

apiWallet = Blueprint('wallet', __name__, url_prefix='/pychain/api/v1/wallet')


@apiWallet.route('/new', methods=['GET'])
@cross_origin()
#@jwt_required
def new_wallet():
    response = pywallet.new_wallet()
    return jsonify(response), 200
