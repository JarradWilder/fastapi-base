from fastapi import FastAPI
import os
import sys
import importlib

# Add the app directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# Automatically import all routers from the 'routers' folder
def include_all_routers(app):
    routers_path = os.path.join(os.path.dirname(__file__), 'routers')
    for filename in os.listdir(routers_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"app.routers.{filename[:-3]}"  # Remove '.py' extension
            module = importlib.import_module(module_name)
            app.include_router(module.router)

# Include all routers
include_all_routers(app)

@app.get("/")
def read_root():
    return "FastAPI base project"