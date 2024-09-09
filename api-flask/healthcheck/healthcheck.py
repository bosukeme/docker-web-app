import http.client
import os
import sys

# Define options
timeout = 2  # seconds
host = 'localhost'
port = os.getenv('PORT', 5000)
path = '/ping'

try:
    # Create connection
    conn = http.client.HTTPConnection(host, port, timeout=timeout)
    
    # Make request
    conn.request("GET", path)
    
    # Get response
    res = conn.getresponse()
    print(f"STATUS: {res.status}")
    
    # Set exit code based on status
    sys.exit(0 if res.status == 200 else 1)

except Exception as err:
    print(f"ERROR: {err}")
    sys.exit(1)

finally:
    if 'conn' in locals():
        conn.close()
