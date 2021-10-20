import socket


def scan(target, ports):
  print('\n' + ' Starting Scan For ' + str(target))
  for port in range(1,ports):
    scan_port(target,port)


def scan_port(ipaddress, port):
  try:
    # create socket
    s = socket.socket()
    # connect to socket (ipaddress, port)
    s.connect((ipaddress, port))
    print("[+] Port Opened " + str(port))
    # close socket
    s.close()
  except:
    pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
  print("[*] Scanning Multiple Targets")
  for ip_addr in targets.split(','):
    scan(ip_addr.strip(' '), ports)
else:
  scan(targets,ports)
