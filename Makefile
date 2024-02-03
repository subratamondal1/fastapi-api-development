install:
	# install pckages
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	# lint code
	pylint *.py

format:
	# format code
	black *.py

test:
	# test
	# python -m pytest --cov=mylib testfile.py

build:
	# build code with Github Actions for Continuous Integration
	# docker build -t fastapi-wiki .

run:
	# docker run
	# docker run -p 127.0.0.1:8080:8080 b19ef7dfd01b

deploy:
	# deploy using AWS ECR (Elastic Container Registry)

all:
	# combine all the needed steps in build in production

run-fastapi:
	# run fastapi app locally
	uvicorn main:app --reload
