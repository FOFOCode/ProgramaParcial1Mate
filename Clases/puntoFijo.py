import sympy as sp

# Pedir al usuario que ingrese la función, el valor inicial, la tolerancia y el número máximo de iteraciones
print("Ingrese la función ya despejada (por ejemplo, cos(x)): ")
fx = input()

print("Ingrese la aproximación inicial: ")
x0 = float(input())  # Convertir a float

print("Ingrese la tolerancia: ")
tol = float(input())  # Convertir a float

print("Ingrese el número máximo de iteraciones: ")
nmax = int(input())  # Convertir a entero

# Función para evaluar la expresión en un valor específico
def eval_func(expr, val):
    x = sp.symbols('x')
    return expr.subs(x, val)

# Método de punto fijo
def punto_fijo(expr, x0, tol, nmax):
    iteracion = 0
    while iteracion < nmax:
        x1 = eval_func(expr, x0)
        print(f"Iteración {iteracion+1}: x = {x1}")
        if abs(x1 - x0) < tol:
            return x1, iteracion + 1
        x0 = x1
        iteracion += 1
    print("Se alcanzó el número máximo de iteraciones.")
    return x1, iteracion

# Convertir la entrada de texto en una expresión simbólica
expr = sp.sympify(fx)

# Ejecutar el método de punto fijo
raiz, iteraciones = punto_fijo(expr, x0, tol, nmax)
print(f"\nLa raíz aproximada es: {raiz:.8f} después de {iteraciones:.8f} iteraciones.")
