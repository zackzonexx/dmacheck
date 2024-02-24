# Datadog Muted Alert Checker

To check muted alert for production in datadog and send alert to opsgenie if any


## How To Use this pipeline in your local host
* To use the script you should clone this pipeline
* Make sure you already have python 3 installed on your local host
* Create new spreadsheet for the report and get the id of the spreadsheet
* Put the id of spreadsheet into the script that have been marked "redacted" 
* Export OPSGENIE_API_KEY variable to your env and add opsgenie api key value in that variable like example below.
> Export OPSGENIE_API_KEY=`api key from opsgenie`<br>
> Export DATADOG_API_KEY=`api key from datadog`<br>
> Export DATADOG_APP_KEY=`app key from datadog`
* Install python dependencies requirements to your local host
> pip install -r requirements.txt
* Execute this main python script 
> python3 script/main.py
