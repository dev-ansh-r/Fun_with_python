import socket

def connect_internet():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
while 1:
    if connect_internet():
        #run python file
        import app.py
        print("internet connected")
    else:
        print("internet not connected")


