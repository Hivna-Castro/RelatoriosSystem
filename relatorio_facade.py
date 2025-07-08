from relatorio_builder import RelatorioBuilder

class RelatorioFacade:
    def __init__(self, builder: RelatorioBuilder):
        self.builder = builder

    def gerar_relatorio(self):
        self.builder.build_titulo()
        self.builder.build_sumario_executivo()
        self.builder.build_tabelas_dados()
        self.builder.build_graficos()
        self.builder.build_recomendacoes()
        return self.builder.get_relatorio()

    def salvar_relatorio(self, relatorio):
        print("[Salvando relatório...]")
        print(relatorio.gerar_relatorio())
