import random
import time

from select_bfprt import select_bfprt

def generate_triple():
    """
    Gera uma instância de teste:
      - y: tamanho do vetor 
      - x: vetor com y elementos aleatórios
      - z: inteiro aleatório entre 1 e y (1-indexado)
    Retorna a dupla (x, z).
    """
    y = 100000
    x = [random.randint(1, 200000) for _ in range(y)]
    z = random.randint(1, y)
    return x, z

def run_instance(x, z, r=3):
    resultado = select_bfprt(x, z - 1, r)
    return resultado

def performance_test(num_instances, r=3):
    """
    Executa num_instances testes:
      - Para cada instância, gera o vetor aleatório e o valor z.
      - Mede o tempo de execução do algoritmo para esta instância.
    Retorna o tempo total e o tempo médio de execução (por instância).
    """
    total_time = 0
    for i in range(num_instances):
        x, z = generate_triple()
        start = time.perf_counter()
        _ = run_instance(x, z, r)
        end = time.perf_counter()
        total_time += (end - start)
        
        # Opcional: imprimir progresso a cada 1000 instâncias
        if (i + 1) % 1000 == 0:
            print(f"{i + 1} instâncias concluídas.")
    
    average_time = total_time / num_instances
    return total_time, average_time

if __name__ == "__main__":
    num_instances = 10000  # 1 milhão de instâncias 
    r = 3  # Tamanho do grupo para a mediana de medianas 
    
    print("Iniciando os testes de performance...")
    total_time, avg_time = performance_test(num_instances, r)
    print(f"\nTeste para temanho de grupo r = {r}")
    print(f"\nTempo total para {num_instances} instâncias: {total_time:.5f} segundos")
    print(f"Tempo médio por instância: {avg_time:.8f} segundos")