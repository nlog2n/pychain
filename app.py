#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on June 26 09:48:12 2018
@author: nlog2n

  Flask server
"""

import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from model.pynode import Node

app = Flask(__name__)
CORS(app)

# 将这个flask app作为一个区块链节点
# A completely random address of the owner of this node
miner_address = "node-as-miner-address-nlog2n"
node = Node(miner_address)

app.config["PYCHAIN_NODE"] = node


# register blueprints
from api.api_node import apiNode
from api.api_transaction import apiTransaction
from api.api_wallet import apiWallet
app.register_blueprint(apiNode)
app.register_blueprint(apiTransaction)
app.register_blueprint(apiWallet)


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/configure')
def configure():
    return render_template('./configure.html')


@app.route('/ping', methods=['GET'])
def hello():
    response = {'message': 'welcome to pychain!'}
    return jsonify(response), 200


if __name__=='__main__':

    # 从命令行获取端口
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=-1, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    # 如果命令行未声明，则从环境变量读取端口。缺省 5000
    if port == -1:
        port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
