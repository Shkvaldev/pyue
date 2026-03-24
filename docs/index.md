# Pyue
> Simple component-based Web UI generator in Python (inspired by Vue JS and Flutter)

## Code example

```python
from pyue import Pyue, BackendType, Page
from pyue.components import Stack, H1, H4, P, UL, LI
from flask import Flask

# Component data
features = [
    "🎯 Easy to use components",
    "⚡ Tailwind included",
    "🚀 Zero runtime overhead",
    "🔌 Pluggable structure",
]

# Component definition
def Feature(text):
    return LI(
        extra_classes=["p-3", "m-1", "border", "border-black", "rounded-xl"],
        content=[text],
    )

# Page definition
p = Page(
    title="Hello Pyue!",
    content=[
        Stack(
            spacing=4,
            align="items-center",
            content=[
                H1(content=["Welcome!"], extra_classes=["mt-3"]),
                P(content=["This page was built with Python 🐍"]),
                H4(extra_classes=["mt-3", "mb-3"], content=["Why Pyue?"]),
                UL(
                    extra_classes=["mt-1"],
                    content=[Feature(feature) for feature in features],
                ),
            ],
        )
    ],
)

# Creating Pyue app
app = Pyue(BackendType.Flask)

# Registering page
app.add_page(page=p, url="/")

f = Flask(__name__)
app.mount(f)

f.run()
```

## Usage

Follow docs link: https://shkvaldev.github.io/pyue

## Goals

- Making MVP web apps creation easy in Python
- Component-based approach for building web UI without garbage from js frameworks

## Features

- Generating frontend from Python code that is fully integrated with backend (Flask, FastAPI)
- Very flexible (UI is processed in a separate router, simply includes onto your app)
- Quite extendable - you can easily implement your own components

## TODO

- `ResourceManager` for better resources handling
- `HTMX` or `Alpine.js` integration for interactivity
- Custom HTML/CSS/JS embeddings (now available via content string)
- `FastAPIBackend` for `FastAPI` support
- MORE COMPONENTS TO THE GOD OF COMPONENTS
- Experimental `Python-Js` translator
