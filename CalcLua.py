import ephem
from datetime import datetime

def calcular_fase_lua(data):
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print("Formato inválido! Use AAAA-MM-DD.")
        return

    lua = ephem.Moon(data)  
    fase = lua.phase  # Obtém a idade da Lua no ciclo (0 a 29,53 dias)

    # Classificação da fase da Lua
    if fase < 1.5:
        nome_fase = "Lua Nova 🌑"
    elif fase < 7.4:
        nome_fase = "Lua Crescente 🌒"
    elif fase < 15.8:
        nome_fase = "Lua Cheia 🌕"
    else:
        nome_fase = "Lua Minguante 🌘"

    print(f"\nData: {data.strftime('%Y-%m-%d')}")
    print(f"Fase da Lua: {fase:.1f} dias")
    print(f"Status: {nome_fase}")

data_usuario = input("Informe a data (AAAA-MM-DD) ou pressione Enter para usar a data atual: ")

# Usa a data informada ou a data de hoje
if not data_usuario:
    data_usuario = datetime.today().strftime("%Y-%m-%d")

calcular_fase_lua(data_usuario)
