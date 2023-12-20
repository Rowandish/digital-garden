---
tags:
  - Crypto
  - Definition
---
![[1 N4Xyvmrm-6uMzJcKkU7BMw.png]]

[ERC20](https://ethereum.org/it/developers/docs/standards/tokens/erc-20/) (Ethereum Request Comment 20) è uno **standard tecnico implementativo** per lo sviluppo di smart contract che devono servire per **l'implementazione di nuovi [[Token]] sulla [[Blockchain]] di Ethereum**. Tali smart contract potranno distribuire token, nonché controllarne la fornitura e monitorarne il movimento e i saldi. 

Ad oggi la quantità di token ERC20 è enorme, basta controllare su [Etherscan](https://etherscan.io/tokens) per avere una idea.

### Funzioni standard

Essendo uno standard ogni smart contract per la fornitura di token ERC20 deve avere le seguenti sei funzioni:

- `totalSupply`: quanti token esistono in totale. Può essere definito e costante oppure variabile qualora il token possa essere sottoposto a mining
- `transfer`: trasferisce il token all'utente che lo chiede
- `allowance`: per verificare la quantità di token approvati
- `balanceOf`: permette di consultare il saldo dei titolari dei token
- `approve`: autorizza altri utenti a spendere i tuoi token. Questo importo approvato è memorizzato in quantità permessa

Di seguito le definizioni delle funzioni in [[Solidity]].
```CSharp
function name() public view returns (string)
function symbol() public view returns (string)
function decimals() public view returns (uint8)
function totalSupply() public view returns (uint256)
function balanceOf(address \_owner) public view returns (uint256 balance)
function transfer(address \_to, uint256 \_value) public returns (bool success)
function transferFrom(address \_from, address \_to, uint256 \_value) public returns (bool success)
function approve(address \_spender, uint256 \_value) public returns (bool success)
function allowance(address \_owner, address \_spender) public view returns (uint256 remaining)
```

Il vantaggio di avere uno standard è la possibilità di sviluppare applicazioni, exchange, portafogli e quant'altro in modo indipendente dal token specifico.