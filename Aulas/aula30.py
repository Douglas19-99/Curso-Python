"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# Posso melhorar esse codigo colocando mais variaveis.
velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 90
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade do carro passo do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro multado em rada 1')


