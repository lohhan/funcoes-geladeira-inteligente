from dados import usuario_logado, usuarios_moradores, produtos, historico_compras, ids_gerados
import random
import datetime

# # NOTE LOGIN MORADORES
# def login_moradores(id_app, senha_morador):
#    global usuario_logado
   
#    for user, dados in usuarios_moradores.items():
#       if dados["id_app"] == id_app:
#          if dados["senha"] == senha_morador:
#                usuario_logado = True
#                return "Acesso concedido"
#    return "ID de usuário ou senha não encontrado"

# id_app = int(input("Digite seu ID: "))
# senha_morador = int(input("Digite sua senha: "))

# print(login_moradores(id_app, senha_morador))

# # NOTE PROCURAR POR PRODUTO
# def search_product(search):
#    if usuario_logado:
#       if search in produtos:
#          return "Produto encontrado"
#       else:
#          return "Produto não encontrado"
#    else:
#       return "Usuário não logado no sistema. Faça login para utilizar essa função"

# nome_produto = input("Procure um item: ").lower()
# print(search_product(nome_produto))

# # NOTE ACESSAR PRODUTO
# def acessar_produto(id_produto):
#    for product, data in produtos.items():
#       if data["id"] == id_produto:
#          return f"Produto: {product}\nPreço: {data["preco"]}\nQtd: {data["qtd_disponivel"]}"
#    return "Produto não disponível no momento"

# print(acessar_produto(222))

# # NOTE REGISTRAR COMPRA
# def registrar_compra(id_produto):
#     for nome_produto, dados in produtos.items():
#         if dados["id"] == id_produto:
#             historico_compras.append({
#                 "nome": nome_produto,
#                 "preco": dados["preco"]
#             })
#             produtos[nome_produto]["qtd_disponivel"] -= 1
#             return f"Produto '{nome_produto}' comprado com sucesso!"
#     return "Produto não encontrado."
    
# # NOTE HISTORICO 
# def historico():
#     if not historico_compras:
#         return "Nenhum produto no histórico."
    
#     historico_str = "Histórico de Compras:\n"
#     for item in historico_compras:
#         historico_str += f"- {item['nome']} por R$ {item['preco']:.2f}\n"
    
#     return historico_str
    
# print(registrar_compra(111))
# print(registrar_compra(222))
# print(registrar_compra(333))

# print(historico())
    
# # NOTE CADASTRAR MORADOR
# def cadastrar_morador(nome_morador, senha_morador, id_app, email_morador, conta_condominio):
#    usuarios_moradores[nome_morador] = {
#        "id_app": id_app,
#        "senha": senha_morador,
#        "email": email_morador,
#        "conta_condominio": conta_condominio,
#    }
#    print(usuarios_moradores)

# def gerar_id():
#     while True:
#         num_id = random.randint(100, 999)
#         if num_id not in ids_gerados:
#             ids_gerados.add(num_id)
#             return num_id

# def gerar_senha():
#     while True:
#         num_senha = random.randint(100000, 999999)
#         if num_senha not in ids_gerados:
#             ids_gerados.add(num_senha)
#             return num_senha

# nome_morador = input("Nome morador: ")
# email_morador = input("Email morador: ")
# conta_condominio = int(input("Insira a conta do condominio: "))
# senha_morador = gerar_senha()
# id_app = gerar_id()

# cadastrar_morador(nome_morador, senha_morador, id_app, email_morador, conta_condominio)

# # NOTE CADASTRAR BEBIDA
# def cadastrar_bebida(nome_produto, id_produto, preco, qtd_disponivel, data_formatada):
#    produtos[nome_produto] = {
#          "id": id_produto,
#          "preco": preco,
#          "qtd_disponivel": qtd_disponivel,
#          "data_validade": data_formatada,
#    }
      
#    print(produtos)

# nome_produto = input("Nome produto: ")
# id_produto = gerar_id()
# preco = float(input("Digite o preço do produto: "))
# qtd_disponivel = int(input("Informe a quantidade: "))

# data_validade = datetime.today()
# data_formatada = data_validade.strftime("%d-%m-%Y")

# cadastrar_bebida(nome_produto, id_produto, preco, qtd_disponivel, data_formatada)


# # NOTE LISTAR MORADORES
# def listar_moradores():
#     return usuarios_moradores

# # NOTE LISTAR BEBIDAS
# def listar_produtos():
#     return produtos

# # NOTE PRAZO VALIDADE
# def monitorar_prazo_validade():
#     for nome, dados in produtos.items():
#         if dados["data_validade"] < datetime.date.today():
#             return "Produto fora da validade! Favor, retirar do estoque!"
            
# NOTE CONTROLE TEMPERATURA
# temperatura = -4
# def aumentar_temperatura(graus):
#    global temperatura

#    temperatura += graus
#    if temperatura <= 5:
#       return f"A temperatura atual é de: {temperatura}"
#    else:
#       return "A temperatura não pode ser maior que 5 graus."
   
# def diminuir_temperatura(graus):
#    global temperatura

#    temperatura -= graus
#    if temperatura >= -15:
#       return f"A temperatura atual é de: {temperatura}"
#    else:
#       return "A temperatura não pode ser menor que 15 graus."
   
# print(diminuir_temperatura(18))