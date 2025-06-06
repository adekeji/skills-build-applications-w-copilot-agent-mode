# Add localhost and 127.0.0.1 to allowed hosts
ALLOWED_HOSTS = ['*']

# Add codespace URL to allowed hosts
ALLOWED_HOSTS.append('[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev')

# Ensure INSTALLED_APPS is initialized
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Add additional apps
INSTALLED_APPS += [
    'rest_framework',
    'djongo',
    'corsheaders',
    'octofit_tracker',
]

# Add the octofit_tracker_app to the installed apps
INSTALLED_APPS.append('octofit_tracker_app')

# Ensure MIDDLEWARE is initialized
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Add CORS middleware
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Update database settings for MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Allow all origins for CORS
CORS_ALLOW_ALL_ORIGINS = True

# Ensure TEMPLATES is initialized
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]