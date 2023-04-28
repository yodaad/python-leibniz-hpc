from mpi4py import MPI
import time

# Inicialización de objetos MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definición de variables necesarias
num_iterations = 9e9
iterations_per_process = int(num_iterations / size)
start_iteration = rank * iterations_per_process
end_iteration = start_iteration + iterations_per_process

# Cálculo de PI utilizando el método de Leibniz
pi_sum = 0.0
for i in range(start_iteration, end_iteration):
    sign = 1.0 if i % 2 == 0 else -1.0
    pi_sum += sign / (2.0 * i + 1.0)

# Reducción de la sumatoria utilizando MPI
pi_approx = comm.reduce(pi_sum, op=MPI.SUM, root=0)

# Impresión de resultados por pantalla
if rank == 0:
    pi_approx *= 4.0
    print(f"PI approximation = {pi_approx:.15f}")
    print(f"Execution time = {time.time() - MPI.Wtime():.6f} seconds")

# Finalización de ejecución de procesos MPI
MPI.Finalize()
