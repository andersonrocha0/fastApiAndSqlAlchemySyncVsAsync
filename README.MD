## This project is a benchmark between sync and async way using SQLAlchemy and FastAPI

### Let's start with a short history:

* In my company we use flask with postgres to build ours microservices.
* We were studying start to use FastAPI.
* Then, in a beautiful day, I made some load tests in my FastAPI POC 
  project and, I figure out that my system has broken.
* So I found this issue at FastAPI GitHub: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/104#issuecomment-809418091
* After that I decided to try the new version of SQLAlchemy Async, and I have good news.
The SQLAlchemy Async way works like a charm.
  

### Technologies involved to execute this benchmark:

* [FastAPI](https://fastapi.tiangolo.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)  
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Uvicorn](https://www.uvicorn.org/)
* [wrk](https://github.com/wg/wrk)

### The benchmark results will depend on the hardware that you have. In my case my configs are:

* CPU: Core I7 9th Gen
* RAM: 32 GB


### How to run the projects?

```sh
docker-compose up
```


### How to test with wrk locally?

```sh
# Sync way
wrk -t12 -c12 -d10s http://localhost:8001/users
```

```sh
# Async way
wrk -t12 -c12 -d10s http://localhost:8000/users
```

### How to test with wrk in docker?

* You will need to know you docker ip, in my case is: <b>172.17.0.1</b>

```sh
# Sync way
docker run --rm  skandyla/wrk -t12 -c12 -d10s http://172.17.0.1:8001/users
```

```sh
# Async way
docker run --rm  skandyla/wrk -t12 -c12 -d10s http://172.17.0.1:8000/users
```



### Results with wrk in docker:

* First test with 1 thread and 1 connection:

```sh
# Sync way
docker run --rm  skandyla/wrk -t1 -c1 -d10s http://172.17.0.1:8001/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8001/users
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    17.95ms   17.05ms  55.92ms   78.65%
    Req/Sec    70.67     27.14   130.00     55.00%
  706 requests in 10.01s, 86.99KB read
Requests/sec:     70.55
Transfer/sec:      8.69KB
```

```sh
# Async way
docker run --rm  skandyla/wrk -t1 -c1 -d10s http://172.17.0.1:8000/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8000/users
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.78ms   16.94ms  54.42ms   77.96%
    Req/Sec    83.89     35.83   171.00     63.00%
  837 requests in 10.00s, 103.11KB read
Requests/sec:     83.67
Transfer/sec:     10.31KB
```

<hr>

* Second test with 12 threads and 12 connections:

```sh
# Sync way
docker run --rm  skandyla/wrk -t12 -c12 -d10s http://172.17.0.1:8001/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8001/users
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.07ms   18.75ms 121.46ms   62.96%
    Req/Sec    48.02     16.41   121.00     62.30%
  5759 requests in 10.01s, 709.72KB read
Requests/sec:    575.37
Transfer/sec:     70.91KB
```

```sh
# Async way
docker run --rm  skandyla/wrk -t12 -c12 -d10s http://172.17.0.1:8000/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8000/users
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    20.59ms   18.43ms  87.20ms   70.33%
    Req/Sec    56.76     19.47   170.00     72.67%
  6810 requests in 10.01s, 839.04KB read
Requests/sec:    679.99
Transfer/sec:     83.78KB
```

<hr>

* Third test with 12 threads and 24 connections:

```sh
# Sync way
docker run --rm  skandyla/wrk -t12 -c24 -d10s http://172.17.0.1:8001/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8001/users
  12 threads and 24 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    38.67ms   21.14ms 101.82ms   63.17%
    Req/Sec    51.82      9.07    80.00     77.58%
  6219 requests in 10.01s, 766.56KB read
Requests/sec:    621.07
Transfer/sec:     76.55KB
```

```sh
# Async way
docker run --rm  skandyla/wrk -t12 -c24 -d10s http://172.17.0.1:8000/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8000/users
  12 threads and 24 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    34.84ms   23.81ms 122.69ms   64.89%
    Req/Sec    58.80     13.49   110.00     74.00%
  7057 requests in 10.02s, 868.71KB read
Requests/sec:    704.39
Transfer/sec:     86.71KB
```

<hr>

* Fourth test with 12 threads and 48 connections:

```sh
# Sync way
docker run --rm  skandyla/wrk -t12 -c48 -d10s http://172.17.0.1:8001/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8001/users
  12 threads and 48 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.00us    0.00us   0.00us    -nan%
    Req/Sec     0.00      0.00     0.00      -nan%
  0 requests in 10.02s, 0.00B read
Requests/sec:      0.00
Transfer/sec:       0.00B
```

```sh
# Async way
docker run --rm  skandyla/wrk -t12 -c48 -d10s http://172.17.0.1:8000/users
```

```sh
# Result:
Running 10s test @ http://172.17.0.1:8000/users
  12 threads and 48 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    58.09ms   24.10ms 157.98ms   65.19%
    Req/Sec    68.91     14.58   111.00     70.85%
  8250 requests in 10.02s, 0.99MB read
Requests/sec:    823.63
Transfer/sec:    101.48KB
```


## Pay attention now

### After the fourth test we can see that FASTApi and SQLAlchemy SYNC WAY not work well.

* Some errors were logged in my console:

```sh
web-async_1           | ERROR:    Exception in ASGI application
web-async_1           | Traceback (most recent call last):
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/uvicorn/protocols/http/h11_impl.py", line 396, in run_asgi
web-async_1           |     result = await app(self.scope, self.receive, self.send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 45, in __call__
web-async_1           |     return await self.app(scope, receive, send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/fastapi/applications.py", line 199, in __call__
web-async_1           |     await super().__call__(scope, receive, send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/applications.py", line 111, in __call__
web-async_1           |     await self.middleware_stack(scope, receive, send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 181, in __call__
web-async_1           |     raise exc from None
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/middleware/errors.py", line 159, in __call__
web-async_1           |     await self.app(scope, receive, _send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/exceptions.py", line 82, in __call__
web-async_1           |     raise exc from None
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/exceptions.py", line 71, in __call__
web-async_1           |     await self.app(scope, receive, sender)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 566, in __call__
web-async_1           |     await route.handle(scope, receive, send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 227, in handle
web-async_1           |     await self.app(scope, receive, send)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/routing.py", line 41, in app
web-async_1           |     response = await func(request)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/fastapi/routing.py", line 201, in app
web-async_1           |     raw_response = await run_endpoint_function(
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/fastapi/routing.py", line 150, in run_endpoint_function
web-async_1           |     return await run_in_threadpool(dependant.call, **values)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/starlette/concurrency.py", line 34, in run_in_threadpool
web-async_1           |     return await loop.run_in_executor(None, func, *args)
web-async_1           |   File "/usr/local/lib/python3.9/concurrent/futures/thread.py", line 52, in run
web-async_1           |     result = self.fn(*self.args, **self.kwargs)
web-async_1           |   File "./sync.py", line 53, in read_users
web-async_1           |     users = get_users(session)
web-async_1           |   File "./sync.py", line 33, in get_users
web-async_1           |     return session.query(User).all()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2685, in all
web-async_1           |     return self._iter().all()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2820, in _iter
web-async_1           |     result = self.session.execute(
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1669, in execute
web-async_1           |     conn = self._connection_for_bind(bind, close_with_result=True)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1519, in _connection_for_bind
web-async_1           |     return self._transaction._connection_for_bind(
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 747, in _connection_for_bind
web-async_1           |     conn = bind.connect()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3095, in connect
web-async_1           |     return self._connection_cls(self, close_with_result=close_with_result)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 91, in __init__
web-async_1           |     else engine.raw_connection()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3174, in raw_connection
web-async_1           |     return self._wrap_pool_connect(self.pool.connect, _connection)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3141, in _wrap_pool_connect
web-async_1           |     return fn()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 301, in connect
web-async_1           |     return _ConnectionFairy._checkout(self)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 755, in _checkout
web-async_1           |     fairy = _ConnectionRecord.checkout(pool)
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 419, in checkout
web-async_1           |     rec = pool._do_get()
web-async_1           |   File "/usr/local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 133, in _do_get
web-async_1           |     raise exc.TimeoutError(
web-async_1           | sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: http://sqlalche.me/e/14/3o7r)
```


## However, we can use SQLAlchemy with ASYNC WAY:

### Results with wrk in docker:

* Fifth test with 12 threads and 200 connections for a long time:

```sh
# Async way
docker run --rm  skandyla/wrk -t12 -c200 -d300s http://172.17.0.1:8000/users
```
```sh
# Result:
Running 5m test @ http://172.17.0.1:8000/users
  12 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   245.74ms   80.78ms   1.12s    87.90%
    Req/Sec    65.39     21.17   180.00     65.91%
  235002 requests in 5.00m, 28.24MB read
Requests/sec:    783.13
Transfer/sec:     96.36KB
```

```sh
# Async way inserting data into database
docker run --rm  skandyla/wrk -t12 -c200 -d30s http://172.17.0.1:8000/users/insert-data-to-test
```

```sh
# Result inserting data into database:
Running 30s test @ http://172.17.0.1:8000/users/insert-data-to-test
  12 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   334.42ms  218.78ms   1.98s    62.74%
    Req/Sec    49.76     23.62   202.00     71.81%
  17677 requests in 30.10s, 2.16MB read
Requests/sec:    587.29
Transfer/sec:     73.46KB
```


### Conclusion:

* Looking at the tests results we can see that SQLAlchemy Async Way is better than with SQLAlchemy Sync Way. 
  To use Async Way you will need the new version of SQLAlchemy >= 1.4.
  

That's all. Thanks for reading.