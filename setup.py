from setuptools import setup


long_description = ""
# Get the long description from the README file
with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name="datadog-muted-alert-checker",
    version="1.0.1",
    license="MIT",
    long_description=long_description,
    url="https://github.com/zackzonexx/datadog-muted-alert-checker.git",
    author="Zackzonexx",
    author_email="zackzonexx@gmail.com",
    packages=["package"],
    keywords="Datadog Muted Alert Checker",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
    ],
    install_requires=[
        "datadog",
        "opsgenie-sdk",
        "requests",
        "urllib3",
        "google-auth",
        "google-auth-httplib2",
        "google-api-python-client",
        "pytest",
    ],
)
