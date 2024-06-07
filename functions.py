import random as rd

def get_login(caixa_login): #pega a informação de login
    login = caixa_login.getText()
    return login

def get_senha(caixa_senha): #pega a senha
    senha = caixa_senha.getText()
    return senha

def get_nome(caixa_nome):
    nome = caixa_nome.getText()
    return nome

def get_cpf(caixa_cpf):
    cpf = caixa_cpf.getText()
    return cpf

def get_id(login_atual):
    with open('dados_login.csv','r') as arquivo:  #pega o id do usuário atual
        for linha in arquivo:
            lista = linha.split(';')
            if login_atual in lista:
                id_atual = lista[0]
        arquivo.close()
        return id_atual

def escreve_dados_exames(saida,login_atual):
    id_atual = get_id(login_atual)

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

def fazer_login_medico(login,senha):
    dados_usuario_format = login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    with open("dados_login_medico.csv", "r",encoding='UTF-8') as arquivo:
      for linha in arquivo:
        linha = linha[0:-1].split(';')

        if dados_usuario_format[0] == linha[1] and dados_usuario_format[1] == linha[2]:
          verificacao_login_medico = True
          break
        else:
          verificacao_login_medico = False
      arquivo.close()
      return verificacao_login_medico

def fazer_login(login,senha): #verifica se as informações que o usuário digitou batem com o data base
    dados_usuario_format = login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    with open("dados_login.csv", "r",encoding='UTF-8') as arquivo:
      for linha in arquivo:
        linha = linha[0:-1].split(';')

        if dados_usuario_format[0] == linha[1] and dados_usuario_format[1] == linha[2]:
          verificacao_login = True
          break
        else:
          verificacao_login = False
      arquivo.close()
      return verificacao_login

def valida_email(login): #valida o email
    if ("@" in login) and (".com" in login ):
        return True
    else:
        return False

def fazer_cadastro(login,nome,cpf,senha): #faz o cadastro do usuário, gerando um id único
    #testa se o id já existe:
    id_valido = False
    while id_valido == False:
        with open("dados_login.csv","r",encoding='UTF-8') as arquivo:
            id_gerado = gera_id()
            for linha in arquivo:
                lista = linha[0:-1].split(';') #transforma a linha em uma lista removendo o '\n'
                if id_gerado != lista[0]: #compara o id_gerado com a posição[0] da lista
                    id_valido = True
                else:
                    id_valido = False
            arquivo.close()

    #testa se o cadastro é válido
    cpf = formata_cpf(cpf)
    dados_usuario = id_gerado + ';' + login + ';' + senha + ";" + nome + ';' + cpf + '\n'
    dados_usuario_format = id_gerado + ';' + login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    verificacao_cadastro = False
    verificacao_cpf = False
    if (login!='') and (senha!=''):
        valido = valida_email(login)
        if valido == True:
            with open("dados_login.csv","r",encoding='UTF-8') as arquivo1:
                for linha in arquivo1:
                    split_linha = linha[0:-1].split(';')

                    if dados_usuario_format[1] == split_linha[1]:
                        verificacao_cadastro = False
                        break
                    else:
                        verificacao_cadastro = True
                        verificacao_cpf = valida_cpf(cpf)
                arquivo1.close()
                if (verificacao_cadastro == True) and (verificacao_cpf == True):
                    with open('dados_login.csv','a',encoding='UTF-8') as arquivo2:
                            arquivo2.write(dados_usuario)
                            arquivo2.close()
        else:
            verificacao_cadastro = False
    else:
        verificacao_cadastro = False
    return verificacao_cadastro

