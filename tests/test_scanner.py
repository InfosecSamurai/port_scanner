import unittest
from scanner.scanner import scan_ports
from scanner.utils import parse_port_range

class TestScanner(unittest.TestCase):
    def test_parse_port_range(self):
        self.assertEqual(parse_port_range("80"), [80])
        self.assertEqual(parse_port_range("20-22"), [20, 21, 22])

    def test_scan_ports(self):
        """Test scanning a common open port like 80 (HTTP)."""
        result = scan_ports("scanme.nmap.org", [80])
        self.assertTrue(any("Port 80 is open" in res for res in result))

if __name__ == "__main__":
    unittest.main()
