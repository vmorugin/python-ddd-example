```
=== Структура проекта ===
my_project/
├── application/
│   ├── orders.py
│   ├── customers.py
│   ├── __init__.py
├── domain/
│   ├── orders/
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── repositories.py
│   │   ├── interfaces.py
│   │   ├── __init__.py
│   ├── customers/
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── repositories.py
│   │   ├── interfaces.py
│   │   ├── __init__.py
├── infrastructure/
│   ├── repositories/
│   │   ├── orders_repository.py
│   │   ├── customers_repository.py
│   │   ├── __init__.py
│   ├── adapters/
│   │   ├── order_service_adapter.py
│   │   ├── customer_service_adapter.py
│   │   ├── __init__.py
├── main.py
```