import nmap
from util.rename_win import rename_window
from util.clear_s import clear_screen
import sys
import os
from datetime import datetime

def nmap_scanner():
    rename_window("Overseer | Nmap Network Scanner")
    clear_screen()
    
    print("Nmap Network Scanner")
    print("-------------------")
    
    # Get target IP/domain
    target = input("Enter target IP or domain: ").strip()
    
    # Scan mode selection
    print("""\n
Scanning Modes:
[1] Simple Scan (Basic Port Scan)
[2] Deep Scan (More Comprehensive)
[3] Extreme Scan (Intensive Scan)
    """)
    
    mode = input("\nSelect Scan Mode [1/2/3]: ").strip()
    
    # Initialize Nmap scanner
    nm = nmap.PortScanner()
    
    try:
        # Scan modes with increasing complexity
        match mode:
            case "1":
                print("\n[*] Performing Simple Scan...")
                nm.scan(target, arguments='-sV -sC')
            
            case "2":
                print("\n[*] Performing Deep Scan...")
                nm.scan(target, arguments='-sV -sC -p- -A')
            
            case "3":
                print("\n[*] Performing Extreme Scan...")
                nm.scan(target, arguments='-sS -sV -sC -p- -A -O --script vuln')
            
            case _:
                print("Invalid scan mode selected.")
                return
        
        # Prepare results
        results = ""
        for host in nm.all_hosts():
            results += f"Host: {host} ({nm[host].hostname()})\n"
            results += f"State: {nm[host].state()}\n\n"
            
            # Protocol and port information
            for proto in nm[host].all_protocols():
                results += f"Protocol: {proto}\n"
                ports = nm[host][proto].keys()
                ports = sorted(ports)
                
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port].get('name', 'Unknown')
                    version = nm[host][proto][port].get('version', 'Unknown')
                    
                    results += f"Port: {port}\t State: {state}\t Service: {service}\t Version: {version}\n"
                
                results += "\n"
        
        # Print results to console
        print("\n[+] Scan Results:\n")
        print(results)
        
        # Save results
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        results_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
        os.makedirs(results_dir, exist_ok=True)
        
        file_path = os.path.join(results_dir, f"nmap_scan_{timestamp}.txt")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(results)
        
        print(f"\n[+] Results saved to {file_path}")
    
    except Exception as e:
        print(f"[-] An error occurred during scanning: {e}")
    
    input("\nPress Enter to return to main menu...")