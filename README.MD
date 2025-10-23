# GitHub Repository Information Query Tool

## Project Overview

### Project Background

This project is a repository information query tool based on the GitHub API. Its core goal is to quickly retrieve key information of a specified GitHub repository through a concise interactive method. The project adopts standardized development technologies such as Git branch management, Docker containerization, and unit testing to ensure clear code structure, convenient deployment, and reliable functions, simulating the project development and delivery process in real work scenarios.

### Project Objectives

- Implement the basic function of querying core repository information through GitHub username and repository name
- Adopt a standardized Git branch management strategy to ensure orderly project iteration
- Achieve application containerization deployment with Docker to ensure consistency in multi-environment operation
- Write test cases to verify core functions and reduce the risk of online function failures

## Technology Stack

- &zwnj;**Programming Language**&zwnj;: Python 3.12
- &zwnj;**Core Dependencies**&zwnj;:
  - `requests`: Used for GitHub API calls to retrieve repository data
  - `python-dotenv`: Load local environment variables (`.env` file) to manage sensitive configurations
  - `pytest`: Write and execute unit tests to verify function correctness
- &zwnj;**Containerization Tool**&zwnj;: Docker
- &zwnj;**Version Control**&zwnj;: Git + GitHub
- &zwnj;**API Interface**&zwnj;: GitHub REST API v3

## Function Description

### Core Functions

Query the specified GitHub repository and format and output the following information:

- Repository Name
- Star Count
- Fork Count
- Last Update Time

# Environment Configuration and Usage Methods

## Local Run

### 1. Clone Repository
```bash
git clone git@github.com:Your Username/Your Repository Name.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```


### 3. Configure Environment Variables
```bash
GITHUB_TOKEN=Your Personal Access Token
```


### 4. Run
```bash
python repofinder.py   
# # Follow the prompts to enter the GitHub repository name to complete the query
```


## Docker Run

### 1. Build Docker Image
```bash
docker build -t repo-finder .
```


### 2. Run Container
```bash
docker run -v %cd%/.env:/app/.env repo-finder
```


## Run test

### 1. 安装依赖
```bash
pip install pytest request
```


### 2. Run
```bash
pytest test.py -v   # -v Show detailed test logs
```
