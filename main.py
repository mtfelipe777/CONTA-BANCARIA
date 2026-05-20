from conta import Conta
acesso = Conta()



while True:
    print("1.Saca;")
    print("2.Deposita;")
    print("3.Calcula Rendimento;")
    print("4.Imprimir Dados.")
    acao = int(input("Informe a opção: "))

    if acao == 1:
        acesso.saca()
    elif acao == 2:
        acesso.deposita()
    elif acao == 3:
        acesso.calcula_Rendimento()
    elif acao == 4:
        acesso.imprimir_dados()
    else:
        break
