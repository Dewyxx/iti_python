import psutil
# Network I/O statistics
print(psutil.net_io_counters())

# Active connections
print(psutil.net_connections())
