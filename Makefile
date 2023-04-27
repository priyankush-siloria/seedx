build:
	@docker-compose -f docker-compose.yaml build --no-cache

run:build
	@docker-compose -f docker-compose.yaml --verbose up

test:
	@docker-compose -f docker-compose-test.yaml run --rm seed_x_api python manage.py test