Homework project so some best practices were omitted, including but not limited:
1. settings.py by environment
2. database setup
3. user authorization
4. no refactor apps like "black"
5. model setup without created_at, currency in the same table as Product
6. no pagination or any output limitations
7. no sanitisation of user input
8. price is an integer (Stripe uses same approach)
9. no index for name or code in Product
10. not a proper way of handling exceptions (short cutted approach)
11. product and products are on the same url /products with and without url query. Because REST is about approacthing verbs, not urls
12. DELETE and PUT are not concurrent safe


Schema url:
`http://127.0.0.1:8000/openapi`

Requirements:
```
poetry
docker-compose
postgresql
```

Install:
`make install`

Run:
`make run`
