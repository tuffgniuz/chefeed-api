FROM python:3.10.2-slim-buster

ENV PYTHONUNBUFFERED=1

# Create user
RUN useradd -ms /bin/bash chef

WORKDIR /src

COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

USER chef

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
