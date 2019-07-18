import tcp_server

def main():
    s = tcp_server.FTPServer()
    s.start()


if __name__ == "__main__":
    main()