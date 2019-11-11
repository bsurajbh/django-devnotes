=====
Devnotes
=====

Devnotes is a simple Django app to store handy notes.

Quick start
-----------

1. Add "devnotes" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
      ...
      'devnotes',
    ]

                      ]
2.Add 'devnotes.middleware.DevnotesMiddleware' to your MIDDLEWARE like this:

    MIDDLEWARE=[
      ...
      'devnotes.middleware.DevnotesMiddleware',

    ]
