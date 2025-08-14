from agents import FunctionTool, RunContextWrapper
from data_schemas.order_status_schema import OrderStatusSchema

fake_orders = {
    "1001": {"status": "Processing", "delivery": "2025-08-18"},
    "1002": {"status": "Delivered", "delivery": "2025-08-10"},
    "1003": {"status": "Shipped", "delivery": "2025-08-16"},
    "1004": {"status": "Cancelled", "delivery": None},
    "1005": {"status": "Processing", "delivery": "2025-08-20"},
    "1006": {"status": "Pending", "delivery": "2025-08-22"},
    "1007": {"status": "Delivered", "delivery": "2025-08-12"},
    "1008": {"status": "Returned", "delivery": "2025-08-14"},
    "1009": {"status": "Shipped", "delivery": "2025-08-19"},
    "1010": {"status": "On Hold", "delivery": None},
    "1011": {"status": "Processing", "delivery": "2025-08-21"},
    "1012": {"status": "Delivered", "delivery": "2025-08-09"},
    "1013": {"status": "Shipped", "delivery": "2025-08-17"},
    "1014": {"status": "Cancelled", "delivery": None},
    "1015": {"status": "Pending", "delivery": "2025-08-23"}
}

async def order_status_function(ctx: RunContextWrapper, arg: str):
    print(f"[TOOL CALLED] get_order_status")
    obj = OrderStatusSchema.model_validate_json(arg)
    order = fake_orders.get(obj.order_id)

    if not order:
        return f"Order {obj.order_id} not found."

    if order["delivery"]:
        return f"Order {obj.order_id} status: {order['status']}, Estimated Delivery: {order['delivery']}"
    else:
        return f"Order {obj.order_id} status: {order['status']}, No delivery date available."

async def enable_for_order_intent(ctx: RunContextWrapper, agent) -> bool:
    return True


order_status_tool = FunctionTool(
    name="get_order_status",
    description="Fetches the status and estimated delivery date of an order by its ID.",
    params_json_schema=OrderStatusSchema.model_json_schema(),
    on_invoke_tool=order_status_function,
    is_enabled=enable_for_order_intent
)