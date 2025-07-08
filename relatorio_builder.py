from abc import ABC, abstractmethod

class RelatorioBuilder(ABC):
    def __init__(self):
        self.relatorio = Relatorio()  
    
    @abstractmethod
    def build_titulo(self):
        pass

    @abstractmethod
    def build_sumario_executivo(self):
        pass

    @abstractmethod
    def build_tabelas_dados(self):
        pass

    @abstractmethod
    def build_graficos(self):
        pass

    @abstractmethod
    def build_recomendacoes(self):
        pass

    def get_relatorio(self):
        return self.relatorio

class Relatorio:
    def __init__(self):
        self.secoes = []

    def adicionar_secao(self, secao):
        self.secoes.append(secao)

    def gerar_relatorio(self):
        return '\n\n'.join(self.secoes) 

class RelatorioExecutivoBuilder(RelatorioBuilder):
    def build_titulo(self):
        self.relatorio.adicionar_secao("Relatório Executivo")
    
    def build_sumario_executivo(self):
        self.relatorio.adicionar_secao("Sumário Executivo: Visão geral dos resultados e recomendações.")
    
    def build_tabelas_dados(self):
        pass

    def build_graficos(self):
        pass

    def build_recomendacoes(self):
        self.relatorio.adicionar_secao("Recomendações: Ações sugeridas com base nos resultados.")
    
class RelatorioAnalistaBuilder(RelatorioBuilder):
    def build_titulo(self):
        self.relatorio.adicionar_secao("Relatório Analítico")
    
    def build_sumario_executivo(self):
        pass
    
    def build_tabelas_dados(self):
        self.relatorio.adicionar_secao("Tabelas de Dados: Informações detalhadas em formato tabular.")
    
    def build_graficos(self):
        self.relatorio.adicionar_secao("Gráficos: Visualizações dos dados para melhor compreensão.")
    
    def build_recomendacoes(self):
        self.relatorio.adicionar_secao("Recomendações: Sugestões baseadas na análise dos dados.")

