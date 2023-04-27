build:
	@docker-compose -f docker-compose.yaml build --no-cache

run:
	@docker-compose -f docker-compose.yaml --verbose up

