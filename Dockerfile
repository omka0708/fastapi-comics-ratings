FROM python:3.10.4
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .