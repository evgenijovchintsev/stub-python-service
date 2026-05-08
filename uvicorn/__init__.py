import sys
import os

def run(*args, **kwargs):
    """Delegate to the real uvicorn.run, avoiding recursion from the local package."""
    cwd = os.getcwd()
    # Temporarily remove current working directory from sys.path to import external uvicorn
    removed = False
    if cwd in sys.path:
        sys.path.remove(cwd)
        removed = True
    try:
        from uvicorn import run as real_run
        return real_run(*args, **kwargs)
    finally:
        if removed:
            sys.path.insert(0, cwd)
