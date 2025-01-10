import sys
sys.stdout.reconfigure(encoding='utf-8')


print("******************Calculadora de Energias******************")


#Energia potencial gravitacional
#Epg = mgh

#energia = "cinética"

print("1. Energia Potêncial Gravitacional\n2. Energia Cinética\n3. Energia Elásica")


energia = input("Qual Energia você gostaria de calcular? ")
print(f"A opção escolhida foi {energia}!")


if energia == "1" or energia.lower() == "gravitacional":
        print("A Epg é calculada utilizando a massa, gravidade e a altura no Sistema Internacional de Medidas.")
        
        massa = float(input(" Informe a massa do objeto no SI: (kg):"))
        print(f"A massa informada foi {massa} kg.")

        gravidade = float(input(" Informe a gravidade do objeto no SI: (m/s²)"))
        print(f"A gravidade informada foi {gravidade} (m/s²).")

        altura = float(input(" Informe a altura do objeto no SI: (m)"))
        print(f"A altura informada foi {altura} m.")

        print("Calculando...")

        Epg = massa * gravidade * altura

        print(f"A Energia Potencial Gravitacional é {Epg} Joules.")

elif energia == "2" or energia.lower() == "Cinética":
        print("A Ec é calculada utilizando a massa, velocidade ao quadrado dividindo por 2")

        massa = float(input(" Informe a massa do objeto no SI: (kg):"))
        print(f"A massa informada foi {massa} kg.")

        velocidade = float(input(" Informe a velocidade do objeto no SI: (m/s):"))
        print(f"A velocidade informada foi {velocidade} kg.")

        Ec = 0.5 * massa * velocidade ** 2

        print(f"A Energia Potencial Gravitacional é {Ec} Joules.")

elif energia == "3" or energia.lower() == "Elásica":
        print("A Ee é calculada utilizando a constante elástica e a deformação da mola.")
    
        mola = float(input("Informe a constante elástica da mola (N/m): "))
        print(f"A constante elástica informada foi {mola} N/m.")
    
        deformacao = float(input("Informe a deformação da mola (em metros): "))
        print(f"A deformação informada foi {deformacao} metros.")
    
    # Cálculo da energia elástica
        Ee = 0.5 * mola * deformacao ** 2

        print(f"A Energia Elástica é {Ee} Joules.")

else:
        print("Opção inválida! Escolha entre as oferecidas.")

