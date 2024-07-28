import math
import numpy as np

def biseccion(f, a, b, tol):
        if f(a) * f(b) > 0:
            print("La función no cambia de signo en el intervalo dado.")
            return None

        while abs(b - a) > tol:
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c

        return (a + b) / 2

def metodo_del_trapecio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1] + 2 * np.sum(y[1:-1])
    integral *= h / 2

    return integral

def newton_raphson(f, df, x0, tol, max_iter):
    for n in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        # Check for division by zero and very small derivative
        if abs(dfx) < 1e-10:
            print("La derivada es muy pequeña, probablemente no se converge.")
            return None
        if abs(fx) < 1e-10:
            return x0

        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    print("El método no converge después de", max_iter, "iteraciones.")
    return None

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def taylor_polynomial(f, a, x, n):
    p = 0
    for k in range(n + 1):
        p += (f.__call__((lambda x: x**k))(a) / factorial(k)) * (x - a)**k
    return p

def suma_riemann(f, x_values):
    s = 0
    for i in range(len(x_values) - 1):
        dx = x_values[i+1] - x_values[i]
        s += f((x_values[i] + x_values[i+1]) / 2) * dx  # Método del punto medio
    return s

def leer_funcion():
    f_str = input("Ingrese la función f(x) en términos de x (ej: x**2 - 2): ")
    try:
        f = eval('lambda x: ' + f_str)
    except Exception as e:
        print("Error al ingresar la función:", e)
        return None
    return f

def obtener_derivada():
    df_str = input("Ingrese la derivada de f(x) en términos de x (ej: 2*x): ")
    try:
        df = eval('lambda x: ' + df_str)
    except Exception as e:
        print("Error al ingresar la derivada:", e)
        return None
    return df

def main():
    while True:
        print("Selecciona el método:")
        print("1. Método de Newton-Raphson")
        print("2. Polinomio de Taylor")
        print("3. Suma de Riemann")
        print("4. Método de Bisección")
        print("5. Método del Trapecio")
        print("6. Salir :)")
        choice = int(input("Ingrese su elección: "))

        if choice == 1:
            # Método de Newton-Raphson
            x0 = float(input("Ingrese el valor inicial: "))
            tol = float(input("Ingrese la tolerancia: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones: "))
            f = leer_funcion()
            df = obtener_derivada()
            if f is not None and df is not None:
                root = newton_raphson(f, df, x0, tol, max_iter)
                if root is not None:
                    print("La raíz aproximada es:", root)
                else:
                    print("El método no convergió.")
        elif choice == 2:
            # Polinomio de Taylor
            f_str = input("Ingrese la función f(x) en términos de x: ")
            try:
                f = eval('lambda x: ' + f_str)
            except Exception as e:
                print("Error al ingresar la función:", e)
                exit()
            a = float(input("Ingrese el punto de expansión a: "))
            n = int(input("Ingrese el grado del polinomio: "))
            x_values = input("Ingrese los puntos a evaluar separados por comas: ").split(',')
            x_values = [float(x) for x in x_values]
            for x in x_values:
                p = taylor_polynomial(f, a, x, n)
                print(f"El valor del polinomio de Taylor en x={x} es: {p}")
        elif choice == 3:
            # Suma de Riemann
            f_str = input("Ingrese la función f(x) en términos de x: ")
            try:
                f = eval('lambda x: ' + f_str)
            except Exception as e:
                print("Error al ingresar la función:", e)
                exit()
            x_values_str = input("Ingrese los puntos de evaluación separados por comas (ej: 0,1,2,3): ")
            x_values = [float(x) for x in x_values_str.split(',')]
            result = suma_riemann(f, x_values)
            print(f"La aproximación de la integral es: {result}")
        elif choice == 4:
            # Método de Bisección
            f_str = input("Ingrese la función f(x) en términos de x: ")
            try:
                f = eval('lambda x: ' + f_str)
            except Exception as e:
                print("Error al ingresar la función:", e)
                exit()
            a = float(input("Ingrese el extremo izquierdo del intervalo: "))
            b = float(input("Ingrese el extremo derecho del intervalo: "))
            tol = float(input("Ingrese la tolerancia: "))
            root = biseccion(f, a, b, tol)
            if root is not None:
                print("La raíz aproximada es:", root)
            else:
                print("El método no convergió.")
        elif choice == 5:
            # Método del Trapecio
            f_str = input("Ingrese la función f(x) en términos de x: ")
            try:
                f = eval('lambda x: ' + f_str)
            except Exception as e:
                print("Error al ingresar la función:", e)
                exit()
            a = float(input("Ingrese el límite inferior del intervalo: "))
            b = float(input("Ingrese el límite superior del intervalo: "))
            n = int(input("Ingrese el número de subintervalos: "))
            resultado = metodo_del_trapecio(f, a, b, n)
            print("La integral definida de f(x) = x^2 en [", a, ",", b, "] con", n, "subintervalos es aproximadamente:", resultado.round(5))
        elif choice == 6:
            #Salida del programa.
            break
        else:
            print("Opción inválida.")

        continuar = input("¿Desea realizar otra operacion? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
  main()
