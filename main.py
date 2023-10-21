import graphics as gf
import random as rd
from datetime import datetime
import os

fundo_tela1 = gf.Image(gf.Point(550,400),"Login.png")
fundo_tela2 = gf.Image(gf.Point(550,400),"Cadastro.png")
fundo_tela3 = gf.Image(gf.Point(550,400),"Paciente_Exame.png")
fundo_tela4 = gf.Image(gf.Point(550,400),"Medico_Pesquisar.png")
fundo_tela5 = gf.Image(gf.Point(550,400),"Cadastro.png")
fundo_tela6 = gf.Image(gf.Point(550,400),"Paciente_Editar.png")
fundo_tela7 = gf.Image(gf.Point(550,400),"Paciente_Editar_Exame.png")

janela = gf.GraphWin("Analizador de hemograma",1100,800)
fundo_tela1.draw(janela)


caixa_login = gf.Entry(gf.Point(551,315),37)
caixa_login.setFill(gf.color_rgb(218, 254, 236))
caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
caixa_login.draw(janela)
                                                                      #criando objetos

caixa_senha = gf.Entry(gf.Point(551,415),37)
caixa_senha.setFill(gf.color_rgb(218, 254, 236))
caixa_senha.setTextColor(gf.color_rgb(0, 0, 0))
caixa_senha.draw(janela)


#eritograma
hemacias_entry = gf.Entry(gf.Point(330,243),10)
hemacias_entry.setFill(gf.color_rgb(255,255,255))

hemoglobina_entry = gf.Entry(gf.Point(330,288),10)
hemoglobina_entry.setFill(gf.color_rgb(255,255,255))

hematocrito_entry = gf.Entry(gf.Point(330,333),10)
hematocrito_entry.setFill(gf.color_rgb(255,255,255))

vcm_entry = gf.Entry(gf.Point(330,376),10)
vcm_entry.setFill(gf.color_rgb(255,255,255))

hcm_entry = gf.Entry(gf.Point(330,421),10)
hcm_entry.setFill(gf.color_rgb(255,255,255))

chcm_entry = gf.Entry(gf.Point(330,466),10)
chcm_entry.setFill(gf.color_rgb(255,255,255))

rdw_entry = gf.Entry(gf.Point(330,510),10)
rdw_entry.setFill(gf.color_rgb(255,255,255))

#leucograma
leucocitos_entry = gf.Entry(gf.Point(603,244),10)
leucocitos_entry.setFill(gf.color_rgb(255,255,255))

basofilos_entry = gf.Entry(gf.Point(603,288),10)
basofilos_entry.setFill(gf.color_rgb(255,255,255))

eosinofilos_entry= gf.Entry(gf.Point(603,331),10)
eosinofilos_entry.setFill(gf.color_rgb(255,255,255))

mielocitos_entry = gf.Entry(gf.Point(603,374),10)
mielocitos_entry.setFill(gf.color_rgb(255,255,255))

metamielocitos_entry = gf.Entry(gf.Point(603,418),10)
metamielocitos_entry.setFill(gf.color_rgb(255,255,255))

bastoes_entry = gf.Entry(gf.Point(603,462),10)
bastoes_entry.setFill(gf.color_rgb(255,255,255))

segmentados_entry = gf.Entry(gf.Point(603,506),10)
segmentados_entry.setFill(gf.color_rgb(255,255,255))

linfocitos_entry = gf.Entry(gf.Point(603,548),10)
linfocitos_entry.setFill(gf.color_rgb(255,255,255))

linfocitos_atipicos_entry = gf.Entry(gf.Point(603,591),10)
linfocitos_atipicos_entry.setFill(gf.color_rgb(255,255,255))

monocitos_entry = gf.Entry(gf.Point(603,634),10)
monocitos_entry.setFill(gf.color_rgb(255,255,255))
 
#plaquetas
plaquetas_entry = gf.Entry(gf.Point(874,246),10)
plaquetas_entry.setFill(gf.color_rgb(255,255,255))

vpm_entry = gf.Entry(gf.Point(874,290),10)
vpm_entry.setFill(gf.color_rgb(255,255,255))

