# python_http_echo_over_tcp

```
ab -c 100 -n 1000000 -p /etc/ssl/certs/WoSign.pem http://127.0.0.1:8000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100000 requests
Completed 200000 requests
Completed 300000 requests
Completed 400000 requests
Completed 500000 requests
Completed 600000 requests
Completed 700000 requests
Completed 800000 requests
Completed 900000 requests
Completed 1000000 requests
Finished 1000000 requests


Server Software:        
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        1990 bytes

Concurrency Level:      100
Time taken for tests:   453.222 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      2171000000 bytes
Total body sent:        2087000000
HTML transferred:       1990000000 bytes
Requests per second:    2206.43 [#/sec] (mean)
Time per request:       45.322 [ms] (mean)
Time per request:       0.453 [ms] (mean, across all concurrent requests)
Transfer rate:          4677.88 [Kbytes/sec] received
                        4496.89 kb/s sent
                        9174.77 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0      29
Processing:     1   45  12.2     44     193
Waiting:        0   27   7.9     26     148
Total:          4   45  12.3     44     193

Percentage of the requests served within a certain time (ms)
  50%     44
  66%     49
  75%     52
  80%     54
  90%     61
  95%     67
  98%     76
  99%     82
 100%    193 (longest request)
 ```
