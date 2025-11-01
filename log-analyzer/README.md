# 🧾 Py-AutoLab: Log Analyzer

A small Python tool that parses web server logs and generates a summary of useful metrics: total requests, top endpoints, error rates, and average response times.

---

## ⚙️ Features
- Counts **total requests**
- Lists **top endpoints** (sorted by request count)
- Calculates **error rate** (`4xx` / `5xx`)
- Computes **average response times**
- Skips **malformed lines** automatically

---

## 🧩 Input Example (`access.log`)
```
2025-11-01 14:02:10 GET /api/users 200 123ms
2025-11-01 14:02:11 POST /api/login 401 45ms
2025-11-01 14:02:12 GET /api/users 200 150ms
2025-11-01 14:02:13 GET /api/posts 500 220ms
2025-11-01 14:02:15 GET /api/users 200 130ms
2025-11-01 14:02:17 GET /api/posts 200 180ms
```

## 🖥️ Output Example
```
----------------------------------------
Total requests: 6

Top endpoints:
  /api/users -> 3 hits
  /api/posts -> 2 hits
  /api/login -> 1 hits

Error rate: 33.33%

Average response times:
  /api/users -> 134.3ms
  /api/login -> 45.0ms
  /api/posts -> 200.0ms
----------------------------------------
```
