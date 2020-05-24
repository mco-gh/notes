Build Your Own Blockchain – FACILELOGIN

# Build Your Own Blockchain

## How to Create a Private Ethereum Blockchain from Ground-up?

Ethereum is a decentralized platform that runs smart contracts, applications that run exactly as programmed without possibility of downtime, censorship, fraud or third party interference. In this blog post I will take you through all the steps required in setting up a fully functioning private ethereum blockchain, inside your local network — which includes:

- •Setting up a private blockchain with ***ethereum*** using ***geth***.
- •Setting up the MetaMask ethereum wallet to work with the private blockchain.
- •Transfer funds between multiple accounts.
- •Create, deploy and invoke a smart contract on the private blockchain using ***remix***.
- •Setting up ***ethereum block explorer*** over the private blockchain.

#### Install Geth

Go Ethereum (or [***geth***](https://geth.ethereum.org/downloads/)) is one of the three original implementations (along with C++ and Python) of the ***ethereum*** protocol. It is written in Go, fully open source and licensed under the GNU LGPL v3. *Go Ethereum* is available either as a standalone client called ***geth*** that you can install on pretty much any operating system, or as a library that you can embed in your Go, Android or iOS projects.

To install ***geth*** on Mac OS X, we use [***homebrew***](https://brew.sh/). Homebrew installs the stuff you need that Apple didn’t. This blog assumes you have ***homebrew*** installed already, in case not check [this](https://docs.brew.sh/Installation.html) out. Once you have ***homebrew*** installed, following commands will install ***geth***.

brew tap ethereum/ethereum
brew install ethereum

Installing ***geth*** on Ubuntu is straightforward, you just need to use ***apt-get — ***the commands are shown below.

sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:thereum/ethereum
sudo apt-get update
sudo apt-get install ethereum

For Windows, you can find the corresponding ***geth*** installation [here](https://ethereum.github.io/go-ethereum/downloads/). If you find any difficulties in any of the above installations, check [this](https://ethereum.github.io/go-ethereum/install/) out.

#### Create a Miner Account

First we need to create an account for ethereum mining. This will generate a public/private key pair for you — and will be password protected. Do not lose your password, otherwise you will never be able to recover the keys. By default, keys are stored inside, **<*datadir>/keystore***. Everything ***geth*** persists, gets written inside ***datadir*** (except for the PoW Ethash DAG). The default data directory locations are platform specific. It is always better to override the path of the ***datadir***, and maintain your own location for your private blockchain.

- •Mac: ~/Library/Ethereum
- •Linux: ~/.ethereum
- •Windows: %APPDATA%\Ethereum

The Ethash DAG is stored at ~/.ethash (Mac/Linux) or %APPDATA%\Ethash (Windows) so that it can be reused by all clients.

Following command shows how to create an account, with a custom path for the ***datadir. ***Once completed, it will print your ethereum address.

**geth account new --datadir** <path-to-data-directory>
Example:
**geth account new --datadir** /path/to/data/dir

#### Create the Genesis Block

One ethereum blockchain differs from another by the genesis block. A blockchain starts with a genesis block and keeps building on top of it, where each block refers to the one below. In the ethereum public blockchain, the genesis block was created on July 20, 2015. To build our own blockchain, we need to create our own genesis block. Use the following command to init our private blockchain with the given genesis block.

**geth -datadir** <path-to-data-directory> **init** <path-to-genesis-block>
Example:
**geth**  **-datadir **/path/to/data/dir **init** /path/to/genesis.json

- •***datadir***: data directory for the databases and keystore.
- •***init***: bootstrap and initialize a new genesis block — with the provided json file.

Following shows our genesis block, used in our private blockchain — you need to save this as ***genesis.json*** and pass it to the above command.

{
"config": {
"chainId": 15,
"homesteadBlock": 0,
"eip155Block": 0,
"eip158Block": 0
},
"difficulty": "0x400",
"gasLimit": "0x2100000",
"alloc": {
"7a69b359e86893efa3d9732e4c65ced51567edd0":
{ "balance": "0x1337000000000000000000" }
}
}

- •***chainid***: this provides a way to send transactions that work on ethereum without working on ETC (ethereum classic) or the Morden testnet. [EIP 155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md) suggests following chainid values for different networks: ethereum mainnet (1), morden /expanse mainnet (2), ropsten (3), rinkeby (4), rootstock mainnet (30), rootstock testnet (31), kovan (42), ethereum classic mainnet (61), ethereum classic testnet (62), geth private chains (1337 by default). In our example we have used 15, which is not used by any of these networks.
- •***homesteadBlock***: the value 0 indicates, it is using ethereum homestead release. Homestead is the 2nd major ethereum release — and couple of days back on 16th Oct, 2017, ethereum did a hard fork to move to the ***byzantium*** release.
- •***eip155Block***: the value 0 indicates, this block supports EIP (ethereum improvement proposal)155. EIPs describe standards for the ethereum platform, including core protocol specifications, client APIs, and contract standards.
- •***eip158Block***: the value 0 indicates, this block supports EIP (ethereum improvement proposal)158.
- •***difficulty***: a value corresponding to the difficulty level applied during the ***nonce*** discovery of this block. In [this](https://medium.facilelogin.com/the-mystery-behind-block-time-63351e35603a) blog I explain how the ***difficulty*** is calculated in ethereum, in detail.
- •***gasLimit***: gas is the internal pricing for running a transaction or contract in ethereum. Each instruction sent to the Ethereum Virtual Machine (EVM) to process a transaction or smart contract costs a specific amount of gas. If the required amount of gas is not provided to the transaction, it will fail before completion. When you do any ethereum transaction, you specify a gas limit — that is the maximum gas all the operations corresponding to that transaction can consume. The ***gasLimit*** parameter in the block specifies, the aggregated ***gasLimit*** from all the transactions included in the block.
- •***alloc***: this allows to pre-allocate ether to one or more accounts from the genesis block. In the above genesis block, the pre-allocation is done to the account we created at the begining.

#### Start Mining

All set! Now we can start mining with ***geth*** using the following command. The ***networkid*** parameter here differentiates this ethereum network from the others. All the miners who want to connect to this network, have to use the same ***networkid*** along with the same genesis block.

**geth --mine --rpc --networkid** <networkd-id> **--datadir** <path-to-data-directory>

Example:
**geth --mine --rpc --networkid 1999 --datadir** /path/to/data/dir

- •***networkid: ****n*etwork identifier of this ethereum network. You pick a value you want. For example: ***olympic*** (0), ***frontier*** (1), ***morden*** (2), ***ropsten***(3).
- •***mine***: enables mining.
- •***rpc***: enables an HTTP-RPC server. Wallet applications can connect to this mining node over http.
- •***rpcaddr***: specifies the HTTP-RPC server listening interface (default: “localhost”)
- •***rpcport***: specifies the HTTP-RPC server listening port (default: 8545)
- •***rpcapi***: specifies the API’s offered over the HTTP-RPC interface (default: “eth,net,web3”)

--rpcapi "web3,eth"

- •***rpccorsdomain:*** enables CORS by specifying a comma separated list of domains from which to accept cross origin requests. This is useful when using browser based solidity editors (***remix***) to deploy smart contracts or browser based wallets. For example, following will accept CORS from any domain.

--rpccorsdomain "*"

- •***nodiscover***: disables the peer discovery mechanism. None of the other nodes in the network will not be able to find your node. If you intend to have this private blockchain being used within your local network with others, do not use this parameter.
- •***console: ***with this command we can start the mining node with an interactive javascript environment. We will learn more about this in the next section.

geth --mine --rpc --networkid 1999 --datadir /path/to/data/dir **console**

#### Attach Geth Console

Either you can start the mining node as a ***console*** — or you run the ***console*** separately and attach it to a mining node, with the ***attach*** command. The following shows how to do it, and make sure you follow the same parameter order.

**geth --datadir** <path-to-data-directory> **attach**  **ipc:**<path-to-data-directory>/**geth.ipc**

Example:

**geth**  **--datadir** /path/to/data/dir **attach ipc**:/path/to/data/dir /**geth.ipc**

The ***console*** connects to the mining node over ***ipc***. ***ipc*** (inter-process communications) works on the local computer. In this case ***geth ***creates***  ***an ***ipc*** pipe (which is represented by the file ***<path-to-data-directory>/geth.ipc***) on local computer’s filesystem — and ***console*** makes the connection to that node over ***ipc***.

#### View All Accounts

Once you are connected to the ***geth*** console, you can try out the following command to list all the available accounts.

> eth.accounts
["0x7a69b359e86893efa3d9732e4c65ced51567edd0"]

#### View Account Balance

Following command shows how to view the balance of a given account from the ***geth*** console.

> eth.getBalance("0x7a69b359e86893efa3d9732e4c65ced51567edd0")
1.295e+21

#### Connect MetaMask Ethereum Wallet

[MetaMask](https://metamask.io/) is an ethereum wallet, running as a chrome [extension](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn). It injects the ethereum web3 API into every website’s javascript context, so that those apps can read from the blockchain. MetaMask also lets the user create and manage their own identities, so when an application wants to perform a transaction and write to the blockchain, the user gets a secure interface to review the transaction, before approving or rejecting it.

To connect MetaMask to the private ethereum blockchain, we need to pick the right host name and the port. Web3 API is the ethereum javascript API implemented in ***web3.js***. To talk to an ethereum node from a javascript application, MetaMask uses the [***web3.js***](https://github.com/ethereum/web3.js)***  ***library, which gives a convenient interface for the **rpc** methods. Under the hood it communicates to a local node through **rpc** calls. ***web3.js*** works with any ethereum node, which exposes an **rpc** layer. You might have noticed in the above, when we start the mining node, we can pass the parameter ***rpcapi ***to specify, which interfaces we need to expose from that node. By default, if you do not specify anything, ***eth,net,web3*** — will be exposed.

![](../_resources/79d47ea9fd7ff16b07622b8b26c9caa2.png)

#### Transfer Ether

MetaMask will create you an ethereum account — a private key and an ethereum address. Following shows you how to transfer ether from the first account you created at the very beginning to the MetaMask account, from the ***geth*** console. To transfer funds from an account, we have to use that account’s private key for the signature. To use the private key, we need to unlock it, as shown below.

> personal.unlockAccount( "0x7a69b359e86893efa3d9732e4c65ced51567edd0","password")

[***personal***](https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal) is a management API provided by ***geth***. In addition to ***personal***, ***geth*** also provides management APIs: [***admin***](https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin), [***debug***](https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug), [***miner***](https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner) and [***txpool***](https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool). Once we unlock the account, we can define three variables in the console, for the ***sender***, ***receiver*** and ***amount*** to be sent. The value of the ***sender*** is the ethereum address we created at the very beginning of this blog, and the value of the ***receiver*** is the ethereum address created under MetaMask.

> var sender = "0x7a69b359e86893efa3d9732e4c65ced51567edd0";
> var receiver = "0xA9f28458eE1170F285440990c196c1592D3a73f5"
> var amount = web3.toWei(1, "ether")

Following command will do the funds transfer — it refers the variables we defined above.

> eth.sendTransaction({from:sender, to:receiver, value: amount})

#### View Account Balance In MetaMask

Once we completed the funds transfer following the above steps, you can find the account balance in two ways. One way is directly from the MetaMask plugin, as shown below.

![](../_resources/639259f0a7132ea6610b16fa2f45096c.png)
The other way is via the ***geth*** console, with the following command.
> eth.getBalance("0xA9f28458eE1170F285440990c196c1592D3a73f5")
1000000000000000000

#### Remex Solidity Editor

Solidity is the most popular programming language to write ethereum smart contracts. Remix is an IDE for ***solidity*** and has an integrated debugger and testing environment. You can access remix online editor from [here](https://remix.ethereum.org/). Remix can be connected to any ethereum network. To connect it to our local blockchain, make sure that you have started your mining node with the following command, with the highlighted parameter. The meaning of this parameter was discussed before. Instead of “*******” (which is more open) you can also use “***https://remix.ethereum.org***” as the value of ***rpccorsdomain*.**

geth --mine --rpc **--rpccorsdomain "*"** --networkid <networkd-id> --datadir <path-to-data-directory>

To connect, ***remix*** to our private network, we need to change the ***Environment*** to ***Web3 Provider***, under the tab ***Run***. When you do this change, ***remix*** will prompt you to specify the ***Web3 Provider Endpoint — ***set the value***  ***http://localhost:8545. Unless you have changed the port explicitly, the default mining node will start on the port 8545.

![](../_resources/824e9614fed6ea2be699b312abe8e924.png)

#### Writing a Smart Contract

Now we are all set to write our very first smart contract to run on ethereum. Copy the following code and paste it on the ***remix*** online editor. This is a very simple smart contract — and I do not wish to do a line by line explanation. In the next blog will explain ***solidity*** in detail.

pragma solidity ^0.4.11;
contract Hello {
// a string variable
string public greeting;

// the function with the same name as the class is a constructor
function Hello(string _greeting) {
greeting = _greeting;
}

// change the greeting message
function setGreeting(string _greeting) {
greeting = _greeting;
}

// get the greeting message
function greet() constant returns (string _greeting) {
_greeting = greeting;
}
}

If you have not changed any default settings in ***remix***, it is set to auto compile. If not you need to compile.

![](../_resources/f3e86e07586dccb13c5443d92488590e.png)

After compiling, when you click on the ***Details*** button, it will show you the estimated ***gas*** need to create this smart contract.

[**Introduction to Smart Contracts - Solidity 0.4.19 documentation** *A contract in the sense of Solidity is a collection of code (its functions) and data (its state) that resides at a…*solidity.readthedocs.io](http://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html)[(L)](http://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html)

#### Deploying a Smart Contract

Now we can deploy our smart contract to our private blockchain. Under the ***Run*** tab, make sure you have the right ethereum ***account*** selected, and then the right ***gas limit*** is specified. You can keep ***gas price*** and ***value*** as zero.

![](../_resources/436c4316264c6f2b20dc385dd9760617.png)

We use an ethereum transaction, signed by the selected account above to deploy the smart contract to the blockchain. To do the signing, first we need to unlock the account, via the ***geth*** console.

> personal.unlockAccount( "0x7a69b359e86893efa3d9732e4c65ced51567edd0","password")

Now you can click on the ***Create*** button to deploy the smart contract. In our smart contract, we have a constructor which accepts a string parameter, that’s why ***remix*** shows you an input box along with the ***Create*** button. You can type some value there (within quotes, e.g: “Hi”) — or just keep it empty. You will see the following message on the ***geth*** console when you submit the smart contract for creation. Also note that, if you have not specified the right ***gas limit***, the above will return an error.

INFO [10-19|07:31:08] Submitted contract creation fullhash=0xf5511bb9d088672ac0d3896b8590b9a3e25484300f02deecdd739c3a549ed33a contract=0x42b7E903Fb42e191a7D623cbb4b7b4330D329d78

#### Invoking a Smart Contract

Once you deploy the smart contract, ***remix*** UI gets changed a bit — as shown below, under the ***Run*** tab.

![](../_resources/d9c2e8adc5d391757f22df7d9f903279.png)

Now you can set some value to the ***setGreeting*** method — and click on it to invoke the smart contract. Once again, make sure that you have your account unlocked, because, to invoke a smart contract we use ethereum transactions and we need the signature of the initiator. Once done with the ***setGreeting*** method, you can invoke other methods too.

![](../_resources/bdedb3798e5dff7f463ce94d263d93ae.png)

#### Ethereum Block Explorer

You may be familiar with [***etherscan***](https://etherscan.io/), which gives a lot of insights into the ethereum public blockchain. But we cannot use it to point to our local blockchain. [Ethereum block explorer](https://github.com/carsenk/explorer) even though not as feature rich as ***etherscan***, is quite useful to find out what is going on in our local blockchain.

To setup ***ethereum block explorer*** first we need to get its source code from the following git repo.

git clone https://github.com/carsenk/explorer
Then, run the following install command from the ***explorer*** directory.
npm install

Once the installation is done, start the ***ethereum block explorer*** with the following command — and then you can access the web console from http://localhost:8000.

npm start

![](../_resources/b1243ec21eaf47c6e8bc478e37179b37.png)

To connect ***ethereum block explorer ***to our local blockchain, make sure that you have started your mining node with the following command, with the highlighted parameter — the meaning of this parameter was discussed before.

geth --mine --rpc **--rpccorsdomain "*"** --networkid <networkd-id> --datadir <path-to-data-directory>

**Update**: There is a discussion on this blog on Hacker News. Please feel free to join https://news.ycombinator.com/item?id=15509147

#### Summary

In this blog post we discussed how to set up a private blockchain with ***ethereum*** using ***geth***. Then we got MetaMask ethereum wallet to work with the private blockchain and transferred funds to the ethereum account created in MetaMask. ***remix ***online IDE was used to create, deploy and invoke a smart contract on the private blockchain. Finally we did set up ***ethereum block explorer*** over the private blockchain.