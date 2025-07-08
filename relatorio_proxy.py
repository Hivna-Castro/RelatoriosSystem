class RelatorioSender:
    def send(self, relatorio, user):
        print(f"[Enviando Relatório para o usuário {user.nome}...]")
        print(relatorio.gerar_relatorio())

class AuthProxy:
    def __init__(self, user):
        self.user = user
        self.real_sender = RelatorioSender()

    def send(self, relatorio):
        if self.user.autenticado:
            self.real_sender.send(relatorio, self.user)
        else:
            print(f"[Acesso negado: usuário {self.user.nome} não autenticado. Relatório não enviado.]")
