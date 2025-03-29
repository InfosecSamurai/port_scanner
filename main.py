import argparse
from scanner.scanner import scan_ports
from scanner.utils import parse_port_range

def main():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner with Service Detection")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("ports", help="Port or port range (e.g., 20-80 or 443)")
    
    args = parser.parse_args()
    ports = parse_port_range(args.ports)

    print(f"Scanning {args.target} for open ports...\n")
    results = scan_ports(args.target, ports)
    
    if results:
        for res in results:
            print(res)
    else:
        print("No open ports detected.")

if __name__ == "__main__":
    main()
