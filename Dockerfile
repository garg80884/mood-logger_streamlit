
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
