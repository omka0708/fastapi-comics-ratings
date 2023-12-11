FROM python:3.10.4
WORKDIR app/
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .