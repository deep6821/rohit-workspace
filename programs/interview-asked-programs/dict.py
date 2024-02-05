data = [
    {
        "item": "apple",
        "qty": 2,
        "id": "order-1"
    },
    {
        "item": "orange",
        "qty": 3,
        "id": "order-2"
    },
    {
        "item": "apple",
        "qty": 4,
        "id": "order-1"
    }
]

from collections import Counter, defaultdict
cnt = defaultdict(int)
for r in data:
    cnt[(r['item'], r['id'])] += r['qty']

res = [{'item': k[0], 'qty': x, 'id': k[1]} for k, x in cnt.items()]
print(res)
