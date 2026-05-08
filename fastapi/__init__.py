from starlette.applications import Starlette as _Starlette

class FastAPI(_Starlette):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
