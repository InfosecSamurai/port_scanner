def parse_port_range(port_range):
    """Parses a port range in the format 20-80 and returns a list of ports."""
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        return list(range(start, end + 1))
    else:
        return [int(port_range)]
