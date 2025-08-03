orders = [
    {"customer_id": 1, "order_id": 100, "status": "shipped"},
    {"customer_id": 2, "order_id": 101, "status": "pending"}
]

payments = [
    {"customer_id": 1, "order_id": 100, "paid_amount": 250},
    {"customer_id": 2, "order_id": 999, "paid_amount": 100}
]

hash_set = []
se = set()
for order in orders:
    for payment in payments:
        order_customer = order["customer_id"]
        payment_customer = payment["customer_id"]
        if order_customer==payment_customer:
            if order["order_id"] == payment["order_id"]:
                # merge the records together
                payment["status"] = order["status"]
                print(payment)
                key = (order["customer_id"],order["order_id"] )
                if key not in se:
                    se.add(key)
                    hash_set.append(payment)
                #del payment["status"]
            else:
                # otherwise simply append
                key = (payment["customer_id"],payment["order_id"] )
                if key not in se:
                    se.add(key)
                    hash_set.append(payment)
                    hash_set.append(order)

print(hash_set)


## optimized code
hash_set = {}
for order in orders:
    key = (order["customer_id"],order["order_id"])
    hash_set[key]= order.copy()
    
for payment in payments:
    key = (payment["customer_id"],payment["order_id"])
    if key in hash_set:
        hash_set[key].update(payment)
    else:
        hash_set[key] = payment.copy()
print(hash_set.values())