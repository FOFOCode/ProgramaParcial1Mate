import sympy as sp

print("Ingrese la funcion: ")
fx = input()

print("Ingrese el valor inicial: ")
a = int(input())

print("Ingrese el valor final: ")
b = int(input())

print("Ingrese la tolerancia: ")
e = float(input())

print("Ingrese el Nmax: ")
nmax = int(input())

def eval_func(expr, val):
    x = sp.symbols('x')
    return expr.subs(x, val)

def falsaPosicion(fx, a, b, e, nmax):
    expr = sp.sympify(fx)
    fa = eval_func(expr, a)
    fb = eval_func(expr, b)
    
    print(f"f(a) = {fa:.8f}, f(b) = {fb:.8f}")
    print()
    
    iteraciones = 0
    xrAnterior = None
    last_valid_iteration = None

    while iteraciones < nmax:
        xrActual = b - ((fb * (b - a)) / (fb - fa))
        fxr = eval_func(expr, xrActual)
        
        if xrAnterior is None:
            tolerancia_calculada = 100  # Inicialmente alta porque no hay valor anterior
        else:
            tolerancia_calculada = abs((xrActual - xrAnterior) / xrActual) * 100
        
        print(f"Iteración {iteraciones + 1}:")
        print(f"  a = {a:.8f}, b = {b:.8f}")
        print(f"  Xr = {xrActual:.8f}, f(Xr) = {fxr:.8f}")
        print(f"  Tolerancia calculada = {tolerancia_calculada:.8f}")
        print()
        
        if tolerancia_calculada <= e:
            last_valid_iteration = iteraciones + 1
            break
        
        if fa * fxr < 0:
            b = xrActual
            fb = fxr
        else:
            a = xrActual
            fa = fxr
        
        xrAnterior = xrActual
        iteraciones += 1
    
    if last_valid_iteration is not None:
        print(f"Última iteración con tolerancia alcanzada: {last_valid_iteration}")
    else:
        print("No se alcanzó la tolerancia en ninguna iteración.")
    
    print(f"Último valor de a: {a:.8f}")
    print(f"Último valor de b: {b:.8f}")
    print(f"Número total de iteraciones: {iteraciones}")
    print(f"Tolerancia calculada: {tolerancia_calculada:.8f}")
    print(f"f(Xr): {fxr:.8f}")
    print()

#Llamamos al metodo para ejecutarlo 
falsaPosicion(fx, a, b, e, nmax)
