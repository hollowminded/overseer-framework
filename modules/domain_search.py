import whois # domain lookup
import time # sleep
import os # cls
from datetime import datetime # Date filename

from util.rename_win import rename_window
from util.clear_s import clear_screen

"""Formats WHOIS data into a readable structure."""
def format_whois_data(web_info):
    return f"""\
Domain Name: {web_info.domain_name}
Domain ID: {web_info.domain_id}
Status: {", ".join(web_info.status) if web_info.status else "N/A"}

WHOIS Server: {web_info.whois_server}
Registrar: {web_info.registrar}
Registrar URL: {web_info.registrar_url}
Registrar Email: {web_info.registrar_email}
Registrar Phone: {web_info.registrar_phone}

Registrant Organization: {web_info.registrant_organization}
Registrant Country: {web_info.registrant_country}
Registrant Email: {web_info.registrant_email}

Admin Email: {web_info.admin_email}
Tech Email: {web_info.tech_email}

Updated Date: {web_info.updated_date}
Creation Date: {web_info.creation_date}
Expiration Date: {web_info.expiration_date}

Name Servers:
{chr(10).join(web_info.name_servers) if web_info.name_servers else "N/A"}
            """

def get_results_path():
    results_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
    os.makedirs(results_dir, exist_ok=True)  # Create folder if it doesn't exist
    return results_dir

def domain_search(domain_name):

    rename_window(f"Overseer | Domain Search")
    clear_screen()

    try:
        web_info = whois.whois(domain_name)

        # Format WHOIS data
        formatted_output = format_whois_data(web_info)

        # Print to console
        
        print("\n[+] WHOIS Information:\n")
        print(formatted_output)

        # Save results to a timestamped file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        results_dir = get_results_path()

        file_path = os.path.join(results_dir, f"domain_search_{timestamp}.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(formatted_output)

        print(f"\nSaved results to {results_dir}.")

    except Exception as err:
        print(f"[-] An error occured. {err}")

    input("\nPress Enter to return to main menu...")