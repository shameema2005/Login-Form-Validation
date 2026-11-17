FROM python:3.12-slim
WORKDIR /tests
COPY tests/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY tests/test_login.py .
CMD ["python", "-m", "unittest", "-v", "test_login.py"]
