# Primeros pasos en Solidity con Python

## Requisitos

Debes instalar el <b>prequirements.txt"</b> para qye no tengas problemas de librerias a la hora de ejecutar el proyecto
```
pip install -r ".\requirements.txt"
```

## Ejecucion del proyecto


## Posibles errores
Si has intalado <b>pip install web3</b>, tendras un error similar 
```
  File "D:\Curso-Emer\Desarrollo_Solidity\Cursos-Solidity\Test-Prueba\venv\Lib\site-packages\parsimonious\expressions.py", line 9, in <module>
    from inspect import getargspec
ImportError: cannot import name 'getargspec' from 'inspect' (C:\Users\emers\AppData\Local\Programs\Python\Python311\Lib\inspect.py)
```
> Este error es generado por la desactualoizacion de la libreria <b>web3</b> en pyrhon, debemos instalarala desde el mismo repositorio

### Pasos solucioar el problema
Desistalacion de <b>pip web3</b> 
```
pip uninstall web3
```
Instalacion de las nueva version de <b>pip web3</b> 
```
pip install git+https://github.com/ethereum/web3.py.git
```
