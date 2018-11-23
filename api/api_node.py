#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request, jsonify, Blueprint, current_app
from flask_cors import cross_origin

from flask_jwt_extended import (
    jwt_required
)


apiNode = Blueprint('node', __name__, url_prefix='/pychain/api/v1/node')


@apiNode.route('', methods=['GET'])
@cross_origin()
#@jwt_required
def get_nodes():
    """
    返回所有的邻居节点
    :return:
    """
    node = current_app.config["PYCHAIN_NODE"]
    response = {
        "nodes": node.peer_nodes
    }
    return jsonify(response), 200


@apiNode.route('/register', methods=['POST'])
@cross_origin()
#@jwt_required
def register_node():
    """
    添加一个新的邻居节点, 接收 URL 形式的新节点列表
    :return:
    """
    values = request.get_json()
    if values is None:
        values = request.form
        neighbors = values.get('nodes').replace(" ", "").split(',')
    else:
        neighbors = values.get('nodes')

    if neighbors is None:
        return "Error: Please supply a valid list of nodes", 400

    node = current_app.config["PYCHAIN_NODE"]
    for n in neighbors:
        node.register_nodes(n)

    response = {
        'message': 'New neighbors have been added',
        'nodes': node.peer_nodes,
    }
    return jsonify(response), 201


@apiNode.route('/consensus', methods=['GET'])
@cross_origin()
#@jwt_required
def consensus():
    """
    与其他节点同步区块链数据
    :return:
    """
    node = current_app.config["PYCHAIN_NODE"]
    replaced = node.consensus()

    chain = node.blockchain.get_blocks()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': chain
        }
    return jsonify(response), 200
