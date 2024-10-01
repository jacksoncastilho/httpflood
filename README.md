# HTTP Flood

This script is a simple tool that allows you to perform multiple HTTP requests to a target URL. It lets you choose the HTTP method (GET or POST), the number of parallel processes, and the number of requests per process, which can be useful for load and performance testing of an endpoint.

> **Warning:** Use this tool only for educational purposes or testing on your own systems or systems for which you have authorization. Unauthorized use can be illegal and may result in penalties.

## How It Works

The script begins by reading user-defined command-line arguments like the target URL, HTTP method, number of processes, and requests. It then uses Python's multiprocessing module to create multiple processes, each sending the specified number of GET or POST requests using the httpx library with HTTP/2 support. A delay can be added between requests to simulate real-world traffic. Errors are handled gracefully, ensuring the process continues without interruption. Once all processes complete their assigned requests, the script terminates, providing an overview of the total requests sent.

## Usage

```
python httpflood.py -t <TARGET_URL> -p <PORT> -m <METHOD> -P <NUM_PROCESSES> -r <NUM_REQUESTS> -d <DELAY> -D <DATA>
```

## Arguments

- `-t` or `--target` (required): Target URL for the test. E.g., `http://example.com`
- `-p` or `--port`: Port to be used (default: `80`)
- `-m` or `--method`: HTTP method to be used (GET or POST, default: `GET`)
- `-P` or `--process`: Number of parallel processes to be created (default: `1`)
- `-r` or `--request`: Number of requests per process (default: `1`)
- `-d` or `--delay`: Interval between requests, in seconds (default: `0.1`)
- `-D` or `--data`: Request body in JSON format for POST methods (e.g., `{"param": 1}`)

## Usage Examples

1. Send 10 GET requests with 2 parallel processes:
   ```bash
   python script.py -t http://example.com -P 2 -r 5
   ```

2. Send POST requests with a JSON payload:
   ```bash
   python script.py -t http://example.com/api -m POST -P 3 -r 2 -D '{"key": "value"}'
   ```
    
## Requirements

- Python 3.x
- `httpx` and `argparse` libraries

You can install the `httpx` library using:

```
pip install httpx
```

## Features

- **Multiple HTTP Methods**: Supports both `GET` and `POST` requests for versatile testing.
- **Parallel Processing**: Can spawn multiple processes to send high volumes of requests concurrently.
- **Customizable Requests**: Allows setting the number of requests per process and adding delays, providing control over traffic patterns.
- **JSON Payload Support**: Easily send JSON data with `POST` requests for testing API endpoints.
- **HTTP/2 Support**: Utilizes HTTP/2 via `httpx` for efficient request handling.

## Credits

This project is based on the original work of [D4Vinci](https://github.com/D4Vinci/PyFlooder).
