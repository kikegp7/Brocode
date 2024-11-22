import time 
import datetime
import pygame 


def set_alarm(alarm: str):
    print(f"Alarm set for {alarm}")
    sound = "C:/Users/luis_/Documents/Luis Gamboa - Programacion/Brocode/my_alarm.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm:
            print("Wake up! 😊")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


def main():
    alarm_time = input("Set alarm time in 24 hours format (HH:MM:SS): ")
    set_alarm(alarm_time)
    

if __name__ == "__main__":
    main()