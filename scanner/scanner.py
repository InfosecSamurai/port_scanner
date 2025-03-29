import socket
import concurrent.futures

def scan_port(target, port):
    """Attempts to connect to a port and detect the service."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                return f"Port {port} is open ({service})"
    except Exception as e:
        return f"Error scanning port {port}: {e}"
    return None

def scan_ports(target, ports):
    """Scans multiple ports using threading."""
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda port: scan_port(target, port), ports)
        for result in results:
            if result:
                open_ports.append(result)
    return open_ports
