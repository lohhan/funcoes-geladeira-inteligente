import datetime

morador_logado = True
admin_logado = True

data_hoje = datetime.date.today()

delta = datetime.timedelta(days=-7)
data_passada = data_hoje + delta

usuarios_moradores = {
   "user1": {
      "id_app": 123,
      "senha": 123456,
      "email": "teste@gmail.com",
      "conta_condominio": 123456101
   },
   "user2": {
      "id_app": 456,
      "senha": 654321,
      "email": "teste@gmail.com",
      "conta_condominio": 123456201
   },
   "user3": {
      "id_app": 789,
      "senha": 999111,
      "email": "teste@gmail.com",
      "conta_condominio": 123456301
   },
}

usuario_admin = {
   "admin": {
      "id_admin": 123,
      "senha": 321321,
   }
}

produtos = {
    "coca-cola": {
        "preco": 3.50,
        "id": 111,
        "qtd_disponivel": 10,
        "data_validade": data_passada
    },
    "heineken": {
        "preco": 7.99,
        "id": 222,
        "qtd_disponivel": 10,
        "data_validade": data_hoje
    },
    "pergola": {
        "preco": 25.0,
        "id": 333,
        "qtd_disponivel": 10,
        "data_validade": data_passada
    },
    "toddynho": {
        "preco": 2.70,
        "id": 444,
        "qtd_disponivel": 10,
        "data_validade": data_hoje
    },
    "oq": {
        "preco": 16.0,
        "id": 555,
        "qtd_disponivel": 10,
        "data_validade": data_hoje
    }
}

historico_compras = []

ids_gerados = set()

senha_gerada = set()

temperatura = -4