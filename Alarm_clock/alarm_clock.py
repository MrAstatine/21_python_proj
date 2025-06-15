from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


# playsound("alarm_sound.mp3")
def alarma(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(
            f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d} minutes and {seconds_left:02d} seconds",
            end="\r",
        )
    playsound("alarm_sound.mp3")


minutes = int(input("Enter the number of minutes for the alarm: "))
seconds = int(input("Enter the number of seconds for the alarm: "))
total_time = minutes * 60 + seconds
if total_time <= 0:
    print("Please enter a valid time greater than zero.")
alarma(total_time)
