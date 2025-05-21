# Skill LMS: A Django-Based Learning Management System with Performance Optimizations

## Overview

Skill LMS is a robust Learning Management System built with Django, designed to provide a platform for managing and delivering online courses and lessons. This repository contains the source code for the Skill LMS, with a particular focus on implementing and demonstrating various front-end web performance optimization techniques to enhance user experience and key performance indicators.

## Features

* **Course Management:** Create, update, and manage courses with titles, descriptions, and images.

* **Module Organization:** Structure courses into logical modules for better content organization.

* **Lesson Delivery:** Deliver individual learning units within modules, supporting various content types:

    * **Text Content:** Rich textual lessons.

    * **Image Content:** Integrated images with captions.

    * **Video Content:** Embedded video content (e.g., YouTube links).

    * **File Content:** Downloadable supplementary files.

* **User Authentication:** (Assumed, standard Django user system)

* **Performance Optimized:** Implemented various front-end optimizations for faster loading and improved responsiveness.

## Performance Optimization Highlights

This project integrates several key front-end performance optimization techniques:

1.  **Server-Side Compression (GzipMiddleware):** HTML, CSS, and JavaScript responses are compressed before being sent to the browser, reducing network transfer size.

2.  **CSS Optimization:**

    * **Minification:** Removal of unnecessary characters (whitespace, comments) from CSS files.

    * **Concatenation/Bundling:** Multiple CSS files are combined into a single file to reduce HTTP requests.

3.  **JavaScript Optimization:**

    * **Minification:** Removal of unnecessary characters from JavaScript files.

    * **Concatenation/Bundling:** Multiple JavaScript files are combined into a single file.

    * **Deferred Loading (`defer`):** JavaScript execution is deferred until HTML parsing is complete, preventing render-blocking.

4.  **Image Optimization:**

    * **Compression & WebP Conversion:** Images (JPEG, PNG) are compressed and converted to the more efficient WebP format.

    * **Model Integration:** Optimized WebP image paths are stored directly in `Course` and `ImageContent` models, allowing templates to serve the most efficient format.

5.  **Browser Caching (WhiteNoise):** Configured to serve static files with long-lived `Cache-Control` headers and manifest-based cache busting, ensuring browsers aggressively cache static assets for faster repeat visits.

## Setup Instructions

Follow these steps to get the Skill LMS running on your local machine.

### Prerequisites

* Python 3.8+

* pip (Python package installer)

* Pillow (Python Imaging Library - automatically installed with `requirements.txt`)

### 1. Clone the Repository

`git clone https://github.com/Adebayolusipe/skill-lms.git`
`cd skill-lms`

### 2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

`python -m venv venv`

`source venv/bin/activate`

### 3. Install Dependencies
Install all required Python packages using pip:

`pip install -r requirements.txt`

### 4. Database Setup
Apply database migrations to create the necessary tables:

`python manage.py makemigrations`
`python manage.py migrate`

### 5. Create a Superuser (Admin Account)
Create an administrator account to access the Django admin panel:

`python manage.py createsuperuser`

Follow the prompts to set up  username, email, and password.

### 6. Media and Static Files Setup
Ensure your settings.py is configured correctly for static and media files:

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

### Running the Application
To start the Django development server:

`python manage.py runserver`

The application will be accessible at http://127.0.0.1:8000/.
You can access the Django admin panel at http://127.0.0.1:8000/admin/.

### Running Optimization Commands
These commands are crucial for applying the performance optimizations.

**1. Collect Static Files**
This command gathers all static files from your apps into STATIC_ROOT, which is necessary for WhiteNoise and django-compressor.

`python manage.py collectstatic`

**2. Compress Images**
This custom management command processes images in your static/ and media/ directories, compressing them and generating WebP versions, and updating your Course and ImageContent models to point to these optimized files.

Basic usage: Process all images, create _optimized.webp and _optimized.jpg/.png files

`python manage.py compress_images`

**Process only media files (Course and ImageContent models) and update model fields**
`python manage.py compress_images --media-only --reprocess-media-webp`

**3. Compress CSS and JavaScript (Django-Compressor)**
This command pre-compresses and minifies your CSS and JavaScript files as configured by django-compressor in your settings.py. This is essential for production deployment when COMPRESS_OFFLINE = True.

python manage.py compress

After running compress, the templates will automatically link to the compressed and bundled files.