def fazer_cadastro_medico(login,nome,cpf,senha):
    #testa se o id já existe:
    id_valido = False
    while id_valido == False:
        with open("dados_login_medico.csv","r",encoding='UTF-8') as arquivo:
            id_gerado = gera_id()
            for linha in arquivo:
                lista = linha[0:-1].split(';') #transforma a linha em uma lista removendo o '\n'
                if id_gerado != lista[0]: #compara o id_gerado com a posição[0] da lista
                    id_valido = True
                else:
                    id_valido = False
            arquivo.close()

    #testa se o cadastro é válido
    cpf = formata_cpf(cpf)
    dados_usuario = id_gerado + ';' + login + ';' + senha + ";" + nome + ';' + cpf + '\n'
    dados_usuario_format = id_gerado + ';' + login + ';' + senha
    dados_usuario_format = dados_usuario_format.split(';')
    verificacao_cpf = False
    verificacao_cadastro_medico = False
    if (login!='') and (senha!=''):
        valido = valida_email(login)
        if valido == True:
            with open("dados_login_medico.csv","r",encoding='UTF-8') as arquivo1:
                for linha in arquivo1:
                    split_linha = linha[0:-1].split(';')

                    if dados_usuario_format[1] == split_linha[1]:
                        verificacao_cadastro_medico = False
                        break
                    else:
                        verificacao_cadastro_medico = True
                        verificacao_cpf = valida_cpf(cpf)
                arquivo1.close()
                if (verificacao_cadastro_medico == True) and (verificacao_cpf == True):
                    with open('dados_login_medico.csv','a',encoding='UTF-8') as arquivo2:
                            arquivo2.write(dados_usuario)
                            arquivo2.close()
        else:
            verificacao_cadastro_medico = False
    else:
        verificacao_cadastro_medico = False
    return verificacao_cadastro_medico

def exames_draw(lista_entrys): #desenha os obejtos da aba de exames
    for var in lista_entrys[1:]:
        var.draw(lista_entrys[0])
    
def exames_undraw(lista_entrys): #apaga os objetos e o background da aba de exames
    for var in lista_entrys[1:]:
        var.undraw()

def get_exames(lista_entrys,data_atual): #pega os dados dos exames digitados
    texto_exames = lista_entrys[1].getText()
    for info in lista_entrys[2:26]:
        texto_exames = texto_exames + ';' + info.getText()
    texto_exames = texto_exames + ';' + data_atual

    print(texto_exames)

    #texto_exames = hemacias_get+';'+hemoglobina_get+';'+hematocrito_get+';'+vcm_get+';'+hcm_get+';'+chcm_get+';'+rdw_get+';'+leucocitos_get+';'+basofilos_get+';'+eosinofilos_get+';'+mielocitos_get+';'+metamielocitos_get+';'+bastoes_get+';'+segmentados_get+';'+linfocitos_get+';'+linfocitos_atipicos_get+';'+monocitos_get+';'+plaquetas_get+';'+vpm_get+';'+plaquetocrito_get+';'+pdw_get+';'+triglicerideos_get+';'+hdl_get+';'+ldl_get+';'+colesterol_get+';'+data_get
    return texto_exames

def apagar_tudo(caixa_login,caixa_senha,fundo_tela1): #apaga os obejtos do primeiro evento
    caixa_login.undraw()
    caixa_senha.undraw()
    fundo_tela1.undraw()

def apagar_tudo_cadastro(caixa_login,caixa_senha,fundo_tela1,caixa_nome,caixa_cpf,fundo_tela5):
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

def valida_cpf(cpf):
    cont = 1
    cont_10 = 10
    cont_11 = 11
    soma10 = 0
    soma11 = 0
    verificacao_cpf = False
    validos = ['1','2','3','4','5','6','7','8','9','0']

    if '.' in cpf:
        cpf = cpf.replace('.','')
    if '-' in cpf:
        cpf = cpf.replace('-','')

    if len(cpf) != 11:
        verificacao_cpf = False
    else:
        for num in cpf:
            if num not in validos:
                verificacao_cpf = False
                break
            if cont_10 > 1:
                soma10 = soma10 + (int(num) * cont_10)
            if cont_11 > 1:
                soma11 = soma11 + (int(num) * cont_11)
            cont_10 = cont_10 - 1
            cont_11 = cont_11 - 1
            cont = cont + 1

        verificação1 = 11 - (soma10 % 11)
        verificação2 = 11 - (soma11 % 11)

        if verificação1 == 10:
            verificação1 = 0
        if verificação2 == 10:
            verificação2 = 0

        if str(verificação1) == cpf[9] and str(verificação2) == cpf[10]:
            verificacao_cpf = True
        else:
            verificacao_cpf = False
        
    return verificacao_cpf

