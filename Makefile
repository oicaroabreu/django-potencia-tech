default: 
	@echo "Comandos disponíveis"
	@echo "make build           			- Cria containers caso não os tenha"
	@echo "make bash           				- Entra no shell dentro do container"
	@echo "make migrate			  			- Cria e executa migrations"
	@echo "make createsuperuser				- Criar um usuario super"
	@echo "make start           			- Inicializa container, e executa serviço Django"
	@echo "make stop            			- Encerra execução dos containers BD e Django"
	@echo "make test            			- Executa testes unitários"
	@echo "make export_requirements 		- Exporta as dependencias do Poetry para um arquivo requirements.txt"

build:
ifeq ("$(wildcard .env)","") 
	cp .env-example .env
	@echo "New file .env created" 		
endif
	docker-compose -f docker-compose-dev.yaml --env-file=.env up -d --build

bash:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti potencia_tech_dev bash

migrate:
	docker exec -ti potencia_tech_dev python manage.py makemigrations --no-input
	docker exec -ti potencia_tech_dev python manage.py migrate

createsuperuser:
	docker exec -ti potencia_tech_dev python manage.py createsuperuser

start:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti potencia_tech_dev python manage.py runserver 0.0.0.0:8000

stop:
	docker-compose -f docker-compose-dev.yaml stop 

test:
	docker exec -ti potencia_tech_dev python manage.py test 

export_requirements:
	poetry export --output requirements.txt --without-hashes