from dataclasses import dataclass
import numpy as np

@dataclass
class ParametrosCSTR:
  vazao: float = 100.0 
  volume: float = 50.0
  constante: float = 0.5

def modelo_cstr(CAin, params):
  F = params.vazao
  V = params.volume
  k = params.constante
  CA = F/(F+V*k)*CAin
  return CA

def simula_cstr(CA0 = 1.0, num_estagios = 3, params):
  CAin = CA0
  CA = np.zeros(num_estagios)
  X = np.zeros(num_estagios)
  for j in range(num_estagios):
    CA[j] = modelo_cstr(CAin, params[j])
    X[j] = (CA0-CA[j])/CA0
    CAin = CA[j]
  return CA, X
    
