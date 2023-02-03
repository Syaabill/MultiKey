from pynput import mouse, keyboard
import socket

def receive_mouse_event(event):
    mouse_controller.move(event[0], event[1])

def receive_keyboard_event(event):
    keyboard_controller.press(event[0])
    keyboard_controller.release(event[0])

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

while True:
    event = s.recv(1024)
    if event.startswith(b'mouse'):
        receive_mouse_event(event[6:])
    elif event.startswith(b'keyboard'):
        receive_keyboard_event(event[9:])
