
# A tiny blockchain implementation in Python

## Introduction

A tiny Blockchain implementation in python, currently supporting 
 - new transaction
 - coin mining
 - proof of work
 - longest chain consensus
 - RestAPI access

## Quick Start

The node was implemented with Flask server, and can be launched via command:
`$ python app.py`


```
$ curl localhost:8000/chain
[{"index": "0", "data": "{'transactions': None, 'proof-of-work': 9}", "hash": "76750048d1e6e679884cba9972785296bcb999c9de685c17f14e52e94b19bdbf", "timestamp": "2018-07-05 16:10:08.239959"}, {"index": "1", "data": "{'transactions': [{'to': 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi', 'amount': 1, 'from': 'network'}], 'proof-of-work': 18}", "hash": "a3a58eba0451bf94561e62a977375b78b3b6c7cf88abcc9a14d7755ec8a35cb3", "timestamp": "2018-07-05 16:10:11.593699"}]
```

```
$ curl "localhost:8000/transaction/new"      -H "Content-Type: application/json"      -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'
Transaction submission successful
```

```
$ curl localhost:8000/mine
{"index": 2, "previous_hash": "a3a58eba0451bf94561e62a977375b78b3b6c7cf88abcc9a14d7755ec8a35cb3", "data": {"transactions": [{"to": "fjlakdj", "amount": 3, "from": "akjflw"}, {"to": "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi", "amount": 1, "from": "network"}], "proof-of-work": 36}, "hash": "e99258e598f93b1a1fb9daceff07148f0e44313653c3b8bf0c6c665e58416257", "timestamp": "2018-07-05 16:10:39.716661"}
```

```
$ curl localhost:8000/chain
[{"index": "0", "data": "{'transactions': None, 'proof-of-work': 9}", "hash": "76750048d1e6e679884cba9972785296bcb999c9de685c17f14e52e94b19bdbf", "timestamp": "2018-07-05 16:10:08.239959"}, {"index": "1", "data": "{'transactions': [{'to': 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi', 'amount': 1, 'from': 'network'}], 'proof-of-work': 18}", "hash": "a3a58eba0451bf94561e62a977375b78b3b6c7cf88abcc9a14d7755ec8a35cb3", "timestamp": "2018-07-05 16:10:11.593699"}, {"index": "2", "data": "{'transactions': [{u'to': u'fjlakdj', u'amount': 3, u'from': u'akjflw'}, {'to': 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi', 'amount': 1, 'from': 'network'}], 'proof-of-work': 36}", "hash": "e99258e598f93b1a1fb9daceff07148f0e44313653c3b8bf0c6c665e58416257", "timestamp": "2018-07-05 16:10:39.716661"}]
```