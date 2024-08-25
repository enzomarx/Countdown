import time
import pyautogui
import threading

# This means that the program will wait for 3 seconds before proceeding to
# execute the rest of the code. This can be useful in scenarios where you want to introduce a delay or
# wait for a specific duration before starting the main functionality of the program.
time.sleep(3)

def contagem_regressiva():
    """
    The function `contagem_regressiva` is intended to perform a countdown for 30 seconds using a library
    called `pyautogui`.
    """
    pyautogui.countdown(30)
    
def monitorar_tempo():
    """
    The function "monitorar_tempo" sets a total time of 30 seconds and an interval of 1 second for
    monitoring.
    """
    total_tempo = 30
    intervalo = 1

# The code snippet you provided is a `for` loop that iterates over a range of numbers starting from
# `total_tempo` (which is 30 in this case) down to 0 with a step size of `-intervalo` (which is 1 in
# this case).
    for restante in range(total_tempo, 0, -intervalo):
        #print(f"Tempo Restante: {restante} segundos")
        time.sleep(intervalo)
        
        if restante == 15:
            print("Congratulations!")

def main():
    """
    The main function creates two threads for countdown and time monitoring tasks and starts them
    concurrently.
    """
    thread_contagem = threading.Thread(target=contagem_regressiva)
    thread_monitoramento = threading.Thread(target=monitorar_tempo)
    
    thread_contagem.start()
    thread_monitoramento.start()
    
    thread_contagem.join()
    thread_monitoramento.join()
            
                
# The `if __name__ == "__main__":` block in Python is a common idiom used to ensure that the code
# inside it is only executed if the script is run directly, and not imported as a module into another
# script.
if __name__ == "__main__":
    main()