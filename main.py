import graphics as gf
import random as rd
from datetime import datetime
import os
from functions import *

fundo_tela1 = gf.Image(gf.Point(550,400),"Login.png")
fundo_tela2 = gf.Image(gf.Point(550,400),"Cadastro.png")
fundo_tela3 = gf.Image(gf.Point(550,400),"Paciente_Editar_Exame.png")
fundo_tela4 = gf.Image(gf.Point(550,400),"Medico_Pesquisar.png")
fundo_tela5 = gf.Image(gf.Point(550,400),"Cadastro.png")
fundo_tela6 = gf.Image(gf.Point(550,400),"Paciente_Editar.png")
fundo_tela7 = gf.Image(gf.Point(550,400),"Paciente_Editar_Exame.png")
fundo_tela8 = gf.Image(gf.Point(550,400),"Paciente_Minha_Saude.png")

janela = gf.GraphWin("Analizador de hemograma",1100,800)
fundo_tela1.draw(janela)


caixa_login = gf.Entry(gf.Point(551,315),37)
caixa_login.setFill(gf.color_rgb(255, 255, 255))
caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
caixa_login.draw(janela)
                                                                      #criando objetos

caixa_senha = gf.Entry(gf.Point(551,415),37)
caixa_senha.setFill(gf.color_rgb(255, 255, 255))
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

triglicerideos_entry = gf.Entry(gf.Point(874,417),10)
triglicerideos_entry.setFill(gf.color_rgb(255,255,255))

hdl_entry = gf.Entry(gf.Point(874,461),10)   
hdl_entry.setFill(gf.color_rgb(255,255,255))

ldl_entry = gf.Entry(gf.Point(874,504),10)
ldl_entry.setFill(gf.color_rgb(255,255,255))

colesterol_entry = gf.Entry(gf.Point(874,547),10)
colesterol_entry.setFill(gf.color_rgb(255,255,255))

data_entry = gf.Entry(gf.Point(823,660),10)
data_entry.setFill(gf.color_rgb(255,255,255))



idade_entry = gf.Entry(gf.Point(535,386),38)
idade_entry.setFill(gf.color_rgb(255,255,255))

sexo_entry = gf.Entry(gf.Point(535,505),38)
sexo_entry.setFill(gf.color_rgb(255,255,255))


#textos

paciente_desejado_entry = gf.Entry(gf.Point(570,307),50)
paciente_desejado_entry.setFill(gf.color_rgb(255,255,255))


gf.update(10)

eventos = ["1","2",'3','4','5','6','7'] #eventos para direcionar o programa

aviso_incorreto = False
aviso_existente = False

