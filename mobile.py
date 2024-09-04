from dados import morador_logado, usuarios_moradores, produtos, historico_compras
import datetime

morador_atual = 0

class Mobile:

   # NOTE LOGIN MORADORES
   def login_moradores(self, id_app, senha_morador):
      global morador_logado, morador_atual
      
      for user, dados in usuarios_moradores.items():
         if dados["id_app"] == id_app:
            if dados["senha"] == senha_morador:
                  morador_atual = id_app
                  morador_logado = True
                  return "Acesso concedido"
      return "ID de usuário ou senha não encontrado"

   # NOTE PROCURAR POR PRODUTO
   def search_product(self, search):
      if search in produtos:
         return "Produto encontrado"
      else:
         return "Produto não encontrado"

   # NOTE ACESSAR PRODUTO
   def acessar_produto(self, id_produto):
      for product, data in produtos.items():
         if data["id"] == id_produto:
            return f"Produto: {product}\nPreço: {data["preco"]}\nQtd: {data["qtd_disponivel"]}"
      return "Produto não disponível no momento"

   # NOTE REGISTRAR COMPRA
   def registrar_compra(self, id_produto):
      for nome_produto, dados in produtos.items():
         if dados["id"] == id_produto:
               historico_compras.append({
                  "nome": nome_produto,
                  "preco": dados["preco"],
                  "data-compra": datetime.date.today()
               })
               produtos[nome_produto]["qtd_disponivel"] -= 1
               return f"Produto '{nome_produto}' comprado com sucesso! ID USUÁRIO: {morador_atual}"
      return "Produto não encontrado."
      
   # NOTE HISTORICO 
   def historico(self):
      if not historico_compras:
         return "Nenhum produto no histórico."
      
      historico_str = "Histórico de Compras:\n"
      for item in historico_compras:
         historico_str += f"- {item['nome']} por R$ {item['preco']:.2f} (DATA - {item["data-compra"]})\n"
      
      return historico_str