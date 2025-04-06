import socket
import threading
import itertools
import requests

# ---------- MODULE 1: PORT SCANNER ----------
def port_scanner(target, ports):
    print(f"\n[+] Scanning ports on {target}")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass

# ---------- MODULE 2: BRUTE FORCER (Demo - HTTP Basic Auth) ----------
def brute_force_http_login(url, usernames, passwords):
    print(f"\n[+] Starting brute-force on {url}")
    for username in usernames:
        for password in passwords:
            response = requests.get(url, auth=(username, password))
            if response.status_code == 200:
                print(f"[SUCCESS] Username: {username}, Password: {password}")
                return
            else:
                print(f"[FAILED] {username}:{password}")
    print("[-] Brute force failed. No valid credentials found.")

# ---------- MAIN MENU ----------
def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Force HTTP Login")
    choice = input("Select option (1/2): ")

    if choice == '1':
        target = input("Enter target IP/domain: ")
        ports = list(range(20, 1025))  # Scan common ports
        port_scanner(target, ports)

    elif choice == '2':
        url = input("Enter URL (with HTTP): ")
        usernames = ["admin", "user", "test"]
        passwords = ["admin", "1234", "password", "test"]
        brute_force_http_login(url, usernames, passwords)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
