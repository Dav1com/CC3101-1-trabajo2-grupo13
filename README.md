# CC3101-1-trabajo2-grupo13

Ya que no nunca supimos si se podía hacer en C++, lo tradujimos a Python, ambos archivos están hechos para ejecutar la implementación de la parte (d)

Para ejecutar la versión en C++ se puede usar:
```bash
clang++ -std=c++17 -pthread -O3 main.cpp -o main
./main
```
o, alternativamente:
```bash
g++ -std=c++17 -pthread -O2 main.cpp -o main
./main
```

en ambos casos `clang++` y `g++` deben estar en una versión que soporte C++17
