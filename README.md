# antigonovo
Exemplo de webiste em Django

Para instalar ambiente de desenvolvimento:

Instale o python 3

Cria um virtualenv na raiz do projeto:

```
python3 -m venv .venv
```

Ative o virtualenv e instale as dependências de desenvolvimento:

```
source .venv/bin/activate
pip install requirements-dev.txt
```

Confira se o código está de acordo com a PEP8:

```
flake8 .
```