def formata_cpf(cpf):
    cont = 1
    num_comp = ''
    if '.' in cpf:
        cpf = cpf.replace('.','')
    if '-' in cpf:
        cpf = cpf.replace('-','')

    for num in cpf:
        if cont == 3:
            num_comp = num_comp + num + "."
        elif cont == 6:
            num_comp = num_comp + num + "."
        elif cont == 9:
            num_comp = num_comp + num + "-"
        else:
            num_comp = num_comp + num
        cont = cont + 1
    return num_comp

def valida_inteiro(lista_entrys,data_atual):
    informacoes = get_exames(lista_entrys,data_atual)
    lista_informacoes = informacoes.split(';')
    informacoes = informacoes.replace(';','')
    informacoes = informacoes.replace('/','')
    inteiros = ['1','2','3','4','5','6','7','8','9','0']

    for num in lista_informacoes:
        if num == '':
            lista_informacoes.remove(num)
    print(lista_informacoes)

    if len(lista_informacoes) != 26:
        verificacao_inteiro = False
    else:
        for iten in informacoes:
            if iten not in inteiros:
                verificacao_inteiro = False
                break
            else:
                verificacao_inteiro = True

    return verificacao_inteiro

def valida_data(data_entry):
    data = data_entry.getText()
    dia = ''
    mes = ''
    ano = ''
    verificacao_data = False

    if '/' in data:
        data = data.replace('/','')

    if len(data) != 8:
        verificacao_data = False

    else:
        cont = 1
        for num in data:
            if cont <= 2:
                dia = dia + num
            elif cont <= 4 and cont > 2:
                mes = mes + num
            elif cont <= 8 and cont > 4:
                ano = ano + num
            cont = cont + 1
        print(dia, mes, ano)
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if dia <= 0 or dia > 31 or mes <= 0 or mes > 12 or ano <= 0:
            verificacao_data = False
        else:
            if ano % 4 == 0:
                if (dia > 29 and mes == 2) or (dia > 30 and mes == 4) or (dia > 30 and mes == 6) or (dia > 30 and mes == 9) or (dia > 30 and mes == 11):
                    verificacao_data = False
                else:
                    verificacao_data = True
            else:
                if (dia > 28 and mes == 2) or (dia > 30 and mes == 4) or (dia > 30 and mes == 6) or (dia > 30 and mes == 9) or (dia > 30 and mes == 11):
                    verificacao_data = False
                else:
                    verificacao_data = True
            
            data = str(f'{data[0] + data[1]}/{data[2] + data[3]}/{data[4] + data[5] + data[6] + data[7]}')
    return verificacao_data

def formata_data(data_entry):
    data = data_entry.getText()
    dia = ''
    mes = ''
    ano = ''

    if '/' in data:
        data = data.replace('/','')
    
    cont = 1
    for num in data:
        if cont <= 2:
            dia = dia + num
        elif cont <= 4 and cont > 2:
            mes = mes + num
        elif cont <= 8 and cont > 4:
            ano = ano + num
            cont = cont + 1

    if len(data) != 8:
        data = '55/55/5555'  #para invalida-lá
    
    data = str(f'{data[0] + data[1]}/{data[2] + data[3]}/{data[4] + data[5] + data[6] + data[7]}')
    return data

def idade_sexo_draw(janela,idade_entry,sexo_entry):
    idade_entry.draw(janela)
    sexo_entry.draw(janela)

def get_idade_sexo(idade_entry,sexo_entry):
    idade = idade_entry.getText()
    sexo = sexo_entry.getText()
    lista = [idade,sexo]
    return lista
    
def idade_sexo_undraw(idade_entry,sexo_entry):
    idade_entry.undraw()
    sexo_entry.undraw()
    
