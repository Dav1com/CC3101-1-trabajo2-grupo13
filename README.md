# CC3101-1-trabajo2-grupo13

Ya que nunca supimos si se podía hacer en C++, lo tradujimos a Python, ambos archivos están hechos para ejecutar la implementación de la parte (d)

Para ejecutar la versión en C++ se puede usar:
```console
$ clang++ -std=c++17 -pthread -O3 main.cpp -o main
$ ./main
```
o, alternativamente:
```console
$ g++ -std=c++17 -pthread -O2 main.cpp -o main
$ ./main
```

en ambos casos `clang++` y `g++` deben estar en una versión que soporte C++17, tener en cuenta que el código fue probado en un ambiente Linux de 64 bits.
