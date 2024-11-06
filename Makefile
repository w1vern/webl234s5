.PHONY: front back proxy redis "first migration"

front:
	npm run dev --prefix ./front

back:
	uvicorn back.main:app --reload

proxy:
	node ./proxy/main.js

redis:
	docker run --name redis_web -p 6379:6379 -d redis

postgres:
	docker run --name postgres_web -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres
	
gen_migration:
	alembic revision --autogenerete -m "first migration"

migration:
	alembic upgrade head

fill_data:
	python -m static.db_base_data
