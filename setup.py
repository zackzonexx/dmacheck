from setuptools import setup, find_packages


setup(
    name="dmacheck",
    version="1.0.5",
    license="MIT",
    url="https://github.com/zackzonexx/dmacheck",
    author="Zackzonexx",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author_email="zackzonexx@gmail.com",
    packages=find_packages(),
    keywords="dmacheck",
    classifiers=[
        "License :: OSI Approved :: MIT License",  # Specify your license type
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    install_requires=[
        "datadog",
        "opsgenie-sdk",
        "requests",
        "urllib3",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "dmacheck=dmacheck.main:main",
        ],
    },
)
