from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from trio import run

from modules import classes, heat_equation, num_math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware)

@app.post("/num_math/differentiation")
async def new_task(task_input: classes.DiffOptions):
    run(num_math.numDiff, *(task_input.task_id, task_input.f, task_input.a, task_input.order))
    return {"response": "OK"}

@app.post("/num_math/integration")
async def new_task(task_input: classes.IntOptions):
    run(num_math.numInt, *(task_input.task_id, task_input.f, task_input.a, task_input.b))
    return {"response": "OK"}

@app.post("/num_math/optimization")
async def new_task(task_input: classes.OptimOptions):
    run(num_math.twoDNumOpt, *(task_input.task_id, task_input.f, task_input.xl, task_input.xu, task_input.yl, task_input.yu))
    return {"response": "OK"}

@app.post("/num_math/lagrange_interpolation")
async def new_task(task_input: classes.LagrangeOptions):
    run(num_math.lagrangePoly, *(task_input.task_id, task_input.a, task_input.b))
    return {"response": "OK"}

@app.post("/num_math/taylor_approximation")
async def new_task(task_input: classes.TaylorOptions):
    run(num_math.approximateTaylorPoly, *(task_input.task_id, task_input.f, task_input.x0, task_input.order))
    return {"response": "OK"}

@app.post("/num_math/heat_equation")
async def new_task(task_input: classes.HeatOptions):
    run(heat_equation.calcAnimUp, *(task_input.task_id, task_input))
    return {"response": "OK"}
