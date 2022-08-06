import rotatescreen
import time
import win32api


screen = rotatescreen.get_primary_display()
start = screen.current_orientation

for i in range(1, 10):
    a = abs((start - i*90) % 360)
    screen.rotate_to(a)
    time.sleep(0.5)
