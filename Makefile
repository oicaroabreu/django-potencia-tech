default: 
	@echo "Comandos disponíveis"
	@echo "make build           			- Cria containers caso não os tenha"
	@echo "make bash           				- Entra no shell dentro do container"
	@echo "make migrate			  			- Cria e executa migrations"
	@echo "make createsuperuser				- Criar um usuario super"
	@echo "make start           			- Inicializa container, e executa serviço Django"
	@echo "make stop            			- Encerra execução dos containers BD e Django"
	@echo "make test            			- Executa testes unitários"
	@echo "make lint						- Organiza o codigo"
	@echo "make black						- Black é um formatador de código Python que segue a PEP 8,"
	@echo "make isort						- Classifica automaticamente as importações em um arquivo de código Python"
	@echo "make flake8						- O Flake8 é um linter de código Python que verifica o estilo e a qualidade do código"
	@echo "make pre							- Pre analise do codigo antes do commit, Isort, Black Flake8 e um teste de coverage e gerar documento de requirements"
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
	docker exec -ti potencia_tech_dev python -m pytest . --cov-report term --cov=. --cov-fail-under=80

isort:
	@echo "############################### Running isort ###################################\n"
	docker exec -ti potencia_tech_dev isort .

black:
	@echo "\n################################# Running black #################################\n"
	docker exec -ti potencia_tech_dev black .

flake8:
	@echo "\n################################ Running flake8. ################################\n"
	docker exec -ti potencia_tech_dev flake8 .

lint:
	@echo "\n########## Runs isort, black and flake8. Organizing and linting code. ###########\n"
	make isort
	make black
	make flake8

export_requirements:
	poetry export --output requirements.txt --without-hashes

pre:
	make test
	make lint
	make export_requirements