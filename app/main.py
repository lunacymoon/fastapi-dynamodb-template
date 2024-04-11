from uuid import UUID

from fastapi import FastAPI
from starlette import status

from app.repositories import ProductRepository
from app.schemas import ProductSchemaIn, ProductSchemaOut

app = FastAPI()

@app.on_event('startup')
async def startup():
    from app.tables import ProductTable
    if not ProductTable.exists():
        ProductTable.create_table(
            read_capacity_units=1, write_capacity_units=1, wait=True
        )

@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductSchemaOut,
)
def create_product(product_in: ProductSchemaIn) -> ProductSchemaOut:
    product_out = ProductRepository.create(product_in)
    return product_out


@app.get(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductSchemaOut,
)
def create_product(product_id: UUID) -> ProductSchemaOut:
    product_out = ProductRepository.get(product_id)
    return product_out
