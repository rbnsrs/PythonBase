#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo do idioma configurado o ambiente, o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável lang devidamente configurada, ex:
    
    export LANG=pt_BR

Execuçao:

    python3 helloII.py
    ou
    ./helloII.py
"""

__version__ = "0.0.1"
__autor__ = "Robson Ar"
__license__ = "Unlicense"

import os


current_language = os.getenv("LANG", "it_IT")[:5]

msg = "Hello, Hello, World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)



