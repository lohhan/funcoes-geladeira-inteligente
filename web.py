from dados import admin_logado, usuario_admin,usuarios_moradores, produtos, ids_gerados, temperatura
import random
import datetime

class Web:

   # NOTE LOGIN ADMIN
   def login_admin(self, id_admin, senha_admin):
      global admin_logado
      
      for user, dados in usuario_admin.items():
         if dados["id_admin"] == id_admin:
            if dados["senha"] == senha_admin:
                  admin_logado = True
                  return "Acesso concedido"
      return "ID de usuário ou senha não encontrado"


   # NOTE CADASTRAR MORADOR
   def cadastrar_morador(self, nome_morador, senha_morador, id_app, email_morador, conta_condominio):
      usuarios_moradores[nome_morador] = {
         "id_app": id_app,
         "senha": senha_morador,
         "email": email_morador,
         "conta_condominio": conta_condominio,
      }

   def gerar_id(self):
      while True:
         num_id = random.randint(100, 999)
         if num_id not in ids_gerados:
               ids_gerados.add(num_id)
               return num_id

   def gerar_senha(self):
      while True:
         num_senha = random.randint(100000, 999999)
         if num_senha not in ids_gerados:
               ids_gerados.add(num_senha)
               return num_senha

   # NOTE CADASTRAR BEBIDA
   def cadastrar_bebida(self, nome_produto, id_produto, preco, qtd_disponivel, data_formatada):
      produtos[nome_produto] = {
            "id": id_produto,
            "preco": preco,
            "qtd_disponivel": qtd_disponivel,
            "data_validade": data_formatada,
      }

   # NOTE LISTAR MORADORES
   def listar_moradores(self):
      return usuarios_moradores

   # NOTE LISTAR BEBIDAS
   def listar_produtos(self):
      return produtos

   # NOTE PRAZO VALIDADE
   def monitorar_prazo_validade(self):
      for nome, dados in produtos.items():
         if dados["data_validade"] < datetime.date.today():
               print(f"Produto '{nome}' fora da validade! Favor, retirar do estoque!")
               
   # NOTE CONTROLE TEMPERATURA
   def aumentar_temperatura(self, graus):
      global temperatura

      temperatura += graus
      if temperatura <= 5:
         return f"A temperatura atual é de: {temperatura}"
      else:
         return "A temperatura não pode ser maior que 5 graus."
      
   def diminuir_temperatura(self, graus):
      global temperatura

      temperatura -= graus
      if temperatura >= -15:
         return f"A temperatura atual é de: {temperatura}"
      else:
         return "A temperatura não pode ser menor que 15 graus."