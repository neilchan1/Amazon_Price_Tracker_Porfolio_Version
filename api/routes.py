# PSEUDOCODE: API routes (Using FastAPI)
#
# Overview of Endpoints:
#
# POST /products
#   - body: {url: str, target_price: float}
#   - creates product (or updates target)
#   - Async to handle multiple requests
#
# GET /products
#   - Retrieve list of all tracked products
#   - Async to handle multiple requests
#
# GET /products/{id}
#   - Get product
#   - Async to handle multiple requests
#
# GET /products/{id}/history}
#   - Get price history of specified product
#   - Async to handle multiple requests
#
# POST /products/{id}/refresh
#   - Force immediate refresh (calls track_product) to fetch live price
#   - Async to handle multiple requests
#