plaquetocrito_entry = gf.Entry(gf.Point(874,334),10)
plaquetocrito_entry.setFill(gf.color_rgb(255,255,255))

pdw_entry = gf.Entry(gf.Point(874,376),10)
pdw_entry.setFill(gf.color_rgb(255,255,255))


hdl_entry = gf.Entry(gf.Point(874,461),10)   
hdl_entry.setFill(gf.color_rgb(255,255,255))

ldl_entry = gf.Entry(gf.Point(874,504),10)
ldl_entry.setFill(gf.color_rgb(255,255,255))


data_entry = gf.Entry(gf.Point(820,609),10)
data_entry.setFill(gf.color_rgb(255,255,255))


#textos

paciente_desejado_entry = gf.Entry(gf.Point(570,307),50)
paciente_desejado_entry.setFill(gf.color_rgb(255,255,255))


gf.update(10)

def get_login(): #pega a informação de login
    login = caixa_login.getText()
    return login

def get_senha(): #pega a senha
    senha = caixa_senha.getText()
    return senha

def get_nome():
    nome = caixa_nome.getText()
    return nome

def get_cpf():
    cpf = caixa_cpf.getText()
    return cpf

def exit(): #esc para sair do programa
    tecla = janela.checkKey()
    if tecla == "Escape":
        janela.close()

def fazer_login_medico():
    dados_usuario_format = login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    with open("dados_login_medico.csv", "r") as arquivo:
      for linha in arquivo:
        linha = linha[0:-1].split(';')

        if dados_usuario_format[0] == linha[1] and dados_usuario_format[1] == linha[2]:
          verificacao_login_medico = True
          break
        else:
          verificacao_login_medico = False
      arquivo.close()
      return verificacao_login_medico

def fazer_login(): #verifica se as informações que o usuário digitou batem com o data base
    dados_usuario_format = login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    with open("dados_login.csv", "r") as arquivo:
      for linha in arquivo:
        linha = linha[0:-1].split(';')

        if dados_usuario_format[0] == linha[1] and dados_usuario_format[1] == linha[2]:
          verificacao_login = True
          break
        else:
          verificacao_login = False
      arquivo.close()
      return verificacao_login

def valida_email(): #valida o email
    if ("@" in login) and (".com" in login ):
        return True
    else:
        return False

def fazer_cadastro(): #faz o cadastro do usuário, gerando um id único
    #testa se o id já existe:
    id_valido = False
    while id_valido == False:
        with open("dados_login.csv","r") as arquivo:
            id_gerado = gera_id()
            for linha in arquivo:
                lista = linha[0:-1].split(';') #transforma a linha em uma lista removendo o '\n'
                if id_gerado != lista[0]: #compara o id_gerado com a posição[0] da lista
                    id_valido = True
                else:
                    id_valido = False
            arquivo.close()

    #testa se o cadastro é válido
    dados_usuario = id_gerado + ';' + login + ';' + senha + ";" + nome + ';' + cpf + '\n'
    dados_usuario_format = id_gerado + ';' + login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    if (login!='') and (senha!=''):
        valido = valida_email()
        if valido == True:
            with open("dados_login.csv","r") as arquivo1:
                for linha in arquivo1:
                    split_linha = linha[0:-1].split(';')

                    if dados_usuario_format[1] == split_linha[1]:
                        verificacao_cadastro = False
                        break
                    else:
                        verificacao_cadastro = True
                arquivo1.close()
                if verificacao_cadastro == True:
                    with open('dados_login.csv','a') as arquivo2:
                            arquivo2.write(dados_usuario)
                            arquivo2.close()
        else:
            verificacao_cadastro = False
    else:
        verificacao_cadastro = False
    return verificacao_cadastro

