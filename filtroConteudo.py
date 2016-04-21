import string
# coding: utf-8

def pesquisaPalavra(dados):
	''' Pesquisa palavras dentro da string dados'''
	try:
		arq = open('palavras.conf')
		html = open(dados).read()
		for palavra in arq:
			palavra = palavra.replace('\n', '')
			if palavra in html:
				return True
		return False
	except IOError:
		return False
	
def verificaDominio(host):
	'''Verifica se host tem permissão'''
	try:
		arq = open('teste.conf')
		for dominio in arq:
			dominio = dominio.replace('\n', '')
			print dominio
			if dominio == host:
				return True
		return False
	except IOError:
		return False
