# 📘 Async Middleware in Django 5 — Complete Detailed Guide

---

# 1️⃣ What is Middleware?

Middleware is a layer that runs:

Client → Middleware → View → Middleware → Client

It can:

- Modify request before view
- Modify response after view
- Handle exceptions
- Run global logic (auth, logging, rate-limit)

---

# 2️⃣ What is Async Middleware?

In Django 5, middleware can be written using:

```python
async def __call__(self, request)


This allows non-blocking request handling when using ASGI.

Async middleware runs inside the event loop.

3️⃣ Requirements

To use async middleware:

Django 4.2+ (Fully stable in Django 5)

ASGI server (uvicorn, daphne, etc.)

async view or async operations inside middleware

Run with:

uvicorn myproject.asgi:application

4️⃣ Basic Async Middleware Structure
class AsyncExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):

        # Before view
        print("Before view")

        response = await self.get_response(request)

        # After view
        print("After view")

        return response


Important:

async def __call__

await self.get_response(request)

5️⃣ How Django Executes Async Middleware

If:

Middleware is async

View is async

Server is ASGI

Then entire pipeline runs async.

If mixed:

Django automatically adapts using threadpool.

6️⃣ Execution Order

If you have:

MIDDLEWARE = [
    "core.middleware.M1",
    "core.middleware.M2",
]


Execution:

Request →
M1 →
M2 →
View →
M2 (response) →
M1 (response)

Stack behavior.

7️⃣ Async Middleware With Database
class VisitorMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):

        await Visitor.objects.acreate(
            ip=request.META.get("REMOTE_ADDR")
        )

        response = await self.get_response(request)
        return response


Important:

Use async ORM methods (.acreate())

Always use await

8️⃣ Async Middleware With External API
import httpx

class ExternalCheckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):

        async with httpx.AsyncClient() as client:
            await client.get("https://example.com")

        response = await self.get_response(request)
        return response


Useful for:

Token validation

API verification

Microservices communication

9️⃣ Hybrid Middleware (Supports Both Sync + Async)

Best production-safe version:

from asgiref.sync import iscoroutinefunction

class HybridMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.is_async = iscoroutinefunction(get_response)

    async def __call__(self, request):

        if self.is_async:
            response = await self.get_response(request)
        else:
            response = self.get_response(request)

        return response


This prevents sync/async mismatch issues.

🔟 process_view / process_exception / process_template_response

Async versions supported:

class AdvancedMiddleware:

    async def __call__(self, request):
        response = await self.get_response(request)
        return response

    async def process_view(self, request, view_func, view_args, view_kwargs):
        print("Before view execution")

    async def process_exception(self, request, exception):
        print("Exception handled")

    async def process_template_response(self, request, response):
        return response


All hooks can be async in Django 5.

1️⃣1️⃣ Common Mistakes

❌ Forgetting await:

response = self.get_response(request)


✔ Correct:

response = await self.get_response(request)


❌ Using sync ORM:

Visitor.objects.create(...)


✔ Correct:

await Visitor.objects.acreate(...)

1️⃣2️⃣ Performance Reality

Async middleware helps when:

High concurrency

I/O operations (DB, APIs, network)

WebSockets

It does NOT:

Speed up database itself

Improve CPU-heavy tasks

Automatically make app faster

1️⃣3️⃣ When To Use Async Middleware

Use when:

Middleware performs async DB calls

Middleware calls external APIs

High traffic application

Real-time systems

Do NOT use when:

Simple logging only

Low traffic app

Entire project is sync

Using WSGI

1️⃣4️⃣ Internal Architecture (Simplified)

ASGI receives request
↓
Event loop handles coroutine
↓
Middleware chain built
↓
If async → run in event loop
If sync → run in threadpool
↓
Response returns same chain

Django auto-detects everything.

1️⃣5️⃣ Full Working Example
middleware.py
class AsyncTimingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):

        import time
        start = time.time()

        response = await self.get_response(request)

        end = time.time()
        print("Time:", end - start)

        return response

settings.py
MIDDLEWARE = [
    "core.middleware.AsyncTimingMiddleware",
]

async view
from django.http import JsonResponse

async def async_view(request):
    return JsonResponse({"message": "Async working"})

1️⃣6️⃣ Final Summary

Async Middleware in Django 5:

✔ Uses async def
✔ Requires ASGI
✔ Supports async ORM
✔ Handles concurrency better
✔ Works with async views

But:

❌ Not required for normal apps
❌ Not automatically faster
❌ Not needed for simple CRUD

🚀 Final Advice

Master:

Sync middleware

Request-response cycle

ORM deeply

Then async middleware

Async is advanced architecture tool.


If you want next, I can make a **diagram-based explanation version** for deep architectural understanding.
