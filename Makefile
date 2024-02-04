install:
	# Install Required Packages
	pip install --upgrade pip && pip install -r requirements.txt

format:
	# Format code with Black
	black *.py blog/.

lint:
	# Lint code with PyLint
	pylint *.py blog/.
	
test:
	# Test code with PyTest
	# python -m pytest --cov=mylib testfile.py

build:
	# Build code with Github Actions for Continuous Integration
	# docker build -t fastapi-wiki .

run:
	# Docker Run
	# docker run -p 127.0.0.1:8080:8080 b19ef7dfd01b

deploy:
	# Deploy using AWS ECR (Elastic Container Registry)

all:
	# combine all the needed steps in build in production
	make format lint

run-fastapi:
	# run fastapi app locally
	uvicorn blog.main:app --reload
