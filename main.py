from dados import usuario_logado, usuarios_moradores, produtos, historico_compras

# NOTE LOGIN MORADORES
def login_moradores(id_morador, senha_morador):
   global usuario_logado
   
   for user, dados in usuarios_moradores.items():
      if dados["id"] == id_morador:
         if dados["senha"] == senha_morador:
               usuario_logado = True
               return "Acesso concedido"
   return "ID de usuário ou senha não encontrado"

id_morador = int(input("Digite seu ID: "))
senha_morador = int(input("Digite sua senha: "))

print(login_moradores(id_morador, senha_morador))

# NOTE PROCURAR POR PRODUTO
def search_product(search):
   if usuario_logado:
      if search in produtos:
         return "Produto encontrado"
      else:
         return "Produto não encontrado"
   else:
      return "Usuário não logado no sistema. Faça login para utilizar essa função"

nome_produto = input("Procure um item: ").lower()
print(search_product(nome_produto))

# NOTE ACESSAR PRODUTO
def acessar_produto(id_produto):
   for product, data in produtos.items():
      if data["id"] == id_produto:
         return f"Produto: {product}\nPreço: {data["preco"]}\nQtd: {data["qtd_disponivel"]}"
   return "Produto não disponível no momento"

print(acessar_produto(222))

# NOTE REGISTRAR COMPRA
def registrar_compra(id_produto):
    for nome_produto, dados in produtos.items():
        if dados["id"] == id_produto:
            historico_compras.append({
                "nome": nome_produto,
                "preco": dados["preco"]
            })
            produtos[nome_produto]["qtd_disponivel"] -= 1
            return f"Produto '{nome_produto}' comprado com sucesso!"
    return "Produto não encontrado."
    
# NOTE HISTORICO 
def historico():
    if not historico_compras:
        return "Nenhum produto no histórico."
    
    historico_str = "Histórico de Compras:\n"
    for item in historico_compras:
        historico_str += f"- {item['nome']} por R$ {item['preco']:.2f}\n"
    
    return historico_str
    
print(registrar_compra(111))
print(registrar_compra(222))
print(registrar_compra(333))

print(historico())
    
    