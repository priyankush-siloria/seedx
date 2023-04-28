build:
	@docker-compose -f docker-compose.yaml build

run:
	@docker-compose -f docker-compose.yaml up

test:
	@docker-compose -f docker-compose-test.yaml run --rm seed_x_api