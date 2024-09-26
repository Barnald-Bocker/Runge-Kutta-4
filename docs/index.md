# Problema a resolver:

Se busca estudiar la evolución temporal de un estado $\mathbf{y}(t)$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genra la dinámica del problema es 
$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$
donde $\mathbf{O}$ es otro operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es un operación de conmutación. Note que **la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal**.

El operador lineal de escogencia para este ejemplo es:

$$ 
Oper = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}  
$$

El estado inicial para este ejemplo es:

$$
yInit = \begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix}
$$

Asimismo, se tiene que definir un espacio para los tiempos y calcular su respectivo intervalo:

\begin{aligned}
tInit = 0 \\
tFinal = 10 
\end{aligned}

Para este caso se usaría la función np.linspace para generar 1000 datos o divisiones, así resulta el intervalo:

\begin{aligned}
h = times[1] - times[0] \\
h \approx 0.01001001001001001
\end{aligned}
