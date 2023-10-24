# Projeto de Exemplo

Este é um projeto de exemplo de API em REST feito em Django para o desafio da Generation Brasil e Potencia Tech 

## Iniciando o Projeto

### Iniciando o Projeto Localmente

Para iniciar o projeto localmente, siga as instruções abaixo:

1. Clone este repositório em sua máquina local.

2. Certifique-se de que você possui um ambiente Python configurado e as dependências instaladas. Você pode instalar as dependências usando o gerenciador de pacotes `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Aplique as migrações ao banco de dados:

   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento do Django:

   ```bash
   python manage.py runserver
   ```

5. Agora, você pode acessar o projeto em [http://localhost:8000/](http://localhost:8000/).

### Iniciando o Projeto com Docker

Para iniciar o projeto com Docker, siga as instruções abaixo:

1. Clone este repositório em sua máquina local.
2. Certifique-se de que o Docker e o Docker Compose estejam instalados.
3. Execute o seguinte comando para construir o ambiente de desenvolvimento:

   ```bash
   make build
   ```

4. Após a conclusão da construção, inicie o servidor do Django com o seguinte comando:

   ```bash
   make start
   ```

5. Agora, você pode acessar o projeto em [http://localhost:8000/](http://localhost:8000/).

## Contribuindo

Sinta-se à vontade para contribuir com melhorias ou correções para este projeto. Basta abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
