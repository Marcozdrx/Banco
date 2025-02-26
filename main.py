from contabancaria import ContaCorrente, CartaoCredito
# programa

#cria uma nova instancia da classe ContaCorrente(conta_lira)
conta_lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)

cartao_lira = CartaoCredito("Lira", conta_lira)