# Add 'octofit_tracker_app' to the INSTALLED_APPS list
INSTALLED_APPS += [
    'octofit_tracker_app',
    'rest_framework',
    'corsheaders',
    'octofit_tracker',
]

# Add CORS headers middleware
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Allow all origins for now (adjust as needed for production)
CORS_ALLOW_ALL_ORIGINS = True

# Configure database to use Djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}