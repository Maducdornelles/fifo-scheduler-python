# FIFO - First Come, First Served
# Simulação simples de escalonamento de processos

# Lista de processos com tempo de chegada e duração
processos = [
    {"id": "P1", "chegada": 0, "duracao": 4},
    {"id": "P2", "chegada": 1, "duracao": 5},
    {"id": "P3", "chegada": 2, "duracao": 1}
]

# Ordenar os processos por tempo de chegada (característica do FIFO)
processos.sort(key=lambda p: p["chegada"])

tempo_atual = 0
tempo_espera_total = 0
tempo_turnaround_total = 0

print("Execução FIFO:")
for p in processos:
    if tempo_atual < p["chegada"]:
        tempo_atual = p["chegada"]  # Se o processo ainda não chegou, esperar

    p["inicio"] = tempo_atual
    p["fim"] = tempo_atual + p["duracao"]
    tempo_atual += p["duracao"]

    p["tempo_espera"] = p["inicio"] - p["chegada"]
    p["turnaround"] = p["fim"] - p["chegada"]

    tempo_espera_total += p["tempo_espera"]
    tempo_turnaround_total += p["turnaround"]

    print(f"{p['id']} - Início: {p['inicio']} | Fim: {p['fim']} | Espera: {p['tempo_espera']} | Turnaround: {p['turnaround']}")

# Cálculo de médias
n = len(processos)
media_espera = tempo_espera_total / n
media_turnaround = tempo_turnaround_total / n

print(f"\nTempo médio de espera: {media_espera:.2f}")
print(f"Tempo médio de turnaround: {media_turnaround:.2f}")

