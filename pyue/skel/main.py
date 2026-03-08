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
