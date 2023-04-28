# Instrucciones

1. Instale MPI en Rocks con el comando:

`sudo yum install openmpi openmpi-devel`

2. Corra el código de Python con los comandos (-n 1 es para un procesador, -n 2 para dos, y -n 3 para tres,):

```mpirun -n 1 python nombre_del_archivo.py
mpirun -n 2 python nombre_del_archivo.py
mpirun -n 3 python nombre_del_archivo.py
```
