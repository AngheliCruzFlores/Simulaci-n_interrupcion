import threading
import random
import time
print("Presiona 'enter' para pausar la tarea actual y pasar a la siguiente.")
pausa1 = threading.Event()
pausa2 = threading.Event()
def resta():
    print("Ejecución de la primera tarea (resta)")
    for _ in range(20):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        res = num2 - num1
        print(f"Resta: {res}")
        time.sleep(0.5)
        if pausa1.is_set():
            pausa1.clear()
            pausa1.wait()
    print("Primera tarea (resta) finalizada")

def suma():
    print("Ejecución de la segunda tarea (suma)")
    for _ in range(20):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        res = num2 + num1
        print(f"Suma: {res}")
        time.sleep(0.5)
        if pausa2.is_set():
            pausa2.clear()
            pausa2.wait()
    pausa1.set()
    print("Segunda tarea (suma) finalizada")

def multiplicacion():
    print("Ejecución de la tercera tarea (multiplicacion)")
    for _ in range(10):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        res = num2 * num1
        print(f"Multiplicación: {res}")
        time.sleep(0.5)
        if pausa2.is_set():
            pausa2.clear()
            pausa2.wait()
    pausa2.set()
    print("Tercera tarea (multiplicacion) finalizada")

def division():
    print("Ejecución de la cuarta tarea (divicion)")
    for _ in range(10):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        while num2 == 0:
            num2 = random.randint(1, 100)
        res = num1 / num2
        print(f"División: {res}")
        time.sleep(0.5) 
    pausa2.set()
    print("Cuarta tarea (divicion) finalizada")

def ejecutar_tareas():
    global pausa
    thread_res = threading.Thread(target=resta)
    thread_sum = threading.Thread(target=suma)
    thread_mul = threading.Thread(target=multiplicacion)
    thread_div = threading.Thread(target=division)

    thread_res.start()
    input()
    pausa1.set()
    print("Tarea interrumpida")
    thread_sum.start()
    input()
    pausa2.set()
    print("Tarea interrumpida")
    thread_mul.start()
    thread_mul.join()
    pausa2.clear()
    input()
    pausa2.set()
    print("Tarea interrumpida")
    thread_div.start()
    thread_div.join()
    pausa2.clear()
    thread_sum.join()  
    pausa1.clear()  
    thread_res.join()

ejecutar_tareas()