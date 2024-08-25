import time
import pyautogui
import threading

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
            
                
if __name__ == "__main__":
    main()