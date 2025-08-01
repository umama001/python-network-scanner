# This script is a simple Network Scanner.
# It helps to find active devices (hosts) on a network by sending 'ping' requests.

import subprocess # This module lets us run external commands, like 'ping' in the operating system.
import platform   # This module helps us find out what operating system (Windows, Linux, macOS) we are running on.
import re         # This module is for Regular Expressions, used to check text patterns (like IP address format).
import sys        # This module allows us to access system-specific parameters and functions, like command-line arguments.

# --- Function to Perform Ping Scan ---
# This function sends a ping to a range of IP addresses.
def ping_scan(network_prefix, start_ip, end_ip):
    """
    Pings a range of IP addresses to find active hosts (devices that are online).

    Args:
        network_prefix (str): The first part of the IP address (e.g., "192.168.1.").
        start_ip (int): The starting number for the last part of the IP address range.
        end_ip (int): The ending number for the last part of the IP address range.
    """
    active_hosts = [] # Create an empty list to store the IP addresses of active hosts.

    # Check the operating system to choose the correct ping parameter.
    # Windows uses '-n 1' (number of pings), while Linux/macOS use '-c 1' (count of pings).
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    print(f"Scanning network: {network_prefix}{start_ip}-{end_ip}") # Tell the user which range is being scanned.

    # Loop through each number in the specified IP range (from start_ip to end_ip).
    for i in range(start_ip, end_ip + 1):
        ip_address = f"{network_prefix}{i}" # Build the full IP address (e.g., "192.168.1.5").
        command = ['ping', param, '1', ip_address] # Prepare the ping command (e.g., 'ping -c 1 192.168.1.5').

        try:
            # Run the ping command using subprocess.
            # capture_output=True: Collects the output of the ping command.
            # text=True: Decodes the output as text.
            # timeout=1: Waits for 1 second for a response. If no response, it's a timeout.
            # check=False: Prevents an error if the ping command fails (e.g., host is down).
            result = subprocess.run(command, capture_output=True, text=True, timeout=1, check=False)

            # Check the ping command's output to see if the host is active.
            # "Reply from" is found in Windows ping output for active hosts.
            # "bytes from" is found in Linux/macOS ping output for active hosts.
            if "Reply from" in result.stdout or "bytes from" in result.stdout:
                print(f"Host {ip_address}: UP") # Print that the host is active.
                active_hosts.append(ip_address) # Add the active host's IP to our list.
            else:
                print(f"Host {ip_address}: DOWN") # Print that the host is not active.

        except subprocess.TimeoutExpired:
            # This happens if the ping command takes too long to get a response.
            print(f"Host {ip_address}: DOWN (Timeout)")
        except Exception as e:
            # Catch any other unexpected errors during the scan.
            print(f"Error scanning {ip_address}: {e}")

    print("\n--- Scan Summary ---") # Print a summary header.
    if active_hosts: # If there are any active hosts in our list.
        print("Active hosts found:")
        for host in active_hosts: # Loop through and print each active host.
            print(f"- {host}")
    else: # If the active_hosts list is empty.
        print("No active hosts found in the specified range.")

# --- Main Function to Run the Script ---
# This function handles command-line arguments and calls the ping_scan function.
def main():
    # Check if the correct number of command-line arguments is provided.
    # sys.argv[0] is the script name itself, so we expect 3 more arguments (4 total).
    if len(sys.argv) != 4:
        print("Usage: python network_scanner.py <network_prefix> <start_last_octet> <end_last_octet>")
        print("Example: python network_scanner.py 192.168.1. 1 254")
        sys.exit() # Exit the script if arguments are wrong.

    network_prefix = sys.argv[1] # Get the network prefix from the first command-line argument.

    try:
        start_ip = int(sys.argv[2]) # Convert the second argument (start IP) to an integer.
        end_ip = int(sys.argv[3])   # Convert the third argument (end IP) to an integer.
        
        # Validate that the last octets are within a valid range (0-255) and start is not greater than end.
        if not (0 <= start_ip <= 255 and 0 <= end_ip <= 255 and start_ip <= end_ip):
            print("Last octets must be between 0 and 255, and start must be less than or equal to end.")
            sys.exit() # Exit if validation fails.
    except ValueError:
        # Catch an error if the start_ip or end_ip are not valid numbers.
        print("Invalid start/end IP. Please enter integers.")
        sys.exit() # Exit if there's a type error.

    # Basic validation for the network_prefix format (e.g., "192.168.1.").
    # It checks for three sets of 1-3 digits followed by a dot, and ending with a dot.
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.$", network_prefix):
        print("Invalid network prefix format. Example: 192.168.1.")
        sys.exit() # Exit if the format is wrong.

    ping_scan(network_prefix, start_ip, end_ip) # Call the main scanning function with the provided arguments.

# This is a standard Python line. It means:
# If this script is being run directly (not imported as a module into another script),
# then call the 'main()' function to start the program.
if __name__ == "__main__":
    main()