def validar_idade_sexo(idade,sexo):
    idade_valida = False
    sexo_valido = False
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    
    if (idade != '') and (sexo != ''):
        for num in idade:
            if num not in numeros:
                idade_valida = False
                break
            else:
                if (int(idade) > 0) and (int(idade)<120):
                    idade_valida = True
                if (sexo=='f') or (sexo=='F') or (sexo=='m') or (sexo=='M'):
                    sexo_valido = True
    
    if (sexo_valido==True) and (idade_valida==True):
        return True
    else:
        return False
        
def teste_de_saude(lista_entrys,idade,sexo,data_atual):
    texto_exames = get_exames(lista_entrys,data_atual)
    lista = texto_exames.split(';')

    with open('relatorio_minha_saude.html','w', encoding='UTF-8') as arq:
        niveis = ['Valor desejado','Intermediário','Elevado','Alto','Baixo']
        saida = '<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="style.css"><title>Minha Saúde</title></head><body><table><caption>Análise do Hemograma</caption> '
        cont = 0
        while cont < len(lista):
            #TRIGLICERIDEOS
            if cont==21:
                if int(idade) <= 19:
                    if int(lista[cont]) <= 130:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) > 130:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>{niveis[2]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')

                elif int(idade) > 19:
                    if int(lista[cont]) < 150:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) >= 150 and int(lista[cont]) < 200:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>{niveis[1]}</td><tr>')
                    elif int(lista[cont]) >= 200:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>{niveis[2]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Triglicerídeos</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')
                        
                        
            #COLESTEROL HDL
            if cont==22:
                if int(idade) < 10:
                    if int(lista[cont]) >= 40:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) < 40:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[4]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')                    
                        
                elif int(idade) >= 10 and int(idade) <= 19:
                    if int(lista[cont]) >= 35:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) < 35:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[4]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')                        
                        
                elif int(idade) > 19:
                    if int(lista[cont]) < 40:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[4]}</td><tr>')
                    elif int(lista[cont]) >= 40 and int(idade) < 60:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[1]}</td><tr>')
                    elif int(lista[cont]) >= 60:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Colesterol HDL</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')
                    
                    
                
            #COLESTEROL LDL                                         
            if cont==23:
                if int(lista[cont]) < 130:
                    saida += (f'<tr><td>Colesterol LDL</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                elif int(lista[cont]) >= 130 and int(lista[cont]) < 160:
                    saida += (f'<tr><td>Colesterol LDL</td><td>{lista[cont]}</td><td>{niveis[1]}</td><tr>')
                elif int(lista[cont]) >= 160:
                    saida += (f'<tr><td>Colesterol LDL</td><td>{lista[cont]}</td><td>{niveis[3]}</td><tr>')
                else:
                    saida += (f'<tr><td>Colesterol LDL</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')
                    
            #COLESTEROL TOTAL
            if cont==24:
                if int(idade) < 19:
                    if int(lista[cont]) < 170:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) >= 170 and int(lista[cont]) < 200:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[1]}</td><tr>')
                    elif int(lista[cont]) >= 200:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[3]}</td><tr>')
                    else:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')                        
                
                elif int(idade) >= 19:
                    if int(lista[cont]) < 200:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[0]}</td><tr>')
                    elif int(lista[cont]) >= 200 and int(lista[cont]) < 250:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[1]}</td><tr>')
                    elif int(lista[cont]) >= 250:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>{niveis[3]}</td><tr>')    
                    else:
                        saida += (f'<tr><td>Colesterol Total</td><td>{lista[cont]}</td><td>O valor informado é inválido</td><tr>')            
            cont += 1
        
        #CALCULADORA DE RITMO CARDIACO
        if sexo == 'f' or sexo == 'F':
            freq_max = 226 - int(idade)
        elif sexo == 'm' or sexo == 'M':
            freq_max = 220 - int(idade)
        saida += (f'</table><br><br><table><caption>Frequência Cardíaca Máxima (FCMáx)</caption><tr><td class="head">Idade</td><td class="head">FCMáx</td></tr><tr><td>{idade} Anos</td><td>{freq_max} bpm</td></tr></table></body></html>')
        arq.write(saida)        
        arq.close()
