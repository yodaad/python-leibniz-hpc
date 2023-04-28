from mpi4py import MPI
import time

# Inicialización de objetos MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# Cálculo de PI utilizando el método de Leibniz
num_iterations = 9e9
pi_sum = sum((-1) ** i / (2 * i + 1) for i in range(rank, int(num_iterations), size))

# Reducción de la sumatoria utilizando MPI
pi_approx = comm.reduce(pi_sum, op=MPI.SUM, root=0)

# Impresión de resultados 
if rank == 0:
    pi_approx *= 4.0
    print(f"Aproximación de PI = {pi_approx:.15f}")
    print(f"Tiempo de ejecución = {time.time() - MPI.Wtime():.6f} segundos")

# Finalización de ejecución de procesos MPI
MPI.Finalize()
