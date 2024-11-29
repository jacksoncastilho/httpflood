# HTTP Flood

This script is a simple tool that allows you to perform multiple HTTP requests to a target URL. It lets you choose the HTTP method (GET or POST), the number of parallel processes, and the number of requests per process, which can be useful for load and performance testing of an endpoint.

> **Warning:** Use this tool only for educational purposes or testing on your own systems or systems for which you have authorization. Unauthorized use can be illegal and may result in penalties.

## How It Works

The script begins by reading user-defined command-line arguments like the target URL, HTTP method, number of processes, and requests. It then uses Python's multiprocessing module to create multiple processes, each sending the specified number of GET or POST requests using the httpx library with HTTP/2 support. A delay can be added between requests to simulate real-world traffic. Errors are handled gracefully, ensuring the process continues without interruption. Once all processes complete their assigned requests, the script terminates, providing an overview of the total requests sent.

## Usage

```
./httpflood.py [-h] -t TARGET [-p PORT] [-m METHOD] [-P PROCESS] [-r REQUEST] [-d DELAY] [-D DATA] [-f FORMAT] [-H HEADER]
```

## Arguments

- `-t` or `--target` (required): Target URL for the test (e.g., `http://example.com`)
- `-p` or `--port`: Port to be used (default: `80`)
- `-m` or `--method`: HTTP method to be used (GET or POST, default: `GET`)
- `-P` or `--process`: Number of parallel processes to be created (default: `1`)
- `-r` or `--request`: Number of requests per process (default: `1`)
- `-d` or `--delay`: Interval between requests, in seconds (default: `0.1`)
- `-D` or `--data`: Request body (e.g., `{"param": 1, "param": "asd"}`)
- `-f` or `--format`: Format of the request body (e.g., "data" for form-encoded or "json" for JSON)
- `-H` or `--header`: Custom headers for the HTTP/2 request, formatted as a JSON string. Headers must use lowercase keys to comply with HTTP/2 requirements (e.g., '{"authorization": "Bearer token", "content-type": "application/json"}')

## Usage Examples

1. Send GET requests:
   ```bash
   ./httpflood.py -t "https://example.com/DVWA/vulnerabilities/csrf/?password_current=asd&password_new=asd&password_conf=asd&Change=Change&user_token=a89327a2b94992de6a3578e1f623ec74#" -p 443 -P 1 -r 1
   ```

2. Send POST requests:
   ```bash
   ./httpflood.py -t https://example.com/DVWA/login.php -p 443 --method POST -H "{\"content-type\": \"application/x-www-form-urlencoded\"}" --data "username=asd&password=asd&Login=Login&user_token=a822769d7aaa50e7a68aa3ad5f2698eb" -P 1 -r 1
   ```

## Credits

This project is based on the original work of [D4Vinci](https://github.com/D4Vinci/PyFlooder).
