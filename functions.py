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

def fazer_login_medico(login,senha):
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

def fazer_login(login,senha): #verifica se as informações que o usuário digitou batem com o data base
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

def valida_email(login): #valida o email
    if ("@" in login) and (".com" in login ):
        return True
    else:
        return False

def fazer_cadastro(login,nome,cpf,senha): #faz o cadastro do usuário, gerando um id único
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

def fazer_cadastro_medico(login,nome,cpf,senha):
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

def exames_draw(janela,hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,hdl_entry,ldl_entry,data_entry): #desenha os obejtos da aba de exames
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

def exames_undraw(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,hdl_entry,ldl_entry,data_entry,fundo_tela3): #apaga os objetos e o background da aba de exames
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

def get_exames(hemacias_entry,hemoglobina_entry,hematocrito_entry,vcm_entry,hcm_entry,chcm_entry,rdw_entry,leucocitos_entry,basofilos_entry,eosinofilos_entry,mielocitos_entry,metamielocitos_entry,bastoes_entry,segmentados_entry,linfocitos_entry,linfocitos_atipicos_entry,monocitos_entry,plaquetas_entry,vpm_entry,plaquetocrito_entry,pdw_entry,hdl_entry,ldl_entry,data_entry): #pega os dados dos exames digitados
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


