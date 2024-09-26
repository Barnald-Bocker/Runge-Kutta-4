import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """Lineal operator for -i[O,y(t)].

    In this case, "O" is another linear operator, i is the complex constant, and "y(t)" is a time-dependent function.
    It requires NumPy to be imported as "np".

    Examples:
        oOper is the linear operator.
        yInit is the initial state.

        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oOper, yInit)
        [[-0.92093156+0.j          0.        +0.38972435j]
         [ 0.        -0.38972435j  0.92093156-0.j        ]]

    Args:
        oper (Numpy array): First argument (linear operator).
        state (Numpy array): Second argument (initial state).

    Returns:
        (Numpy array): Returns the result of applying the operator -i[A.B] = -i(AB - BA), known as the commutator.
    """
    return (np.dot(oper, state) - np.dot(state, oper)) * (-1.0j)

def rk4(func, oper, state, h):
    """ Runge-Kutta 4, for a non time dependent function.

    This is the main purpose of all the code, it develops the numerical with the following arguments:

    Args:
        func (Function): This would be the function that is going to be used to input and develop the solution. For this particular example it would be dyn_generator
        oper (Numpy array): Second argument (linear operator)
        state (Numpy array): Third argument. This is a dynamic array that will be change during the for loop for the purpose of changing the initial state, therefore changing the temporal point.
        h (float): Temporal step necessary for the numerical method

    Returns:
        (Numpy array): Returns the state of the system in that particular time.

    Examples:
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> h = 0.01001001001001001
        >>> print(rk4(dyn_generator,oOper, yInit, h))
        [[0.68560521+0.j         0.        +0.46427439j]
         [0.        -0.46427439j 0.31439479+0.j        ]]

    """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state+(k1/2))
    k3 = h*func(oper,state+(k2/2))
    k4 = h*func(oper,state+k3)
    return state + (1/6)*(k1+(2*k2)+(2*k3)+k4)
