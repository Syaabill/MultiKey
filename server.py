from pynput import mouse, keyboard
import socket

def send_mouse_event(event):
    s.send(event)

def send_keyboard_event(event):
    s.send(event)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen()

connection, address = s.accept()
print(f'Connected to {address}')

mouse_listener = mouse.Listener(on_move=send_mouse_event, on_click=send_mouse_event, on_scroll=send_mouse_event)
keyboard_listener = keyboard.Listener(on_press=send_keyboard_event, on_release=send_keyboard_event)

mouse_listener.start()
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()
