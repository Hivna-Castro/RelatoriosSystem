from relatorio_builder import RelatorioExecutivoBuilder, RelatorioAnalistaBuilder
from relatorio_facade import RelatorioFacade
from relatorio_proxy import AuthProxy
from user import User


if __name__ == "__main__":
    print("==== RELATÓRIO EXECUTIVO ====")
    cria_relatorio= RelatorioExecutivoBuilder()
    facade_exec = RelatorioFacade(cria_relatorio)
    relatorio = facade_exec.gerar_relatorio()
    facade_exec.salvar_relatorio(relatorio)

    user = User(nome="Ana Maria Gerente", autenticado=True)
    proxy = AuthProxy(user)
    proxy.send(relatorio)

    print("\n==== RELATÓRIO ANALISTA ====")
    cria_relatorio_analista = RelatorioAnalistaBuilder()
    facade_analista = RelatorioFacade(cria_relatorio_analista)
    relatorio_analista = facade_analista.gerar_relatorio()
    facade_analista.salvar_relatorio(relatorio_analista)

    user_analista = User(nome="Zé Analista", autenticado=False)
    proxy_analista = AuthProxy(user_analista)
    proxy_analista.send(relatorio_analista)
