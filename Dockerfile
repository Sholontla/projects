FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install  --upgrade -r /code/requirements.txt

# 
COPY . /code/app

# 
CMD ["/code/app/main.py"]
ENTRYPOINT ["python"]