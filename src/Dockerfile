# Use a lightweight Python image
FROM python:3.9-slim

WORKDIR /app

# Copy code
COPY app.py .

# Install Flask
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
