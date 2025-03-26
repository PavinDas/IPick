import requests
import json
from colorama import init, Fore, Style

init()

if __name__ == "__main__":
    banner = """
                                        
@@@  @@@@@@@   @@@   @@@@@@@  @@@  @@@  
@@@  @@@@@@@@  @@@  @@@@@@@@  @@@  @@@  
@@!  @@!  @@@  @@!  !@@       @@!  !@@  
!@!  !@!  @!@  !@!  !@!       !@!  @!!  
!!@  @!@@!@!   !!@  !@!       @!@@!@!   
!!!  !!@!!!    !!!  !!!       !!@!!!    
!!:  !!:       !!:  :!!       !!: :!!   
:!:  :!:       :!:  :!:       :!:  !:!  
 ::   ::        ::   ::: :::   ::  :::  
:     :        :     :: :: :   :   :::  
                                        
    """
    print(f"{Fore.LIGHTRED_EX}{banner}{Style.RESET_ALL}")
    print()
    print(f"{Fore.RED}{Style.BRIGHT}[+]  Creator    :  Pavin Das{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[+]  GitHub     :  PavinDas{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[+]  Instagram  :  pavin__das{Style.RESET_ALL}")
    print()
    print()
    try:
        ip = input("Enter IP Address: ")
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = json.loads(response.content)
        mapUrl = f"https://www.google.com/maps/@?api=1&map_action=map&center={data['lat']}%2C{data['lon']}&zoom=15&basemap=satellite&layer=transit"

        print()
        print(f"{Fore.CYAN}[+] CITY\t {data['city']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] ISP\t\t { data['isp']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] ISP\t\t { data['country']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] REG\t\t { data['regionName']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] TIME\t { data['timezone']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] ZIP\t\t { data['zip']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] LAT\t\t { data['lat']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] LON\t\t { data['lon']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] MAP\t\t {mapUrl}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print()
        print(f"{Fore.RED} \n[-] Exited {Style.RESET_ALL}")
    except Exception:
        print()
        print(f"{Fore.YELLOW}[!] Enter a valid IP Address {Style.RESET_ALL}")
