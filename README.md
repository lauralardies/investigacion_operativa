# investigacion_operativa

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/investigacion_operativa)
https://github.com/lauralardies/investigacion_operativa

> Los diferentes **modelos** que vemos en el repositorio son distintas interpretaciones que hemos extraído del texto. Por otro lado, las diferentes **variantes** son las que nos proponen en el enunciado.

## Enunciado 
Asier es un estudiante emprendedor de tercer año en la UAX. Tiene la teoría de que solo estudiar y nada de diversión acabarán por convertirlo en un trol. Para evitarlo quiere distribuir su tiempo disponible para ambas tareas, a lo sumo 10 horas al día en total, entre el estudio y la diversión. Calcula que divertirse es dos veces más interesante que estudiar, pero cree que para poder cumplir con las tareas diarias de la universidad la diferencia entre las horas que dedica a divertirse y las que dedica a estudiar debe ser a lo sumo de 1 hora. Además, debe tener en cuenta que sus padres le permiten dedicar como máximo 4 horas a actividades lúdicas. ¿Cómo debe distribuir Asier su tiempo para conseguir que sea lo más interesante posible?
- Variante 1: Supongamos ahora que Asier valora exactamente igual las horas dedicadas a estudiar que las dedicadas a divertirse. ¿Cuál sería ahora la solución óptima?
- Variante 2: Si ahora eliminamos la restricción de que el número máximo de horas disponibles es de 10 horas ¿cuál sería la solución óptima del problema?
- Variante 3: ¿Cuál sería la solución óptima del problema si el objetivo de Asier fuera convertirse en un trol?
- Variante 4: Olvidémonos de ser un trol, no era una buena idea ¿Cuál sería la solución óptima del problema si el objetivo de Asier fuera divertirse lo máximo posible?

## Modelos

### Modelo 1: 
En este modelo tomamos como función objetivo Max(Z)=x1+2x2.

Y restricciones: x2<=10-x1; x2<=x1+1; x2<=4. 

En este modelo hemos tomado que la frase 'la diferencia entre las horas que dedica a divertirse y las que dedica a estudiar debe ser a lo sumo de 1 hora' se representa matemáticamente como x2-x1<=1.

### Modelo 2: 
En este modelo tomamos como función objetivo Max(Z)=x1+2x2.

Y restricciones: x2<=10-x1; x2<=x1-1; x2<=4. 

En este modelo hemos tomado que la frase 'la diferencia entre las horas que dedica a divertirse y las que dedica a estudiar debe ser a lo sumo de 1 hora' se representa matemáticamente como x1-x2<=1.

### Modelo 3: 
En este modelo tomamos como función objetivo Max(Z)=x1+2x2.

Y restricciones: x2<=10-x1; x2<=x1+1; x2<=x1-1; x2<=4. 

En este modelo hemos tomado que la frase 'la diferencia entre las horas que dedica a divertirse y las que dedica a estudiar debe ser a lo sumo de 1 hora' se representa matemáticamente como |x1-x2|<=1.

## Variantes
En las variantes hemos trabajado sobre el modelo 1, pues lo hemos considerado el más apropiado de los tres que hemos visto.

### Variante 1:
En este modelo tomamos como función objetivo Max(Z)=x1+x2. Se valora de igual manera la diversión y el estudio.

Las restricciones son las mismas: x2<=10-x1; x2<=x1+1; x2<=4. 

### Variante 2:
En este modelo tomamos como función objetivo Max(Z)=x1+2x2. Sólo eliminamos una de las restricciones.

Y restricciones: x2<=x1+1; x2<=4. 

### Variante 3:
En este modelo tomamos como función objetivo Max(Z)=y. Se trata de maximizar la diversión, que posteriormente limitaremos a 0 en las restricciones, ya que Asier se quiere convertir en un troll.

Restricciones: x2<=10-x1; x2<=x1+1; x2<=4; x2=0. 

### Variante 4:
En este modelo tomamos como función objetivo Max(Z)=y. Maximizamos la diversión.

Restricciones: x2<=10-x1; x2<=x1+1; x2<=4; x2=0. 
