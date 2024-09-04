from dados import morador_logado, admin_logado
import datetime
    
from web import Web
from mobile import Mobile

w = Web()
m = Mobile()

# id_app = int(input("Digite seu ID: "))
# senha_morador = int(input("Digite sua senha: "))
# print(m.login_moradores(id_app, senha_morador))

if morador_logado == True:
   # print(m.search_product("coca-colaa")) #REVIEW - funcionando
   # print(m.acessar_produto(111)) #REVIEW - funcionando
   # print(m.registrar_compra(222)) #REVIEW - funcionando
   # print(m.registrar_compra(111)) #REVIEW - funcionando
   # print(m.historico()) #REVIEW - funcionando
   pass

# id_admin = int(input("Digite seu ID: "))
# senha_admin = int(input("Digite sua senha: "))
# print(w.login_admin(id_admin, senha_admin))

if admin_logado == True:
   # w.cadastrar_morador("Fulano", w.gerar_senha(), w.gerar_id(), "fulano@gmail.com", 102987123) #REVIEW - funcionando
   # w.cadastrar_bebida("kapo", w.gerar_id(), 2.70, 10, datetime.date.today()) #REVIEW - funcionando
   # print(w.listar_moradores()) #REVIEW - funcionando
   # print(w.listar_produtos()) #REVIEW - funcionando
   # w.monitorar_prazo_validade() #REVIEW - funcionando
   # print(w.aumentar_temperatura(5)) #REVIEW - funcioando
   # print(w.diminuir_temperatura(56)) #REVIEW - funcionando
   pass
