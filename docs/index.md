# Pyue
> Simple component-based Web UI generator in Python (inspired by Vue JS and Flutter)

## Usage

```python
from pyue import Pyue, BackendType, Page
from flask import Flask

# Describing page
p = Page(title="My Site")

# Creating Pyue app
app = Pyue(BackendType.Flask)

# Register page like that:
app.add_page(page=p, url="/")

f = Flask(__name__)
app.mount(f)

f.run()
```

## Goals
- Making MVP web apps creation easy in Python
- Component-based approach for building web UI without garbage from js frameworks

## :fontawesome-solid-list: Features
- Generating frontend from Python code that is fully integrated with backend (Flask, FastAPI)
- Very flexible (UI is processed in a separate router, simply includes onto your app)
- Quite extendable - you can easily implement your own components

