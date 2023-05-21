# Vamos criar uma classe para clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido") #indica que uma exceção ocorreu. A classe Cliente não será criada.

    def mudar_plano(self, novo_plano):
            if novo_plano in self.lista_planos:
                self.plano = novo_plano
            else:
                print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
            if self.plano == plano_filme:
                print(f"Ver filme {filme}") #redirecionar para a página para o cliente assistir o filme
            elif self.plano == "premium":
                print(f"Ver filme {filme}")
            elif self.plano == "basic" and plano_filme == "premium":
                print("Faça upgrade para premium para ver esse filme")
            else:
                print("Plano inválido")

#testes de classe
#criado um cliente com o plano basic
cliente = Cliente("Mariana", "mariana@gmail.com", "basic")

#exibir o plano do cliente
print("O plano do cliente é:", cliente.plano)

# #Cliente assistir a um filme do plano premium, sendo o plano do cliente basic
cliente.ver_filme("Harry Potter", "premium")
#
# #no botão de upgrade
# #Alteração de plano do cliente para premium;
cliente.mudar_plano("confort")
print(cliente.plano)
#
cliente.ver_filme("Harry Potter", "premium")