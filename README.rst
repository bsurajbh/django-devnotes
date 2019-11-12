## Devnotes

Devnotes is a simple Django app to store handy notes alongside your project.

----

**Installation**

    pip install django-devnotes
    or
    pip3 install django-devnotes
----
**Getting Started**

 1. Add "devnotes" to your INSTALLED_APPS setting like this:

		INSTALLED_APPS = [
						 'devnotes',
		]

 2. Add 'devnotes.middleware.DevnotesMiddleware' to your MIDDLEWARE like this:

	    MIDDLEWARE = [
	    	      'devnotes.middleware.DevnotesMiddleware',
	    ]

 3. Migrate the database schema into your database:

	    python manage.py makemigrations
	    python manage.py migrate

 4. Make sure your debug mode is True:

		 # in your project settings.py

		 DEBUG = True

 5. Include the app urls :

		 # in your project urls.py

    	 from django.conf import settings
    	 from django.urls import path,include

    	 #right below your project "urlpatterns":
    	 if settings.DEBUG:
		     import devnotes
		     urlpatterns = [
			     path('devnotes/', include('devnotes.urls')),
			 ] + urlpatterns

 7. Thats it :smile:
