from os import path
from pyue import Pyue, BackendType, Page
from flask import Flask

# Describing page
p = Page(title="My Site")

# Creating Pyue app
app = Pyue(BackendType.Flask, "static")

# Building page
p.to_file(path.join(app.static_path, p.filename))

# Register page like that:
app.add_page(page=p, url="/")

f = Flask(__name__)
app.mount(f)

f.run()
