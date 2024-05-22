import numpy as np
import art
from art import text2art

# Cria arte ASCII do símbolo de pi
pi_art = text2art("PI", font="block")

# Exibe no display
print(pi_art)

pi = np.pi

print(f"Valor aproximado de π = {pi:.2f}")
# Com descrição
print(f"Descrição:\nO número pi(π) é infinito. Por esse motivo,\nele é representado com reticências no fim.\nNo entanto, muitas vezes utiliza-se apenas\na aproximação para 3,1416, ou 3,14")