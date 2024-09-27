# HTTP Flood

An [HTTP Flood](https://en.m.wikipedia.org/wiki/HTTP_Flood) Python script designed to send multiple GET requests to a target server concurrently using multiprocessing, which can potentially overwhelm a normal website.

## How It Works

PyFlooder sends a configurable number of GET requests to a target using multiple processes, with each process capable of sending multiple requests. This allows for a high level of concurrency and traffic simulation.

## Usage

```python httpflood.py <Target_Hostname> <Port> <Number_of_Processes> <Number_of_Requests_per_Process> <Delay_between_Attacks>```

- `<Target_Hostname>`: The target URL (e.g., `http://example.com`).
- `<Port>`: The port to attack (default is `80` if not specified).
- `<Number_of_Processes>`: Number of concurrent processes to spawn (default is `1` if not specified).
- `<Number_of_Requests_per_Process>`: Number of requests each process should send (default is `1` if not specified).
- `<Delay_between_Attacks>`: Delay in seconds between starting each process (default is `0.01` if not specified).

### Examples

1. Basic attack with one process sending one request to a target on port 80:
    
    `python httpflood.py http://example.com`
    
2. Attack a target on port 8080 using 5 processes, each sending 10 requests:
    
    `python httpflood.py http://example.com 8080 5 10`
    
3. Attack a target on port 443 with 3 processes, each sending 20 requests, and a 0.1-second delay between starting each process:

    `python httpflood.py https://example.com 443 3 20 0.1`
    
## Requirements

- Python 3.x
- `httpx` library

You can install the `httpx` library using:

`pip install httpx`

## Features

- **Multiprocessing**: Uses Python's `multiprocessing` module to spawn multiple processes, allowing a high volume of concurrent requests.
- **Configurable**: Set the number of processes, requests per process, port, and delay for more granular control.
- **Supports HTTP/2**: Uses `httpx` for HTTP/2 support, allowing efficient handling of requests.

## Important Notice

This script is intended for educational purposes only. Unauthorized use of this tool against any website without permission is illegal and unethical.

## Credits

This project is based on the original work of [D4Vinci](https://github.com/D4Vinci/PyFlooder).