def fazer_cadastro_medico():
    #testa se o id já existe:
    id_valido = False
    while id_valido == False:
        with open("dados_login_medico.csv","r") as arquivo:
            id_gerado = gera_id()
            for linha in arquivo:
                lista = linha[0:-1].split(';') #transforma a linha em uma lista removendo o '\n'
                if id_gerado != lista[0]: #compara o id_gerado com a posição[0] da lista
                    id_valido = True
                else:
                    id_valido = False
            arquivo.close()

    #testa se o cadastro é válido
    dados_usuario = id_gerado + ';' + login + ';' + senha + ";" + nome + ';' + cpf + '\n'
    dados_usuario_format = id_gerado + ';' + login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    if (login!='') and (senha!=''):
        valido = valida_email()
        if valido == True:
            with open("dados_login_medico.csv","r") as arquivo1:
                for linha in arquivo1:
                    split_linha = linha[0:-1].split(';')

                    if dados_usuario_format[1] == split_linha[1]:
                        verificacao_cadastro_medico = False
                        break
                    else:
                        verificacao_cadastro_medico = True
                arquivo1.close()
                if verificacao_cadastro_medico == True:
                    with open('dados_login_medico.csv','a') as arquivo2:
                            arquivo2.write(dados_usuario)
                            arquivo2.close()
        else:
            verificacao_cadastro_medico = False
    else:
        verificacao_cadastro_medico = False
    return verificacao_cadastro_medico

def exames_draw(): #desenha os obejtos da aba de exames
    hemacias_entry.draw(janela)
    hemoglobina_entry.draw(janela)
    hematocrito_entry.draw(janela)
    vcm_entry.draw(janela)
    hcm_entry.draw(janela)
    chcm_entry.draw(janela)
    rdw_entry.draw(janela)
    leucocitos_entry.draw(janela)
    basofilos_entry.draw(janela)
    eosinofilos_entry.draw(janela)
    mielocitos_entry.draw(janela)
    metamielocitos_entry.draw(janela)
    bastoes_entry.draw(janela)
    segmentados_entry.draw(janela)
    linfocitos_entry.draw(janela)
    linfocitos_atipicos_entry.draw(janela)
    monocitos_entry.draw(janela)
    plaquetas_entry.draw(janela)
    vpm_entry.draw(janela)
    plaquetocrito_entry.draw(janela)
    pdw_entry.draw(janela)
    hdl_entry.draw(janela)
    ldl_entry.draw(janela)
    data_entry.draw(janela)

def exames_undraw(): #apaga os objetos e o background da aba de exames
    hemacias_entry.undraw()
    hemoglobina_entry.undraw()
    hematocrito_entry.undraw()
    vcm_entry.undraw()
    hcm_entry.undraw()
    chcm_entry.undraw()
    rdw_entry.undraw()
    leucocitos_entry.undraw()
    basofilos_entry.undraw()
    eosinofilos_entry.undraw()
    mielocitos_entry.undraw()
    metamielocitos_entry.undraw()
    bastoes_entry.undraw()
    segmentados_entry.undraw()
    linfocitos_entry.undraw()
    linfocitos_atipicos_entry.undraw()
    monocitos_entry.undraw()
    plaquetas_entry.undraw()
    vpm_entry.undraw()
    plaquetocrito_entry.undraw()
    pdw_entry.undraw()
    hdl_entry.undraw()
    ldl_entry.undraw()
    data_entry.undraw()
    fundo_tela3.undraw()

