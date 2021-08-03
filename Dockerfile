FROM python:3
WORKDIR /Users/mac/Downloads/git/pythonLearning/pythonLearning/Docker
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src/dataProcessing/JSONProcessing.py ./
COPY sources/map.json ./sources/
CMD [ "python", "./JSONProcessing.py" ]

# COPY src/DockerUse.py ./app.py
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0" ]

#docker build -t my_webservice:latest .
#docker run my_webservice

#docker run -p 8000:8000 my_webservice