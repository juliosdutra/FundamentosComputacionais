from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CSTR_param:
    F: float = 50.0   # Vazão de alimentação (L/min)
    V: float = 100.0  # Volume do reator (L)
    k: float = 0.5    # Constante cinética de 1ª ordem (1/min)

def modelo_CSTR(param: CSTR_param, CA_entrada: float) -> float:
    """
    Modelo de um reator CSTR: calcula concentração de saída.

    Parâmetros:
        param: objeto com F, V, k do reator
        CA_entrada: concentração na entrada (mol/L)

    Retorna:
        CA_saida: concentração na saída (mol/L)
    """
    return (param.F / (param.F + param.V * param.k)) * CA_entrada

def serie_CSTR(param_list: List[CSTR_param], CA_entrada: float) -> Tuple[List[float], List[float]]:
    """
    Simula uma série de reatores CSTR com parâmetros possivelmente diferentes.

    Parâmetros:
        param_list: lista de objetos CSTR_param, um para cada reator
        CA_entrada: concentração inicial de A (mol/L)

    Retorna:
        Conc: lista com as concentrações (entrada e saídas)
        Conv: lista com conversões acumuladas após cada reator
    """
    Conc = [CA_entrada]
    Conv = []

    CA0 = CA_entrada
    for param in param_list:
        CA_saida = modelo_CSTR(param, CA_entrada)
        conversao = 1 - CA_saida / CA0
        Conc.append(CA_saida)
        Conv.append(conversao)
        CA_entrada = CA_saida

    return Conc, Conv

def ajuda():
    """
    Exemplo de uso do módulo de simulação de CSTRs.

    >>> from cstr_series import CSTR_param, modelo_CSTR, serie_CSTR

    # Criar uma lista de 3 reatores com parâmetros diferentes
    >>> reatores = [
    ...     CSTR_param(F=50, V=100, k=0.5),
    ...     CSTR_param(F=50, V=100, k=0.8),
    ...     CSTR_param(F=50, V=100, k=1.2)
    ... ]

    # Concentração de entrada no primeiro reator
    >>> CA0 = 1.0

    # Simular série de reatores
    >>> concentracoes, conversoes = serie_CSTR(reatores, CA0)

    # Exibir resultados
    >>> for i, (CA, X) in enumerate(zip(concentracoes[1:], conversoes), start=1):
    ...     print(f"Reator {i}: C_A = {CA:.4f} mol/L | Conversão acumulada = {X:.2%}")
    """
    print(ajuda.__doc__)