def get_exames(): #pega os dados dos exames digitados
    hemacias_get = hemacias_entry.getText()
    hemoglobina_get = hemoglobina_entry.getText()
    hematocrito_get = hematocrito_entry.getText()
    vcm_get = vcm_entry.getText()
    hcm_get = hcm_entry.getText()
    chcm_get = chcm_entry.getText()
    rdw_get = rdw_entry.getText()
    leucocitos_get = leucocitos_entry.getText()
    basofilos_get = basofilos_entry.getText()
    eosinofilos_get = eosinofilos_entry.getText()
    mielocitos_get = mielocitos_entry.getText()
    metamielocitos_get = metamielocitos_entry.getText()
    bastoes_get = bastoes_entry.getText()
    segmentados_get = segmentados_entry.getText()
    linfocitos_get = linfocitos_entry.getText()
    linfocitos_atipicos_get = linfocitos_atipicos_entry.getText()
    monocitos_get = monocitos_entry.getText()
    vpm_get = vpm_entry.getText()
    plaquetocrito_get = plaquetocrito_entry.getText()
    pdw_get = pdw_entry.getText()
    data_get = data_entry.getText()
    ldl_get = ldl_entry.getText()
    hdl_get = hdl_entry.getText()

    texto_exames = hemacias_get+';'+hemoglobina_get+';'+hematocrito_get+';'+vcm_get+';'+hcm_get+';'+chcm_get+';'+rdw_get+';'+leucocitos_get+';'+basofilos_get+';'+eosinofilos_get+';'+mielocitos_get+';'+metamielocitos_get+';'+bastoes_get+';'+segmentados_get+';'+linfocitos_get+';'+linfocitos_atipicos_get+';'+monocitos_get+';'+vpm_get+';'+plaquetocrito_get+';'+pdw_get+';'+ldl_get+';'+hdl_get+';'+data_get
    return texto_exames

def apagar_tudo(): #apaga os obejtos do primeiro evento
    caixa_login.undraw()
    caixa_senha.undraw()
    fundo_tela1.undraw()

def apagar_tudo_cadastro():
    caixa_login.undraw()
    caixa_senha.undraw()
    fundo_tela1.undraw()
    caixa_nome.undraw()
    caixa_cpf.undraw()
    fundo_tela5.undraw()

def gera_id(): #gera um id aleatório de 5 dígitos
    id = ''

    for i in range(5):
        num = rd.randint(0,9)
        id = id + str(num)
    return id

eventos = ["1","2",'3','4','5','6'] #eventos para direcionar o programa

aviso_incorreto = False
aviso_existente = False

