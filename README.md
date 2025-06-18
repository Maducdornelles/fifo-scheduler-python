# Simulação do Algoritmo de Escalonamento FIFO (First In, First Out)
Trabalho acadêmico para a disciplina de Sistemas Operacionais, ministrada pelo professor Fernando Posser Pinheiro, na Atitus Educação.

## Integrantes da equipe: 
Gabriela Lenz, Gustavo Rampanelli, Isadora Aguirre, Maria Eduarda Carvalho e Pablo De Oliveira.

## Descrição do Projeto
Este projeto simula o algoritmo de escalonamento de processos FIFO (First In, First Out), também conhecido como FCFS (First-Come, First-Served), um algoritmo simples onde o primeiro processo que chega é o primeiro a ser executado. O objetivo é calcular o tempo de execução de cada processo, considerando o tempo de espera e o tempo de turnaround, e exibir as métricas relevantes.

## ESPAÇO PARA O VÍDEO YT/DRIVE -------------

## Contexto do Código

O código implementa o algoritmo de escalonamento **FIFO (First-In, First-Out)** utilizando a linguagem Python.  
O FIFO é um dos algoritmos de escalonamento mais simples e diretos, onde os processos são executados na ordem de chegada ao sistema, sem qualquer tipo de preempção.

No código, a lista de processos contém três entradas, cada uma com o **tempo de chegada** e a **duração de execução**:

- P1: Chegada = 0, Duração = 4
- P2: Chegada = 1, Duração = 5
- P3: Chegada = 2, Duração = 1

Antes da execução, os processos são ordenados por tempo de chegada, que é uma característica essencial do FIFO.

---

## Análise dos Resultados Obtidos

Durante a execução, o sistema calcula para cada processo:

- **Tempo de Início:** Quando o processo começa a executar.
- **Tempo de Fim:** Quando o processo termina sua execução.
- **Tempo de Espera:** Quanto tempo o processo aguardou na fila antes de iniciar.
- **Tempo de Turnaround:** Tempo total desde a chegada até a finalização do processo.

### Resultados individuais dos processos:

| Processo | Início | Fim | Tempo de Espera | Turnaround |
|--------- | ------ | --- | --------------- | ---------- |
| P1 | 0 | 4 | 0 | 4 |
| P2 | 4 | 9 | 3 | 8 |
| P3 | 9 | 10 | 7 | 8 |

### Cálculos Finais:

- **Tempo médio de espera:** 3.33 unidades de tempo
- **Tempo médio de turnaround:** 6.67 unidades de tempo

---

## Conclusão sobre o FIFO

O algoritmo FIFO garante uma execução simples e fácil de implementar, priorizando a ordem de chegada dos processos.  
No entanto, pode gerar problemas de **injustiça para processos menores**, como observado no exemplo: o processo P3 teve que esperar bastante tempo, mesmo tendo uma duração muito curta.

### Pontos positivos do FIFO:
- Fácil implementação
- Previsível (ordem de chegada é respeitada)
- Baixa sobrecarga no sistema

### Pontos negativos:
- Pode causar **alto tempo de espera médio**, principalmente quando há **processos curtos atrás de processos longos** (fenômeno conhecido como **convoy effect**).
---

## Como executar o projeto

1. Clone e acesse o repositório:
    ```bash
    git clone https://github.com/Maducdornelles/fifo-scheduler-python.git 
    cd fifo-scheduler-python
    ```
2. Rode o arquivo .py:
    ```bash
    python fifo.py
    ```

## Referências
Aqui estão alguns repositórios no GitHub com implementações e exemplos do algoritmo de escalonamento **FIFO (First-In, First-Out)**:

- [**anubha-paliwal / Operating-System-Scheduling-Algorithms** - FCFS.py](https://github.com/anubha-paliwal/Operating-System-Scheduling-Algorithms/blob/master/FCFS.py)  
Repositório com implementações de vários algoritmos de escalonamento. O arquivo `FCFS.py` traz uma implementação simples e direta do FIFO.

- [**TheAlgorithms / Python** - fcfs_scheduling.py](https://github.com/TheAlgorithms/Python/blob/master/operating_system/fcfs_scheduling.py)  
Repositório com várias implementações de algoritmos em Python. A pasta `operating_system` contém o arquivo `fcfs_scheduling.py`, com código de escalonamento FIFO.

- [**rohithasrk / CPU-Scheduling-Algorithms** - fcfs.py](https://github.com/rohithasrk/CPU-Scheduling-Algorithms/blob/master/fcfs.py)  
Repositório dedicado apenas a algoritmos de escalonamento de CPU, com código bem separado para o FIFO.

- [**dhanrajdc7 / Operating-System-CPU-Scheduling-Algo** - FCFS.py](https://github.com/dhanrajdc7/Operating-System-CPU-Scheduling-Algo/blob/master/FCFS.py)  
Outro repositório focado em algoritmos de escalonamento, com implementação bem comentada do FCFS.

- [**shivanshugarg12800 / CPU_Scheduling_Algorithms** - fcfs.py](https://github.com/shivanshugarg12800/CPU_Scheduling_Algorithms/blob/main/fcfs.py)  
Implementação simples e didática de FIFO (FCFS), adequada para estudos iniciais.

