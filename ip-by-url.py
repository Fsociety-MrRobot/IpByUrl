import socket
import pyfiglet
from colorama import Fore, Back, Style


def get_ipaddr_by_hostname(hostname):

	try: 
		host = Fore.CYAN + f'[$] Host: {hostname}'
		ip = Fore.GREEN + f'[+] IP address: {socket.gethostbyname(hostname)}'
		msg = f'{host}\n{ip}'
		return msg


	except socket.gaierror as error:
		error_msg = f'[!] Invalid Hostname - {error}.'
		msg = Fore.RED + error_msg
		return msg
		

def main():
	preview = pyfiglet.figlet_format('PBRL Tool', font = 'isometric1')
	print(f'{preview}\n ')
	
	hostname = input('Please enter a website address (URL): ')
	print(get_ipaddr_by_hostname(hostname))


if __name__ == '__main__':
	main()
