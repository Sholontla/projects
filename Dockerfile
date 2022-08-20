FROM python:3.9

# 
WORKDIR /.

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install  --upgrade -r ./requirements.txt

# 
COPY . .

# 
CMD ["main.py"]
ENTRYPOINT ["python"]