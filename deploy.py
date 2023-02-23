# Libreria para compilar e instalar solidity
from solcx import compile_standard, install_solc
import json
from web3 import Web3

# Aqui estamos leendo el archivo .sol
with open("./simple_storage.sol", "r") as file:
    simple_storage_file = file.read()

# Aqui vamos a instalar la version se solidity
# print("Installing...")
install_solc("0.6.0")

# Solidity source code
compiled_sol = compile_standard(
    {
        # El lenguaje que vamos a compilar
        "language": "Solidity",
        "sources": {"simple_storage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    # Version de solidity que vamos a usar -> Lo hemos instalado con anterioridad
    solc_version="0.6.0",
)

# print(compiled_sol)

# estamos enviando la informacio de compiled_sol -> file en formato JSON
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


## Configuracion de Datos -> para poder usar los contratos inteligentes

# get bytecode
bytecode = compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]


## Conexion con Ganache

##RPC SERVER HTTP://127.0.0.1:7545
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# NETWORK ID 5777
chain_id = 5777
## Direccion Y Llave
# Define contract address and private key
my_address = "0x7f032d1FFe62CE56004eCc15042104A94c51D6f2"
private_key = "0xaf317601ec406f442fc2eeb05f2728e31ca0234cc61f02a9e59034f9b84a31a5"

# Create the contract object using the ABI and bytecode
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the current transaction count for the account
nonce = w3.eth.get_transaction_count(my_address)

# Create the transaction to deploy the contract
transaction = SimpleStorage.constructor()._build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "gas": 200000,  # Set gas limit to an appropriate value
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")


tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


# Enviar la transaccion

# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# # Wait for the transaction to be mined, and get the transaction receipt
# print("Waiting for transaction to finish...")
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
