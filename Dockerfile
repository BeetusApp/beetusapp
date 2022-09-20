FROM python:slim
LABEL org.opencontainers.image.source="https://github.com/BeetusApp/beetusapp"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "beetus.py"]