# coding: utf-8

import os

def pesquisaCache(host, nomeArquivo):
    ''' Pesquisa um arquivo em disco. Se existir retorna seu conteúdo.
        Caso contrario retorna False.
    '''
    if not nomeArquivo:
        nomeArquivo = '/index.html'

    return abreArquivo(host + '/' + nomeArquivo)
    
    
def abreArquivo(nomeArquivo):
    ''' Abre um arquivo em disco caso ele exista em modo leitura.
        Retorna seu conteúdo ou False em caso de erro.
    '''
    try:
        arq = open(nomeArquivo).read()
    except IOError:
        return False
    return arq


def separaUrl(host):
    url = host.split('.')
    print url
    for i in url:
        if(os.path.exists(i) and os.path.isdir(i)):
            os.chdir(i)
        else:
            os.mkdir(i)
            os.chdir(i)
        print i
    print 'Diretorio criado'
    
separaUrl('www.barbacena.ifsudestemg.edu.br/biblioteca')
    
'''def leDados(nomeArquivo, qtdeDados)

def gravaArquivoCache(host, nomeArquivo, conteudo):
     Grava um arquivo em disco. Cria uma pasta, caso não exista,
        com nome do host.
    try:
        mkdir(host)
    except OSError:
        pass
    
    if not nomeArquivo:
            nomeArquivo = 'index.html'
    open(host + '/' + nomeArquivo, 'w+').write(conteudo)'''

