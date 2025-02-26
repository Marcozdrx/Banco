from datetime import datetime
from random import pytz
from random import randint

class ContaCorrente():
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/#Y %H:%M:%S')
    

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite - None
        self._agencia = agencia
        self._num_conta - num_conta
        self._transacoes = []
        self._cartoes = []
    
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))
        pass

    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self._saldo -valor < self._limite_conta():
            print('Voce não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self):
        print('Historico de transaoes: ')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(100000000000000000, 99999999999999999)
        self.titular = titular 
        self.validade = None
        self.cod_segurança = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)


# programa

conta_maeLira = ContaCorrente('Beth', '222.333.444-55', 5555, 656565)

conta_lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)

cartao_lira = CartaoCredito("Lira", conta_lira)

print(cartao_lira.__dict__)

cartao_lira.numero = 123

print(cartao_lira.conta_corrente._num_conta)

print(conta_lira._cartoes)

print(conta_lira._cartoes[0].numero)


#depositar um dinheirinho na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

conta_lira.transferir(1000, conta_maeLira)

#sacando um dinheirinho na conta:
conta_lira.sacar_dinheiro(1000000)
conta_lira.consultar_saldo

#saldo via metodos
print(conta_lira._saldo)

#tentando mudar o valor do saldo por fora do programa
conta_lira._saldo = 8000

#novo valor apos a tentativa de burlar o sistema
print(conta_lira._saldo)


print('Saldo Final:')
conta_lira.consultar_saldo()