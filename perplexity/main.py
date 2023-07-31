from fastapi import FastAPI, Depends
from perplexity.routers import router
from perplexity.settings import get_settings

app = FastAPI(dependencies=[Depends(get_settings)])

# include routers
app.include_router(router)


def main():
    import uvicorn

    uvicorn.run("perplexity.main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
