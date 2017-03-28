# -*- coding: UTF-8 -*-
# descontos.py

class Desconto_por_cinco_itens(object):

	def __init__(self, proximo_desconto):
  		self.__proximo_desconto = proximo_desconto

  	def calcular(self, orcamento):

  		if(orcamento.total_itens > 5):
  			return orcamento.valor * 0.1
  		else: 
  			return self.__proximo_desconto.calcular(orcamento)

class Desconto_por_mais_de_quinhentos_reais(object):

	def __init__(self, proximo_desconto):
		self.__proximo_desconto = proximo_desconto

	def calcular(self, orcamento):

		if(orcamento.valor > 500):
			return orcamento.valor * 0.07
		else:
			return self.__proximo_desconto.calcular(orcamento)


class Sem_desconto(object):
	def calcular(self, orcamento):
		return 0
		
      