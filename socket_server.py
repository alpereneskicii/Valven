import os
import socket
import subprocess
import threading

sessions = {}

def run_command(cmd,session):
    print("Gelen komut: " + str(cmd))
    parts = cmd.split()
    if not parts:
        return " "
    cmd = parts[0]
    args = parts[1:]
    # We will discuss the cd command separately for changing the folder.
    if cmd == "cd": 
        if len(args) == 0:
            return session["current_dir"]
        new_path = os.path.abspath(os.path.join(session["current_dir"], args[0]))
        if os.path.isdir(new_path):
            session["current_dir"] = new_path
            return ""
        else:
            return f"cd: no such directory: {args[0]}"
    
    if cmd == "pwd":
        return session["current_dir"]
    shell_flag = not (cmd == "mkdir") 
    try:
        result = subprocess.run(
            [cmd] + args,
            cwd=session["current_dir"], 
            capture_output=True,
            text=True,
            shell=shell_flag,
            check=True,
            encoding='utf-8',    
            errors='replace'     
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Hata: {e}"

def handle_client(conn, address):
    print(f"[+] Connection from: {address}")
    sessions[address] = {"current_dir": os.getcwd()}

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            output = run_command(data,sessions[address])
            if output == "":  # If the output is empty, it is a bug. send [OK]. 
                output = "[OK]"
            conn.send(output.encode())
    except Exception as e:
        print(f"[!] Error with {address}: {e}")
    finally:
        conn.close()
        del sessions[address]
        print(f"[-] Connection closed: {address}")

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)  # Max 5 connections
    print(f"[*] Server listening on {host}:{port}")

    try:
        while True:
            conn, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, address)) # Start a new thread for each client
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    server_program()
