#!/bin/bash
# Configura o PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Instala dependências básicas
pip3 install --user -r requirements.txt

# Cria links simbólicos para imports
ln -s $(pwd)/blockchain /usr/local/lib/python3.10/dist-packages/blockchain
ln -s $(pwd)/security /usr/local/lib/python3.10/dist-packages/security
