# Quotation

## CREATE A QUOTATION (/api/sales/quotation/)

Perform a POST request to /api/sales/quotation/. Provided below is a sample format for the request body:

```
{
    "type": "Project Based",
    "status": "Pending",
    "salesrep_id": 1,
    "customer_id": 2,
    "items": [
        {
            "product_id": 2,
            "quantity": 3,
            "unit_price": 45000
        },
        {
            "product_id": 3,
            "quantity": 1,
            "unit_price": 59900
        }
    ]
}
```
