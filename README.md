# pracmin_task9.2
rest_server

```
bnaich:~/Desktop/pracmin/6/server/pracmin_server_rest/pracmin_task8.3$ docker-compose up
Starting pracmin_task83_rediska_1 ... done
Starting pracmin_task83_echo_server_1 ... done
Attaching to pracmin_task83_rediska_1, pracmin_task83_echo_server_1
rediska_1      | 1:C 11 Nov 2019 14:01:29.089 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
rediska_1      | 1:C 11 Nov 2019 14:01:29.089 # Redis version=5.0.6, bits=64, commit=00000000, modified=0, pid=1, just started
.....................................................................................
condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
rediska_1      | 1:M 11 Nov 2019 14:01:29.090 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
rediska_1      | 1:M 11 Nov 2019 14:01:29.090 * Ready to accept connections
echo_server_1  |  * Serving Flask app "echo-server" (lazy loading)
echo_server_1  |  * Environment: production
echo_server_1  |    WARNING: This is a development server. Do not use it in a production deployment.
echo_server_1  |    Use a production WSGI server instead.
echo_server_1  |  * Debug mode: off
echo_server_1  |  * Running on http://0.0.0.0:65432/ (Press CTRL+C to quit)
```

```
bnaich:~/Desktop/pracmin/6/server/pracmin_server_rest$ telnet localhost 2000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
PUT /storage_server?key=max HTTP/1.1
Content-Type: application/json
Content-Length: 20

{"Max":"Scherbakov"}
HTTP/1.0 201 CREATED
Content-Type: text/html; charset=utf-8
Content-Length: 7
Server: Werkzeug/0.16.0 Python/3.8.0
Date: Mon, 11 Nov 2019 14:03:32 GMT

CreatedConnection closed by foreign host.
bnaich:~/Desktop/pracmin/6/server/pracmin_server_rest$ telnet localhost 2000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET /storage_server?key=max HTTP/1.1

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 20
Server: Werkzeug/0.16.0 Python/3.8.0
Date: Mon, 11 Nov 2019 14:03:55 GMT

{"Max":"Scherbakov"}Connection closed by foreign host.

```
