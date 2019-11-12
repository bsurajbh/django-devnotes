import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-devnotes",
    version="0.2",
    author="Suraj Bhadange",
    author_email="",
    description="Devnotes is a simple Django app to store handy notes alongside your project",
    long_description='https://github.com/bsurajbh/django-devnotes/blob/master/README.md',
    long_description_content_type="text/markdown",
    url="https://github.com/bsurajbh/django-devnotes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
