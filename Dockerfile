# Python کا official lightweight image استعمال کریں
FROM python:3.10-slim

# Working directory set کریں
WORKDIR /app

# Requirements کو کاپی کریں اور install کریں
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# باقی سارا code کاپی کریں
COPY . .

# Container start ہوتے ہی bot.py چل جائے گا
CMD ["python", "bot.py"]
