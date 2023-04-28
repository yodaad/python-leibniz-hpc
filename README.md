# Instrucciones

1. Instale MPI en Rocks con el comando:

`sudo yum install openmpi openmpi-devel`

2. Corra el código de Python con el comando:
   Un procesador: `mpirun -n 1 python nombre_del_archivo.py`
   Dos procesadores: `mpirun -n 2 python nombre_del_archivo.py`
   Tres procesadores: `mpirun -n 3 python nombre_del_archivo.py`
