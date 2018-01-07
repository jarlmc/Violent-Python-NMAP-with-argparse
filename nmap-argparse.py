import nmap
import argparse

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print ("[*] " + tgtHost + " tcp/"+tgtPort +" "+state)

def main():
    parser = argparse.ArgumentParser(description='Enter: -H <IP> -p <Ports[s]>')
    parser.add_argument('-H', '--Host',
                      action="store", help='specify target host')
    parser.add_argument('-p', '--port',
                      action="store", help='specify target port[s] separated by comma')
    
    args = parser.parse_args()
    
    tgtHost = args.Host
    tgtPort = str(args.port).split(',')
    
    if (tgtHost == None) | (tgtPort == None):
        print (parser.description)
        exit(0)
    for tgtPorts in tgtPort:
        nmapScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()