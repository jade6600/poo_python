# POO en Python 

- El paradigma de programacion orientada a objetos esta basado en una abstraccion del mundo real, que nos va a permitir a desarrolar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## clase

- Una clase esun tipo de dato cuyas variables se llaman objetos o instancias.
- La clase es la definicion del concepto del mundo real y los objetos o instancias son el propio  objeto del mundo real.
- Las clases estan compuestas por dos elementos: atributos y metodos.

### atributos
- Son informacion que alamacena la clase.

### mètodos
- Operaciones que pueden realizar las clases.

## Definicion de una clase en Python
```python
class Nombreclase:

   def__init__(self, variable1, variable2):
       self.Atributo1 = valor 1
       self.Atributo2 = valor 2

   def nombreMetodo(self):
      bloque codigo
```


### componentes

```class```: palabra reservada en python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en python que se utiliza para definir tanto el constructor de la clase(metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene.

```__init__```: palabra reservada en python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto deuna clase.

```(self,variable x)```parametro del constructor de la clase. el parametro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.

```(self.AtributoX)```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```nombre del metodo de la clase.

```(self)```parametros del metodo. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que en las funciones.

```bloqueCodigo```instrucciones que ejecutara el metodo.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
     - Puedes definir tantos atributos como necesites.
     - Puedes defnir tantos metodos como necesites.
     - Puedes definir tantos parametros en el consructor y en los metodos como necesites.
     
## Composicion 
- Consiste en la creaion de nuevas clases a partir de otras clases ya existentes, que actuan como elementos compositores de la nueva.
- Las clases existntes seran atributos de la nueva clase.
- En POO la composicion significa que entre las dos clases que existe una relacion de tipo "tiene 1"
- Ejempo:
     una coordenada en dos dimensiones esta compuesta por dos valores, el valor del eje de las x y el valor en el eje de las  y , esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que sonlos cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada. 
     