prosseguir = eventos[0]     #Tela inicial
while True:
    if prosseguir == eventos[0]:
        click = janela.getMouse()
        login = get_login(caixa_login)
        senha = get_senha(caixa_senha)

        #LOGIN
        if (click.getX() >= 449 and click.getX() <= 646) and (click.getY() >= 489 and click.getY() <= 528):
            #verifica se o login pode ser efetuado
            verificacao_login = fazer_login(login,senha)
            #Verifica e remove se ja existe um aviso na tela
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            #testa se o login esta certo
            if verificacao_login == True:
                login_atual = get_login(caixa_login)  #pega o e-mail do usuário atual
                apagar_tudo(caixa_login,caixa_senha,fundo_tela1)
                prosseguir = eventos[1]
            else:
                aviso_usuario_incorreto = gf.Text(gf.Point(550,465),"E-mail ou senha inválidos.")
                aviso_usuario_incorreto.setTextColor(gf.color_rgb(92, 158, 224))
                aviso_usuario_incorreto.draw(janela)
                aviso_incorreto = True
                
        #CADASTRO
        if (click.getX() >= 449 and click.getX() <= 647) and (click.getY() >= 551 and click.getY() <= 588):
            caixa_login.undraw()
            caixa_senha.undraw()
            prosseguir = eventos[3]

        #LOGIN MÉDICO
        if (click.getX() >= 449 and click.getX() <= 647) and (click.getY() >= 613 and click.getY() <= 690):
            verificacao_login_medico = fazer_login_medico(login,senha)

            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_login_medico == True:
                login_atual = get_login(caixa_login)   #pega o e-mail do usuário atual
                apagar_tudo(caixa_login,caixa_senha,fundo_tela1)
                prosseguir = eventos[2]
            else:
                aviso_usuario_existente = gf.Text(gf.Point(550,465),"Email não cadastrado ou inválido")
                aviso_usuario_existente.setTextColor(gf.color_rgb(92, 158, 224))
                aviso_usuario_existente.draw(janela)
                aviso_existente = True

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    informacoes_desenhadas = False    #introdução dos dados dos exames
    while prosseguir == eventos[1]:
        if informacoes_desenhadas == False:
            fundo_tela3.draw(janela)
            exames_draw(janela,hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry)                               #objetos e caixas de entrada são desenhados

        informacoes_desenhadas = True #verifica se os objetos forma desenhados e evita o crash
        click = janela.getMouse()
        print(click)

        if (click.getX() >= 434 and click.getX() <= 667) and (click.getY() >= 665  and click.getY() <= 739):     #verifica as coordenadas e pega os dados dos Entrys
            data_atual = formata_data(data_entry)
            verificacao_inteiro = valida_inteiro(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_atual)
            verificacao_data = valida_data(data_entry)
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_inteiro == True and verificacao_data == True:
                saida = get_exames(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_atual)
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
            else:
                if verificacao_inteiro == True and verificacao_data == False:
                    aviso_usuario_existente = gf.Text(gf.Point(825,740),"Por favor, insira um formato válido \n para a data, assim como está no exemplo.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(92, 158, 224))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True
                else:
                    aviso_usuario_existente = gf.Text(gf.Point(825,740),"Insira apenas números \n nas informações do seu exame.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(92, 158, 224))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True

        if (click.getX() >= 106 and click.getX() <= 246) and (click.getY() >= 63 and click.getY() <= 118): #botão de voltar para página principal
            exames_undraw(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry,fundo_tela3)

            prosseguir = eventos[0]
            caixa_login = gf.Entry(gf.Point(551,315),37)
            caixa_login.setFill(gf.color_rgb(255, 255, 255))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,415),37)
            caixa_senha.setFill(gf.color_rgb(255, 255, 255))
            caixa_senha.draw(janela)

            fundo_tela1.draw(janela)
        
        if (click.getX() >= 195 and click.getX() <= 349) and (click.getY() >= 585 and click.getY() <= 652): #botão para ver os exames
            with open('dados_login.csv','r') as arquivo:  #pega o id do usuário atual
                for linha in arquivo:
                    lista = linha.split(';')
                    if login_atual in lista:
                        id_atual = lista[0]
                arquivo.close()

            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table><caption> Seus Exames </caption> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Hemacias </td> <td class="head"> Hemoglobina </td> <td class="head"> Hematocrito </td> <td class="head"> VCM </td> <td class="head"> HCM </td> <td class="head"> CHCM </td> <td class="head"> RDW </td> <td class="head"> Leucocitos </td> <td class="head"> Basofilos </td> <td class="head"> Eosinofilos </td> <td class="head"> Mielocitos </td> <td class="head"> Metamielocitos </td> <td class="head"> Bastoes </td> <td class="head"> Segmentados </td> <td class="head"> Linfocitos </td> <td class="head"> Linfocitos atipicos </td> <td class="head"> Monocitos </td> <td class="head"> Plaquetas </td> <td class="head"> VPM </td> <td class="head"> Plaquetocrito </td> <td class="head"> PDW </td> <td class="head"> Triglicerídeos </td> <td class="head"> HDL </td> <td class="head"> LDL </td> <td class="head"> Colesterol Total </td> <td class="head"> Data </td></tr>'
            with open('dados_exames.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    if linha[0] == id_atual:
                        saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[2]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td> <td> {linha[5]} </td> <td> {linha[6]} </td> <td> {linha[7]} </td> <td> {linha[8]} </td> <td> {linha[9]} </td> <td> {linha[10]} </td> <td> {linha[11]} </td> <td> {linha[12]} </td> <td> {linha[13]} </td> <td> {linha[14]} </td> <td> {linha[15]} </td> <td> {linha[16]} </td> <td> {linha[17]} </td> <td> {linha[18]} </td> <td> {linha[19]} </td> <td> {linha[20]} </td> <td> {linha[21]} </td> <td> {linha[22]} </td> <td> {linha[23]} </td> <td> {linha[24]} </td> <td> {linha[25]} </td> <td> {linha[26]} </td> <td> {linha[27]} </td>')
                arquivo.close()
            saida = saida + '</table></body></html>'

            with open('relatorio_paciente_desejado.html','w', encoding="UTF-8") as html:
                html.write(saida)
                html.close()
            os.system('relatorio_paciente_desejado.html')
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
    verificador_anticrash = False
    while prosseguir == eventos[2]:    #seleção de pacientes do médico
        exames_undraw(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry,fundo_tela3)
        if verificador_anticrash == False:    #evita crash e permite o loop do programa
            fundo_tela4.draw(janela)
            paciente_desejado_entry.draw(janela)

        verificador_anticrash = True
        click = janela.getMouse()
        print(click)

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
            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table><caption> Exames de ' +str(paciente_desejado)+ '</caption> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Hemacias </td> <td class="head"> Hemoglobina </td> <td class="head"> Hematocrito </td> <td class="head"> VCM </td> <td class="head"> HCM </td> <td class="head"> CHCM </td> <td class="head"> RDW </td> <td class="head"> Leucocitos </td> <td class="head"> Basofilos </td> <td class="head"> Eosinofilos </td> <td class="head"> Mielocitos </td> <td class="head"> Metamielocitos </td> <td class="head"> Bastoes </td> <td class="head"> Segmentados </td> <td class="head"> Linfocitos </td> <td class="head"> Linfocitos atipicos </td> <td class="head"> Monocitos </td> <td class="head"> Plaquetas </td> <td class="head"> VPM </td> <td class="head"> Plaquetocrito </td> <td class="head"> PDW </td> <td class="head"> Triglicerídeos </td> <td class="head"> HDL </td> <td class="head"> LDL </td> <td class="head"> Colesterol Total </td> <td class="head"> Data </td></tr>'
            with open('dados_exames.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    if linha[0] == paciente_desejado:
                        saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[2]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td> <td> {linha[5]} </td> <td> {linha[6]} </td> <td> {linha[7]} </td> <td> {linha[8]} </td> <td> {linha[9]} </td> <td> {linha[10]} </td> <td> {linha[11]} </td> <td> {linha[12]} </td> <td> {linha[13]} </td> <td> {linha[14]} </td> <td> {linha[15]} </td> <td> {linha[16]} </td> <td> {linha[17]} </td> <td> {linha[18]} </td> <td> {linha[19]} </td> <td> {linha[20]} </td> <td> {linha[21]} </td> <td> {linha[22]} </td> <td> {linha[23]} </td> <td> {linha[24]} </td> <td> {linha[25]} </td> <td> {linha[26]} </td> <td> {linha[27]} </td>')
                arquivo.close()

            saida = saida + '</table></body></html>'

            with open('relatorio_paciente_desejado.html','w',encoding="UTF-8") as html:
                html.write(saida)
                html.close()
            os.system('relatorio_paciente_desejado.html')
        
        if (click.getX() >= 110 and click.getX() <= 270) and (click.getY() >= 70 and click.getY() <= 123): #botão de voltar para página principal
            paciente_desejado_entry.undraw()
            fundo_tela4.undraw()
            
            caixa_login = gf.Entry(gf.Point(551,315),37)
            caixa_login.setFill(gf.color_rgb(255, 255, 255))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,415),37)
            caixa_senha.setFill(gf.color_rgb(255, 255, 255))
            caixa_senha.draw(janela)

            fundo_tela1.draw(janela)

            prosseguir = eventos[0]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    verificador_anticrash = False
    while prosseguir == eventos[3]:  #sessão de cadastro paciente/medico
        if verificador_anticrash == False:
            caixa_login = gf.Entry(gf.Point(551,357),38)
            caixa_login.setFill(gf.color_rgb(255, 255, 255))
            caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,429),38)
            caixa_senha.setFill(gf.color_rgb(255, 255, 255))
            caixa_senha.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_senha.draw(janela)

            caixa_nome = gf.Entry(gf.Point(551,211),38)
            caixa_nome.setFill(gf.color_rgb(255, 255, 255))
            caixa_nome.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_nome.draw(janela)

            caixa_cpf = gf.Entry(gf.Point(551,284),38)
            caixa_cpf.setFill(gf.color_rgb(255, 255, 255))
            caixa_cpf.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_cpf.draw(janela)

            fundo_tela5.draw(janela)
        verificador_anticrash = True

        click = janela.getMouse()
        login = get_login(caixa_login)
        senha = get_senha(caixa_senha)
        nome = get_nome(caixa_nome)
        cpf = get_cpf(caixa_cpf)


        if (click.getX() >= 452 and click.getX() <= 648) and (click.getY() >= 586 and click.getY() <= 624):  #cadastro como paciente
            #verifica se o cadastro pode ser efetuado
            verificacao_cadastro = fazer_cadastro(login,nome,cpf,senha)
            verificacao_cpf = valida_cpf(cpf)
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_cadastro == True and verificacao_cpf == True:
                login_atual = get_login(caixa_login)   #pega o e-mail do usuário atual
                apagar_tudo_cadastro(caixa_login,caixa_senha,fundo_tela1,caixa_nome,caixa_cpf,fundo_tela5)
                prosseguir = eventos[1]
            else:
                if verificacao_cadastro == True and verificacao_cpf == False:
                    aviso_usuario_existente = gf.Text(gf.Point(550,465),"CPF inválido.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(255,255,255))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True
                else:
                    aviso_usuario_existente = gf.Text(gf.Point(550,465),"Usuário existente ou inválido.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(255,255,255))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True


        if (click.getX() >= 452 and click.getX() <= 648) and (click.getY() >= 647 and click.getY() <= 686): # cadastro como medico
            #verifica se o cadastro pode ser efetuado
            verificacao_cadastro_medico = fazer_cadastro_medico(login,nome,cpf,senha)
            verificacao_cpf = valida_cpf(cpf)
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_cadastro_medico == True and verificacao_cpf == True:
                login_atual = get_login(caixa_login)   #pega o e-mail do usuário atual
                apagar_tudo_cadastro(caixa_login,caixa_senha,fundo_tela1,caixa_nome,caixa_cpf,fundo_tela5)
                prosseguir = eventos[2]
            else:
                if verificacao_cadastro_medico == True and verificacao_cpf == False:
                    aviso_usuario_existente = gf.Text(gf.Point(550,465),"CPF inválido.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(255,255,255))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True
                else:
                    aviso_usuario_existente = gf.Text(gf.Point(550,465),"Usuário existente ou inválido.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(255,255,255))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True


        if (click.getX() >= 179 and click.getX() <= 334) and (click.getY() >= 43 and click.getY() <= 102): #botão de voltar para página principal
            apagar_tudo_cadastro(caixa_login,caixa_senha,fundo_tela1,caixa_nome,caixa_cpf,fundo_tela5)
            caixa_login = gf.Entry(gf.Point(551,315),37)
            caixa_login.setFill(gf.color_rgb(255, 255, 255))
            caixa_login.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_login.draw(janela)

            caixa_senha = gf.Entry(gf.Point(551,415),37)
            caixa_senha.setFill(gf.color_rgb(255, 255, 255))
            caixa_senha.setTextColor(gf.color_rgb(0, 0, 0))
            caixa_senha.draw(janela)

            fundo_tela1.draw(janela)

            prosseguir = eventos[0]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    verificador_anticrash = False
    while prosseguir == eventos[4]:  # Usuário - edição e vizualização dos exames
        exames_undraw(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry,fundo_tela3)
        if verificador_anticrash == False:
            fundo_tela6.draw(janela)
        verificador_anticrash = True

        click = janela.getMouse()
        print(click)

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

            saida = '<html lang = "pt-br"><head><meta charset = "UTF-8"><title> Formulario </title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><table> <tr><td class="head"> ID </td> <td class="head"> Email </td> <td class="head"> Hemácias </td> <td class="head"> Hemoglobina </td> <td class="head"> Hematócrito </td> <td class="head"> VCM </td> <td class="head"> HCM </td> <td class="head"> CHCM </td> <td class="head"> RDW </td> <td class="head"> Leucócitos </td> <td class="head"> Basófilos </td> <td class="head"> Eosinófilos </td> <td class="head"> Mielócitos </td> <td class="head"> Metamielócitos </td> <td class="head"> Bastões </td> <td class="head"> Segmentados </td> <td class="head"> Linfócitos </td> <td class="head"> Linfócitos atípicos </td> <td class="head"> Monócitos </td> <td class="head"> Plaquetas </td> <td class="head"> VPM </td> <td class="head"> Plaquetócrito </td> <td class="head"> PDW </td> <td class="head"> Triglicerídeos </td> <td class="head"> HDL </td> <td class="head"> LDL </td> <td class="head"> Colesterol Total </td> <td class="head"> Data </td></tr>'
            with open('dados_exames.csv','r') as arquivo:
                for linha in arquivo:
                    linha = linha[:-1].split(";")
                    print(len(linha))
                    if linha[0] == id_atual:
                        saida += (f'<tr><td> {linha[0]} </td><td> {linha[1]} </td> <td> {linha[2]} </td> <td> {linha[3]} </td> <td> {linha[4]} </td> <td> {linha[5]} </td> <td> {linha[6]} </td> <td> {linha[7]} </td> <td> {linha[8]} </td> <td> {linha[9]} </td> <td> {linha[10]} </td> <td> {linha[11]} </td> <td> {linha[12]} </td> <td> {linha[13]} </td> <td> {linha[14]} </td> <td> {linha[15]} </td> <td> {linha[16]} </td> <td> {linha[17]} </td> <td> {linha[18]} </td> <td> {linha[19]} </td> <td> {linha[20]} </td> <td> {linha[21]} </td> <td> {linha[22]} </td> <td> {linha[23]} </td> <td> {linha[24]} </td> <td> {linha[25]} </td> <td> {linha[26]} </td> <td> {linha[27]} </td>')
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
        if (click.getX() >= 463 and click.getX() <= 605) and (click.getY() >= 665 and click.getY() <= 719): 
            janela.close()

        #Botão (minha saúde)
        if (click.getX() >= 357 and click.getX() <= 730) and (click.getY() >= 571 and click.getY() <= 639): 
            fundo_tela6.undraw()
            prosseguir = eventos[6]
            
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
    verificador_anticrash = False
    while prosseguir == eventos[5]:  #Editar último exame
        if verificador_anticrash == False:
            fundo_tela7.draw(janela)
            exames_draw(janela,hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry)
            verificador_anticrash = True

        click = janela.getMouse()
        print(click)

        if (click.getX() >= 434 and click.getX() <= 667) and (click.getY() >= 665  and click.getY() <= 739): #pega os dados novos dos Entrys
            data_atual = formata_data(data_entry)
            verificacao_inteiro = valida_inteiro(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_atual)
            verificacao_data = valida_data(data_entry)
            #Verifica e remove se ja existe um aviso na tela, evitando crash
            if aviso_existente == True:
                aviso_usuario_existente.undraw()
            if aviso_incorreto == True:
                aviso_usuario_incorreto.undraw()

            if verificacao_inteiro == True and verificacao_data == True:
                saida = get_exames(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_atual)

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
                            aviso_data_incorreta = gf.Text(gf.Point(825,740),"Você não possui um exame com essa data.")
                            aviso_data_incorreta.setTextColor(gf.color_rgb(92, 158, 224))
                            aviso_data_incorreta.draw(janela)
                    arquivo.close()
                fundo_tela7.undraw()
            else:
                if verificacao_inteiro == True and verificacao_data == False:
                    aviso_usuario_existente = gf.Text(gf.Point(825,740),"Por favor, insira um formato válido \n para a data, assim como está no exemplo.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(92, 158, 224))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True
                else:
                    aviso_usuario_existente = gf.Text(gf.Point(825,740),"Insira apenas números \n nas informações do seu exame.")
                    aviso_usuario_existente.setTextColor(gf.color_rgb(92, 158, 224))
                    aviso_usuario_existente.draw(janela)
                    aviso_existente = True
        
        if (click.getX() >= 104 and click.getX() <= 246) and (click.getY() >= 64 and click.getY() <= 120): # botão de voltar
            exames_undraw(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_entry,fundo_tela3)
            fundo_tela7.undraw()
            prosseguir = eventos[4]
            
            
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
    verificador_anticrash = False
    while prosseguir == eventos[6]:  #Minha Saúde
        if verificador_anticrash == False:
            fundo_tela8.draw(janela)
            verificador_anticrash = True
            idade_sexo_draw(janela,idade_entry,sexo_entry)
        click = janela.getMouse()
        #print(click)
        
        if (click.getX() >= 104 and click.getX() <= 246) and (click.getY() >= 64 and click.getY() <= 120): # botão de voltar
            idade_sexo_undraw(idade_entry,sexo_entry)
            fundo_tela8.undraw()
            prosseguir = eventos[4]
            
        if (click.getX() >= 404 and click.getX() <= 695) and (click.getY() >= 638 and click.getY() <= 727): #gerar relatório
            lista = get_idade_sexo(idade_entry,sexo_entry)
            idade = lista[0]
            sexo = lista[1]
            
            if validar_idade_sexo(idade,sexo) == True:
                teste_de_saude(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,triglicerideos_entry,hdl_entry,ldl_entry,colesterol_entry,data_atual,idade,sexo)
                os.system('relatorio_minha_saude.html')
                
            else:
                aviso_data_incorreta = gf.Text(gf.Point(545,550),"Idade ou sexo inválido(a)")
                aviso_data_incorreta.setTextColor(gf.color_rgb(0, 17, 93))
                aviso_data_incorreta.draw(janela)
            
