Datadog Muted Alert Checker 
==============================

.. image:: https://img.shields.io/pypi/v/dmacheck

To check muted alert for production in datadog and send alert to opsgenie if any


How To Use this module in your local host
------------------------------------------

* To use the script you should clone this repository

* Make sure you already have python 3 installed on your local host

* Create new spreadsheet for the report and get the id of the spreadsheet

* Put the id of spreadsheet into the script that have been marked "redacted"

* Export OPSGENIE_API_KEY variable to your env and add opsgenie api key value in that variable like example below.


.. code-block:: bash

        Export OPSGENIE_API_KEY=`api key from opsgenie`
        Export DATADOG_API_KEY=`api key from datadog`
        Export DATADOG_APP_KEY=`app key from datadog`


* Install python dependencies requirements to your local host

.. code-block:: bash

        pip install -r requirements.txt


* Execute this main python script 

.. code-block:: bash

        python3 package/main.py

* If using this as a module just import this module in your code 

.. code-block:: python

        import dmacheck

