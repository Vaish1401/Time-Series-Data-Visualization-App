FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install grpcio grpcio-tools psycopg2-binary Flask

COPY timeseries.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. timeseries.proto

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

#Building and Running the Docker Container
docker build -t timeseries-backend .

#Run the Docker container:
docker run -p 5000:5000 timeseries-backend
