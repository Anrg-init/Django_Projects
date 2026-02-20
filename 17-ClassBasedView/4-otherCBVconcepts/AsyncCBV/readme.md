# Async in Django Class-Based Views (CBV) — A to Z Guide

## 📌 What “async” means (in simple terms)

**Async = non-blocking execution**

* Your server can handle other requests while waiting for slow tasks (DB, API, file I/O).
* Improves scalability for I/O-heavy apps (chat apps, APIs, streaming, etc.)
* Not for CPU-heavy work (use Celery / background workers instead)

---

## 📌 Sync vs Async (Quick Comparison)

| Feature       | Sync (Normal Django) | Async                |
| ------------- | -------------------- | -------------------- |
| Blocking      | Yes                  | No                   |
| Concurrency   | Limited              | High                 |
| Best for      | Simple apps          | APIs, real-time apps |
| CPU tasks     | OK                   | Not ideal            |
| External APIs | Slower               | Much faster          |

---

## 📌 Requirements for Async CBV

✅ Django 3.1+ (Full support improves in 4.x / 5.x / 6.x)
✅ ASGI server (NOT WSGI)

Use:

```
uvicorn
daphne
hypercorn
```

Run example:

```
uvicorn project.asgi:application --reload
```

---

## 📌 How Async Works Internally

Traditional Django:

```
Request → View → Response
```

Async Django:

```
Request → Event Loop → Async View → Await Tasks → Response
```

Event loop manages thousands of concurrent tasks efficiently.

---

## 📌 Making a CBV Async

You can make handler methods async:

```
get()
post()
put()
delete()
dispatch()
```

---

## 📌 Basic Async CBV Example

```python
from django.views import View
from django.http import HttpResponse
import asyncio

class MyAsyncView(View):

    async def get(self, request):
        await asyncio.sleep(2)  # simulate slow task
        return HttpResponse("Async GET response")
```

---

## 📌 Async in Template Views

```python
from django.views.generic import TemplateView
import asyncio

class HomeView(TemplateView):
    template_name = "home.html"

    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return await super().get(request, *args, **kwargs)
```

⚠️ Must `await super().get()` because it’s async-compatible.

---

## 📌 Async in DetailView

```python
from django.views.generic import DetailView
from .models import Book
import asyncio

class BookDetailView(DetailView):
    model = Book

    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return await super().get(request, *args, **kwargs)
```

---

## 📌 Async Database Access ⚠️ VERY IMPORTANT

### ❌ Django ORM is mostly synchronous

Direct use inside async view can block event loop.

---

### ✅ Correct way — use `sync_to_async`

```
from asgiref.sync import sync_to_async
```

Example:

```python
from django.views import View
from django.http import HttpResponse
from asgiref.sync import sync_to_async
from .models import Book

class AsyncDBView(View):

    async def get(self, request):
        books = await sync_to_async(list)(Book.objects.all())
        return HttpResponse(f"Books: {len(books)}")
```

---

## 📌 Async External API Calls (BEST USE CASE)

Use async libraries:

* httpx (recommended)
* aiohttp

Example:

```python
import httpx
from django.views import View
from django.http import JsonResponse

class AsyncAPI(View):

    async def get(self, request):
        async with httpx.AsyncClient() as client:
            r = await client.get("https://api.github.com")
        return JsonResponse(r.json())
```

---

## 📌 Async POST Example

```python
class AsyncFormView(View):

    async def post(self, request):
        await asyncio.sleep(1)
        return HttpResponse("Form submitted async")
```

---

## 📌 Async dispatch()

You can make the entire view async:

```python
class AsyncDispatchView(View):

    async def dispatch(self, request, *args, **kwargs):
        return await super().dispatch(request, *args, **kwargs)
```

---

## 📌 Mixing Sync + Async Code

Sometimes you must call sync code inside async view:

### Use:

```
sync_to_async()
```

Opposite case (calling async from sync):

```
async_to_sync()
```

---

## 📌 Full Real-World Async CBV Example

```python
import httpx
from asgiref.sync import sync_to_async
from django.views import View
from django.http import JsonResponse
from .models import Book

class DashboardView(View):

    async def get(self, request):

        # Async API call
        async with httpx.AsyncClient() as client:
            api_data = await client.get("https://api.github.com")

        # DB call safely
        books = await sync_to_async(list)(Book.objects.all())

        return JsonResponse({
            "api_status": api_data.status_code,
            "books": len(books)
        })
```

---

## 📌 When Async Actually Helps

✅ External APIs
✅ Multiple network calls
✅ Chat apps
✅ Streaming
✅ Long polling
✅ WebSockets (via Django Channels)

---

## 📌 When Async Does NOT Help

❌ Heavy CPU work
❌ Pure database-only apps
❌ Small projects
❌ Simple CRUD sites

Use background workers instead:

* Celery
* RQ
* Huey

---

## 📌 Performance Tip — Parallel Tasks

Async allows concurrent execution:

```python
import asyncio

async def get(self, request):
    task1 = asyncio.create_task(some_call())
    task2 = asyncio.create_task(another_call())

    result1 = await task1
    result2 = await task2
```

---

## 📌 Async vs Threads vs Processes

| Feature     | Async     | Threads  | Processes |
| ----------- | --------- | -------- | --------- |
| Memory      | Low       | Medium   | High      |
| CPU tasks   | Bad       | OK       | Best      |
| I/O tasks   | Best      | Good     | Good      |
| Scalability | Excellent | Moderate | Moderate  |

---

## 📌 Common Mistakes

❌ Using sync ORM directly in async view
❌ Running async code on WSGI server
❌ Using time.sleep() instead of asyncio.sleep()
❌ Forgetting `await`
❌ Mixing blocking libraries

---

## 📌 Quick Cheat Sheet

✔ Use async def in CBV methods
✔ Use await for async calls
✔ Use sync_to_async for ORM
✔ Use ASGI server
✔ Best for I/O-bound tasks

---

## 📌 Interview-Level Definition

> Async CBVs allow Django views to handle requests using non-blocking I/O via Python’s asyncio, enabling high concurrency and efficient handling of external operations without blocking the server thread.

---

## 📌 Final Summary

Async CBV = Modern scalable Django views.

Best use cases:

⭐ API gateways
⭐ Microservices
⭐ Real-time features
⭐ High-traffic apps

Not required for:

👉 Basic websites
👉 Small CRUD apps

---

## ✅ End of A-to-Z Guide
