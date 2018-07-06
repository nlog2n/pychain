
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

## Add neighbors


`$ curl "localhost:8000/nodes/register"      -H "Content-Type: application/json"      -d '{"nodes": ["http://localhost:5000"]}'`

```
{
    "message": "New neighbors have been added",
    "nodes": [
        "http://localhost:5000"
    ]
}
```

`$ curl localhost:8000/nodes`

```bash
{
    "nodes": [
        "http://localhost:5000"
    ]
}
```

## Wallet generation

`$ curl localhost:8000/wallet/new`

```bash
{
    "private_key": "3082025c020100028181009bf35a39546fc3bbc11bad35d9a567fd970ec37dfa12e2706c20598d76b32a9e8b44d2d18c0a0b9778cecc6ccff5eac6dd08f0c3f9f9588e62b9ce02017490a23679a9a5787c6a70ca4f219b3a25208398bed8c6858442af4a21a6e8c5f195af6285ef2f15345a3cc60b98a8fcca3b3c48f828b799b71dfd678742c0ec2b92dd02030100010281802272fe523db9b6a62a014020ee2420b59f01cee36c3371bbddd6c391815010b11718abed481f0bf278e84db617b63e1791ca20cd59d1dfe30c21f944ee275eaf6dfdc99c1d57e534dec7552d88178e2d0e05e311b3ec3c696651575c3d24663030a9d7f1a3bebb6e4ed246fd33e004f4c4387936fffce4f39ed9529dd36bef41024100b7ceb07212ac1c9724365c49ababcd80fbf181201743669ec8170071cba79768463dbde88c226da59592baa925fbcc103b481202c1acd5efd4680bf21a14ae31024100d933be1665e6e4bec9cbac35f747e519232d8e1f2777efdbc3826ca5e66b641ae32a23509ed055812247a3f45d75cf16f44a5dfaa757aa0fe085bbb1d651e86d02410098f13f186c391241213caa6612968e14f98ee6a6d134a03b16bb2cff833a1c5e03b47444fff5d5cea63ac55ee1e036d87abb696129ceaae53894aafbf47fa8c1024045c0f7400c33cdac73f423f724d602fe42ace3a29fb345e5a6f120e15a918c9191f8bb64adcc2c598f5fc088bee711bdc67087a3f2d0157e89d58904c0d687350240373555c30e0450f5925dda99a2fbae9018f2080d14e5a6df5f037e9b22c399d56785a0e88e0a7e621d07fcc8702c8981e794b28e31dc30fa275a98b2dbb9a5f5",
    "public_key": "30819f300d06092a864886f70d010101050003818d00308189028181009bf35a39546fc3bbc11bad35d9a567fd970ec37dfa12e2706c20598d76b32a9e8b44d2d18c0a0b9778cecc6ccff5eac6dd08f0c3f9f9588e62b9ce02017490a23679a9a5787c6a70ca4f219b3a25208398bed8c6858442af4a21a6e8c5f195af6285ef2f15345a3cc60b98a8fcca3b3c48f828b799b71dfd678742c0ec2b92dd0203010001"
}
```