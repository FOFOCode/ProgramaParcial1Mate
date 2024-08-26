#Hecho por Rodolfo Rivas Rodriguez y Diego Andres Hernandez Contreras.

import sympy as sp #Biblioteca de mate
from decimal import * #no pude setear con esto :(

class Biseccion:
    #Flexible :)
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

    #Evalua la funcion hace que la X tome el valor que se le asignara con a y b
    def eval_func(expr, val):
        x = sp.symbols('x')
        return expr.subs(x,val)


    def biseccion(fx, a, b, e, nmax):
        expr = sp.sympify(fx)
        fa = eval_func(expr, a)
        fb = eval_func(expr, b)
        
        print()
        print(f"f(a) = {fa}, f(b) = {fb}")
        print()
        
        iteraciones = 0
        last_valid_iteration = None

        while iteraciones < nmax:
            m = (a + b) / 2
            fm = eval_func(expr, m)
            
            
            tolerancia_calculada = abs((b - a) / 2) * 100
            
            print(f"Iteración {iteraciones + 1}:")
            print(f"  a = {a}, b = {b}")
            print(f"  m = {m}, f(m) = {fm}")
            print(f"  Tolerancia calculada = {tolerancia_calculada}")
            print()
            
            
            if tolerancia_calculada <= e:
                last_valid_iteration = iteraciones
                break
            
            if fa * fm < 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm
            
            iteraciones += 1

        
        if last_valid_iteration is not None:
            print(f"Última iteración con tolerancia alcanzada: {last_valid_iteration + 1}")
        else:
            print("No se alcanzó la tolerancia en ninguna iteración.")

        # Calcula la tolerancia final
        #No se setearon :(
        tolerancia_calculada = abs((b - a) / 2) * 100
        print(f"Último valor de a: {a:.8f}")
        print(f"Último valor de b: {b:.8f}")
        print(f"Número total de iteraciones: {iteraciones}")
        print(f"Tolerancia calculada: {tolerancia_calculada:.8f}")
        print(f"f(m): {fm:.8f}")
        print()
   
    #Llamamos al metodo para ejecutarlo 
    biseccion(fx, a, b, e, nmax)

    #la raiz es m.