from pyue import Pyue, BackendType
from flask import Flask

app = Pyue(BackendType.Flask, "static")
# Register page like that:
# app.add_page(page=put page instance here, url="/")

f = Flask(__name__)
app.mount(f)

f.run()
