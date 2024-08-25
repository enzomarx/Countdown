# Countdown Timer with Python
### This Python script uses the pyautogui library to display a visual countdown and runs a parallel timer to print a message when the countdown reaches 15 seconds.

## Description
- Visual Countdown: Uses pyautogui.countdown(30) to show a 30-second countdown on the screen.
- Time Monitoring: Runs a parallel timer to check the remaining time and prints "Congratulations!" when there are 15 seconds left.

## How It Works
- contagem_regressiva(): Starts a 30-second visual countdown using pyautogui.
- monitorar_tempo(): Continuously checks the remaining time and prints a message when the timer reaches 15 seconds.
- main(): Creates and runs two threads concurrently: one for the countdown and one for time monitoring.
The script starts by initializing the countdown and monitoring in separate threads to run simultaneously.

