from fastapi import FastAPI

from app.api import products

app = FastAPI(title="Teklif Motoru")

app.include_router(products.router)


@app.get("/health")
def health():
    return {"status": "ok"}
