from dataclasses import dataclass

@dataclass
class CSTR_param():
  F: float = 50.0 # L/min
  V: float = 100.0 # L
  k: float = 0.5 # 1/min

def CSTR_model(param, Ca_entrada):
  Ca_saida = (param.F*Ca_entrada)/(param.F + param.V * param.k)
  return Ca_saida

def CSTR_series(lista_param, Ca_entrada):
  conc = [Ca_entrada]
  conv = []
  for param in lista_param:
    Ca_saida = CSTR_model(param, Ca_entrada)
    conv_local = 1 - Ca_saida/conc[0]
    conc.append(Ca_saida)
    conv.append(conv_local)
    Ca_entrada = Ca_saida
  return conc, conv
