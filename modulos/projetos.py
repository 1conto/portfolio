from typing import List, Iterable, Optional


class Projetos:
    def __init__(self, nome: str, categoria: str, link_repositorio: str, main_stack:str = None, destaque:bool = False):
        self._nome = nome
        self._link = link_repositorio
        self.categoria = categoria
        self.destaque = destaque
        self.main_stack = main_stack

    #def show_project(self, funcao_show: function):
    #    funcao_show()

class ProjetosManager:
    """Gerencia a lista de projetos exibidos no portfólio."""

    def __init__(self, projetos: Optional[Iterable[Projetos]] = None):
        self._projetos: List[Projetos] = list(projetos) if projetos else []

    def adicionar(self, projeto: Projetos) -> None:
        self._projetos.append(projeto)

    def listar(self) -> List[Projetos]:
        return list(self._projetos)

    def filtrar_por_categoria(self, categoria: str) -> List[Projetos]:
        return [p for p in self._projetos if p.categoria.lower() == categoria.lower()]

    @property
    def get_projetos(self):
        return self._projetos

    @property
    def get_destaques(self):
        return [projeto for projeto in self.get_projetos if projeto.destaque]