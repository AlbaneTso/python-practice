import socket

while True :
    try : 
        url = input("Enter url")
        if url.startswith('https://') or url.startswith('http://'):
            host = url.split('/')[2]
        else :
            host = url
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)
        chars = b""
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            chars += data
        chunk = chars.decode()[:3000]
        print(f"{chunk} this file has {len(chunk)} characters")
        mysock.close()
        break
    except Exception as e:
        print(f"error {e}, try again a correct url")
        continue