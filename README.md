
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


## API Access

### Add new transaction

`$ curl "localhost:8000/transaction/new"      -H "Content-Type: application/json"      -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'`

```
Transaction submission successful
```

### Mining

`$ curl localhost:8000/mine`

```
{
    "data": {
        "proof-of-work": 29543,
        "transactions": [
            {
                "amount": 3,
                "from": "akjflw",
                "to": "fjlakdj"
            },
            {
                "amount": 1,
                "from": "network",
                "to": "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
            }
        ]
    },
    "hash": "e334ace39593e6d9c1d8b2720229334e7e1a4bf52d048324026ce64b3d8fcce8",
    "index": 1,
    "previous_hash": "a3dc0ee35424c60377966cbc8604890d042be2070303a329a4946f02c1ee689d",
    "timestamp": "2018-07-05 18:15:28.362631"
}
```

## Show full chain

`$ curl localhost:8000/chain`

```
{
    "chain": [
        {
            "data": {
                "proof-of-work": 9,
                "transactions": null
            },
            "hash": "a3dc0ee35424c60377966cbc8604890d042be2070303a329a4946f02c1ee689d",
            "index": 0,
            "previous_hash": "0",
            "timestamp": "2018-07-05 18:14:53.258656"
        },
        {
            "data": {
                "proof-of-work": 29543,
                "transactions": [
                    {
                        "amount": 3,
                        "from": "akjflw",
                        "to": "fjlakdj"
                    },
                    {
                        "amount": 1,
                        "from": "network",
                        "to": "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
                    }
                ]
            },
            "hash": "e334ace39593e6d9c1d8b2720229334e7e1a4bf52d048324026ce64b3d8fcce8",
            "index": 1,
            "previous_hash": "a3dc0ee35424c60377966cbc8604890d042be2070303a329a4946f02c1ee689d",
            "timestamp": "2018-07-05 18:15:28.362631"
        }
    ],
    "length": 2
}
```