# Método numérico: Runge-Kutta de orden 4 (RK4)

Este método numérico sirve para encontrar soluciones numéricas a ecuaciones diferenciales en sistemas dinámicos.
El método RK4 se basa en estomar la solución a un punto temporal $y_{n+1}$ con base en la solución en el punto temporal $y_{n}$. Tenemos:

$$\begin{aligned}
k_{1} &:= hf\left(t_{n},y_{n}\right) \\
k_{2} &:= hf\left(t_{n}+\frac{h}{2},y_{n}\frac{k_{1}}{2}\right) \\
k_{3} &:= hf\left(t_{n}+\frac{h}{2},y_{n}+\frac{k_{2}}{2}\right) \\
k_{4} &:= hf\left(t_{n}+h,y_{n}+k_{3}\right) \\
y_{n+1} &= y_{n} + \frac{1}{6}\left(k_{1}+2k_{2}+2k_{3}+k_{4}\right)
\end{aligned}$$

## Sistemas dinámicos
Los sistemas dinámicos son modelos de suma importancia en las ciencias. En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico $y$ mediante la ecuación dinámica
\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}

En esta notación, $y$ corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, $t$ corresponde a la variable temporal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como **problema de condición inicial**.
