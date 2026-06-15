FROM python:3.11-slim

WORKDIR /app

# 2. Logs directory pehle hi bana lein
RUN mkdir -p /app/logs

COPY app.py .

# 3. Pip dependencies install karein (Yahan chmod ki koi zaroorat nahi hai)
RUN pip install --no-cache-dir flask

#RUN useradd -u 1001 ares
#RUN chown -R ares:ares /app
#USER devender

EXPOSE 5000

CMD ["python", "app.py"]

