import socket

def check_port(port, host='127.0.0.1'):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  
        s.connect((host, port))
        s.close()
        return True
    except socket.gaierror:
        print('host couldn\'t resolve')
    except socket.error:
        print('server not responding!!')
    except KeyboardInterrupt:
        print('exit by pressing a key on the keyboard')
if __name__ == "__main__":
    
    port_to_check = int(input("Enter the port number to check: "))

    if check_port(port_to_check):
        print(f"Port {port_to_check} is open.")
    else:
        print(f"Port {port_to_check} is closed.")


       