prosseguir = eventos[0]
while True:
    if prosseguir == eventos[0]:
        click = janela.getMouse()
        rodar = exit()
        login = get_login()
        senha = get_senha()

        #LOGIN
        if (click.getX() >= 449 and click.getX() <= 646) and (click.getY() >= 489 and click.getY() <= 528):
            #verifica se o login pode ser efetuado
            verificacao_login = fazer_login()
            #Verifica e remove se ja existe um aviso na tela
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            #testa se o login esta certo
            if verificacao_login == True:
                login_atual = get_login()  #pega o e-mail do usuário atual
                apagar_tudo()
                prosseguir = eventos[1]
            else:
                aviso_usuario_incorreto = gf.Text(gf.Point(550,465),"E-mail ou senha inválidos.")
                aviso_usuario_incorreto.setTextColor(gf.color_rgb(0, 255, 128))
                aviso_usuario_incorreto.draw(janela)
                aviso_incorreto = True
                
        #CADASTRO
        if (click.getX() >= 449 and click.getX() <= 647) and (click.getY() >= 551 and click.getY() <= 588):
            caixa_login.undraw()
            caixa_senha.undraw()
            prosseguir = eventos[3]

        #LOGIN MÉDICO
        if (click.getX() >= 449 and click.getX() <= 647) and (click.getY() >= 613 and click.getY() <= 690):
            verificacao_login_medico = fazer_login_medico()

            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_login_medico == True:
                login_atual = get_login()   #pega o e-mail do usuário atual
                apagar_tudo()
                prosseguir = eventos[2]
            else:
                aviso_usuario_existente = gf.Text(gf.Point(550,465),"Email não cadastrado ou inválido")
                aviso_usuario_existente.setTextColor(gf.color_rgb(0, 255, 128))
                aviso_usuario_existente.draw(janela)
                aviso_existente = True

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    informacoes_desenhadas = False
    while prosseguir == eventos[1]:
        rodar = exit()
        if informacoes_desenhadas == False:
            fundo_tela3.draw(janela)
            exames_draw()                               #objetos e caixas de entrada são desenhados

        informacoes_desenhadas = True #verifica se os objetos forma desenhados e evita o crash
        click = janela.getMouse()

        if (click.getX() >= 434 and click.getX() <= 667) and (click.getY() >= 665  and click.getY() <= 739):     #verifica as coordenadas e pega os dados dos Entrys
            data_atual = data_entry.getText()
            saida = get_exames()
            with open('dados_login.csv','r') as arquivo:  #pega o id do usuário atual
                for linha in arquivo:
                    lista = linha.split(';')
                    if login_atual in lista:
                        id_atual = lista[0]
                arquivo.close()
            
            informacoes = ''
            with open("dados_exames.csv","r") as arquivo:
                for linha in arquivo:
                    informacoes = informacoes + linha
                arquivo.close()
            with open('dados_exames.csv','w',encoding='UTF-8') as arquivo:  #escreve no csv dos exames o id, login e a saida
                texto = informacoes + id_atual + ';' + login_atual + ';' + saida + '\n'
                #print(texto)
                arquivo.write(texto)
                arquivo.close()
            prosseguir = eventos[4]            #passa para o próximo evento

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
    verificador_anticrash = False
    while prosseguir == eventos[2]:    #seleção de pacientes do médico
        exames_undraw()
        if verificador_anticrash == False:    #evita crash e permite o loop do programa
            fundo_tela4.draw(janela)
            paciente_desejado_entry.draw(janela)
            '''pacientes_text.draw(janela)'''
            '''text_botao_gerar.draw(janela)'''

        verificador_anticrash = True
        rodar = exit()
        click = janela.getMouse()

        if (click.getX() >= 388 and click.getX() <= 713) and (click.getY() >= 587 and click.getY() <= 661):
            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table><caption> Pacientes cadastrados </caption> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Nome </td> <td class="head"> CPF </td><tr>'
            with open('dados_login.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td>')
                arquivo.close()

            saida = saida + '</table></body></html>'

            with open('relatorio_pacientes.html','w',encoding="UTF-8") as html:
                html.write(saida)
                html.close()
            os.system('relatorio_pacientes.html')
        
        
        if (click.getX() >= 388 and click.getX() <= 714) and (click.getY() >= 485 and click.getY() <= 556):  #botão para gerar o relatório
            paciente_desejado = paciente_desejado_entry.getText()
            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table><caption> Exames de ' +str(paciente_desejado)+ '</caption> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Hemacias </td> <td class="head"> Hemoglobina </td> <td class="head"> Hematocrito </td> <td class="head"> VCM </td> <td class="head"> HCM </td> <td class="head"> CHCM </td> <td class="head"> RDW </td> <td class="head"> Leucocitos </td> <td class="head"> Basofilos </td> <td class="head"> Eosinofilos </td> <td class="head"> Mielocitos </td> <td class="head"> Metamielocitos </td> <td class="head"> Bastoes </td> <td class="head"> Segmentados </td> <td class="head"> Linfocitos </td> <td class="head"> Linfocitos atipicos </td> <td class="head"> Monocitos </td> <td class="head"> VPM </td> <td class="head"> Plaquetocrito </td> <td class="head"> PDW </td> <td class="head"> HDL </td> <td class="head"> LDL </td> <td class="head"> Data </td></tr>'
            with open('dados_exames.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    if linha[0] == paciente_desejado:
                        saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[2]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td> <td> {linha[5]} </td> <td> {linha[6]} </td> <td> {linha[7]} </td> <td> {linha[8]} </td> <td> {linha[9]} </td> <td> {linha[10]} </td> <td> {linha[11]} </td> <td> {linha[12]} </td> <td> {linha[13]} </td> <td> {linha[14]} </td> <td> {linha[15]} </td> <td> {linha[16]} </td> <td> {linha[17]} </td> <td> {linha[18]} </td> <td> {linha[19]} </td> <td> {linha[20]} </td> <td> {linha[21]} </td> <td> {linha[22]} </td> <td> {linha[23]} </td> <td> {linha[24]} </td>')
                arquivo.close()

            saida = saida + '</table></body></html>'

            with open('relatorio_paciente_desejado.html','w',encoding="UTF-8") as html:
                html.write(saida)
                html.close()
            os.system('relatorio_paciente_desejado.html')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    verificador_anticrash = False
    while prosseguir == eventos[3]:  #sessão de cadastro paciente/medico
        if verificador_anticrash == False:
            caixa_login = gf.Entry(gf.Point(551,357),38)
            caixa_login.setFill(gf.color_rgb(218, 254, 236))
            caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,429),38)
            caixa_senha.setFill(gf.color_rgb(218, 254, 236))
            caixa_senha.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_senha.draw(janela)

            caixa_nome = gf.Entry(gf.Point(551,211),38)
            caixa_nome.setFill(gf.color_rgb(218, 254, 236))
            caixa_nome.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_nome.draw(janela)

            caixa_cpf = gf.Entry(gf.Point(551,284),38)
            caixa_cpf.setFill(gf.color_rgb(218, 254, 236))
            caixa_cpf.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_cpf.draw(janela)

            fundo_tela5.draw(janela)
        verificador_anticrash = True

        click = janela.getMouse()
        login = get_login()
        senha = get_senha()
        nome = get_nome()
        cpf = get_cpf()


        if (click.getX() >= 452 and click.getX() <= 648) and (click.getY() >= 586 and click.getY() <= 624):  #cadastro como paciente
            #verifica se o cadastro pode ser efetuado
            verificacao_cadastro = fazer_cadastro()
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_cadastro == True:
                login_atual = get_login()   #pega o e-mail do usuário atual
                apagar_tudo_cadastro()
                prosseguir = eventos[1]
            else:
                aviso_usuario_existente = gf.Text(gf.Point(550,465),"Usuário existente ou inválido.")
                aviso_usuario_existente.setTextColor(gf.color_rgb(0, 255, 128))
                aviso_usuario_existente.draw(janela)
                aviso_existente = True

        if (click.getX() >= 452 and click.getX() <= 648) and (click.getY() >= 647 and click.getY() <= 686): # cadastro como medico
            #verifica se o cadastro pode ser efetuado
            verificacao_cadastro_medico = fazer_cadastro_medico()
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_cadastro_medico == True:
                login_atual = get_login()   #pega o e-mail do usuário atual
                apagar_tudo_cadastro()
                prosseguir = eventos[2]
            else:
                aviso_usuario_existente = gf.Text(gf.Point(550,465),"Usuário existente ou inválido.")
                aviso_usuario_existente.setTextColor(gf.color_rgb(0, 255, 128))
                aviso_usuario_existente.draw(janela)
                aviso_existente = True

        if (click.getX() >= 179 and click.getX() <= 334) and (click.getY() >= 43 and click.getY() <= 102):
            apagar_tudo_cadastro()
            caixa_login = gf.Entry(gf.Point(551,315),37)
            caixa_login.setFill(gf.color_rgb(218, 254, 236))
            caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,415),37)
            caixa_senha.setFill(gf.color_rgb(218, 254, 236))
            caixa_senha.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_senha.draw(janela)

            fundo_tela1.draw(janela)

            prosseguir = eventos[0]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    verificador_anticrash = False
    while prosseguir == eventos[4]:  # Usuário - edição e vizualização dos exames
        exames_undraw()
        if verificador_anticrash == False:
            fundo_tela6.draw(janela)
        verificador_anticrash = True

        click = janela.getMouse()

        #Botão (voltar)
        if (click.getX() >= 101 and click.getX() <= 260) and (click.getY() >= 58 and click.getY() <= 119): 
            fundo_tela6.undraw()
            prosseguir = eventos[1]

        #Botão (ver meus exames) 
        if (click.getX() >= 352 and click.getX() <= 729) and (click.getY() >= 338 and click.getY() <= 412): 
            with open('dados_login.csv','r') as arquivo:  #pega o id do usuário atual
                for linha in arquivo:
                    lista = linha.split(';')
                    if login_atual in lista:
                        id_atual = lista[0]
                arquivo.close()

            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Hemácias </td> <td class="head"> Hemoglobina </td> <td class="head"> Hematócrito </td> <td class="head"> VCM </td> <td class="head"> HCM </td> <td class="head"> CHCM </td> <td class="head"> RDW </td> <td class="head"> Leucócitos </td> <td class="head"> Basófilos </td> <td class="head"> Eosinófilos </td> <td class="head"> Mielócitos </td> <td class="head"> Metamielócitos </td> <td class="head"> Bastões </td> <td class="head"> Segmentados </td> <td class="head"> Linfócitos </td> <td class="head"> Linfócitos atípicos </td> <td class="head"> Monócitos </td> <td class="head"> VPM </td> <td class="head"> Plaquetócrito </td> <td class="head"> PDW </td> <td class="head"> HDL </td> <td class="head"> LDL </td> <td class="head"> Data </td></tr>'
            with open('dados_exames.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    if linha[0] == id_atual:
                        saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[2]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td> <td> {linha[5]} </td> <td> {linha[6]} </td> <td> {linha[7]} </td> <td> {linha[8]} </td> <td> {linha[9]} </td> <td> {linha[10]} </td> <td> {linha[11]} </td> <td> {linha[12]} </td> <td> {linha[13]} </td> <td> {linha[14]} </td> <td> {linha[15]} </td> <td> {linha[16]} </td> <td> {linha[17]} </td> <td> {linha[18]} </td> <td> {linha[19]} </td> <td> {linha[20]} </td> <td> {linha[21]} </td> <td> {linha[22]} </td> <td> {linha[23]} </td> <td> {linha[24]} </td>')
                arquivo.close()
            saida = saida + '</table></body></html>'

            with open('relatorio_paciente_desejado.html','w', encoding="UTF-8") as html:
                html.write(saida)
                html.close()
            os.system('relatorio_paciente_desejado.html')

        #Botão (editar último exame) 
        if (click.getX() >= 352 and click.getX() <= 729) and (click.getY() >= 455 and click.getY() <= 529):
            fundo_tela6.undraw()
            prosseguir = eventos[5]


        #Botão (sair)
        if (click.getX() >= 469 and click.getX() <= 614) and (click.getY() >= 564 and click.getY() <= 622): 
            janela.close()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
    verificador_anticrash = False
    while prosseguir == eventos[5]:  #Editar último exame
        if verificador_anticrash == False:
            fundo_tela7.draw(janela)
            exames_draw()
            verificador_anticrash = True
        click = janela.getMouse()

        if (click.getX() >= 434 and click.getX() <= 667) and (click.getY() >= 665  and click.getY() <= 739): #pega os dados novos dos Entrys
            data_atual = data_entry.getText()
            saida = get_exames()

            with open('dados_login.csv','r') as arquivo:  #pega o id do usuário atual
                for linha in arquivo:
                    lista = linha.split(';')
                    if login_atual in lista:
                        id_atual = lista[0]
                arquivo.close()
            
            with open('dados_exames.csv','r',encoding='UTF-8') as arquivo:
                lista_dados_exames = arquivo.readlines()  #separa o arquivo em uma grande lista
                separador =''

                for i in lista_dados_exames:
                    lista_paciente = i[:-1].split(';')

                    if (id_atual == lista_paciente[0]) and (data_atual == lista_paciente[-1]):   #verifica se a data existe
                        texto_editado = id_atual + ';' + login_atual + ';' + saida + '\n'    #texto com a saida editada
                        index = lista_dados_exames.index(i)    #index da do elemento atual da lista
                        lista_dados_exames[index] = texto_editado  #reescreve elemento da lista

                        with open('dados_exames.csv','w',encoding='UTF-8') as arquivo_editado:
                            lista_dados_exames = separador.join(lista_dados_exames)  #junta a lista em uma string 
                            print(lista_dados_exames)
                            arquivo_editado.write(lista_dados_exames)
                            arquivo_editado.close()
                        prosseguir = eventos[4]
                        break
      
                    else:
                        aviso_data_incorreta = gf.Text(gf.Point(825,694),"Você não possui um exame com essa data.")
                        aviso_data_incorreta.setTextColor(gf.color_rgb(0, 255, 128))
                        aviso_data_incorreta.draw(janela)
                arquivo.close()
            fundo_tela7.undraw()

                    
