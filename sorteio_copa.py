import random
import time

# Lista com as 8 equipes classificadas
times = [
    "Atlético Mineiro",
    "Cruzeiro",
    "Grêmio",
    "Internacional",
    "Palmeiras",
    "Santos",
    "Vasco",
    "Vitória",
]

# Aqui embaralha os times na lista com a função 'shuffle'
random.shuffle(times)

print("\n=== SORTEIO DAS QUARTAS DE FINAL - COPA DO BRASIL ===")

# Percorre a lista pulando de 2 em 2(0, 2, 4, 6)
confronto_num = 1
for i in range(0, len(times), 2):
    time.sleep(1) # A função sleep() de Time, faz com que o sorteio ocorra com pausas de 1 segundo
    time_mandante_ida = times[i]
    time_visitante_ida = times[i + 1]

    print(f"\nConfronto {confronto_num}: ")
    print(f" Jogo de Ida: {time_mandante_ida} x {time_visitante_ida}")
    print(f" Jogo de Volta: {time_visitante_ida} x {time_mandante_ida}\n")

    confronto_num += 1
