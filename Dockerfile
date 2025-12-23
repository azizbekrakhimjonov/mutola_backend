# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
        libpng-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create staticfiles directory if it doesn't exist
RUN mkdir -p /app/staticfiles

# Set environment variables for collectstatic
ENV STATIC_ROOT=/app/staticfiles
ENV DEBUG=False

# Collect static files (static/ papkasidagi fayllarni staticfiles/ ga yig'adi)
RUN python manage.py collectstatic --noinput --clear || true

# Expose port
EXPOSE 7511

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7511", "--workers", "3", "project.wsgi:application"]

