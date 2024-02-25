from unittest import result
import datadog
import opsgenie_sdk
import os
import sys
from time import sleep
from pprint import pprint
from opsgenie_sdk.rest import ApiException
from googleapiclient.discovery import build
from google.oauth2 import service_account

# get muted alert in datadog
def get_datadog_key(api_key, app_key):
    # initialize connection to datadog api
    datadog.initialize(api_key=api_key, app_key=app_key)
    # query to datadog api
    muted = datadog.api.Monitor.search(query="notification:opsgenie-xxx-xxx",per_page=1000,page=2)
    result = {}
    for monitor in muted['monitors']:
        name = monitor['name']
        for notification in monitor['name']:
            if not notification.startswith('priority'):
                continue
            elif notification not in result:
                result[notification] = []
            result[notification]
        print (name)
        return result

#prepare create payload for opsgenie
def create_alert_payload(id, monitor_ids):
    count = 0
    total = sum (count == 0 for value in monitor_ids)

    return opsgenie_sdk.CreateAlertPayload(
        message=f'[P3] [Datadog-Checker] Muted monitor in production is {total} alert(s)',
        description=f'Datadog alerting in production for {id} is muted. Please check your list muted monitor below and unmute it, or close this alert if this is expected : \n- https://app.datadoghq.com/monitors/manage?q=muted%3Atrue%20env%3Aproduction%20notification%3Aopsgenie-{id}',
        responders=[{
            'name': f'{id}',
            'type': 'team'
            }],
        visible_to=[
            {'name': f'{id}',
            'type': 'team'}],
        note='This alert generate by me',
        user='zackzonexx',
        priority='P3',
        source='Datadog Muted Alert Checker Tools',
    )

# Check if env variable declare or not
def get_env_value(key):
    value = os.environ.get(key, None)
    if not value:
        print(f'ERROR: environment {key} is needed')
        sys.exit(1)
    return value


def main():
    #define necessary variables here
    api_key = get_env_value('DATADOG_API_KEY')
    app_key = get_env_value('DATADOG_APP_KEY')
    sa_path = get_env_value('GCP_SA')
    opsgenie_api_key = get_env_value('OPSGENIE_API_KEY')
    opsgenie_configuration = opsgenie_sdk.Configuration()
    opsgenie_configuration.api_key['Authorization'] = opsgenie_api_key
    opsgenie_alert_api_instance = opsgenie_sdk.AlertApi(opsgenie_sdk.ApiClient(opsgenie_configuration))
    name = get_datadog_key(api_key, app_key)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = service_account.Credentials.from_service_account_file(sa_path,scopes=SCOPES)
    SPREADSHEET_ID = 'redacted'
    RANGE_NAME = 'redacted'
    service = build('sheets', 'v4', credentials= creds)
    sheet = service.spreadsheets()
    values = [
                [name]
            ]
    body = {
            'values': values,
            'majorDimension': 'ROWS'
             }
    result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,valueInputOption='RAW', body=body)
    result.execute()
    get_datadog_key(api_key, app_key)
    for monitor_name in name.__getitem__(result):
        print (monitor_name)
    Clear the spreadsheet
    bods = {}
    request = sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, body=bods)
    request.execute()

    ##condition
    if name == {}:
        print ("There is no muted Alert in production")
        sys.exit(0)
    else:
        for notification in name.items():
            print (notification)
            id = opsgenie_id.replace('opsgenie-','')
            alert_payload = create_alert_payload(id, monitor_ids)
            count = 0
            total = sum (count == 0 for value in monitor_ids)
            try:
                opsgenie_alert_api_instance.create_alert(alert_payload)
                print(f'Alert for {opsgenie_id} Created')
                values = [
                            [id, f'https://app.datadoghq.com/monitors/manage?q=muted%3Atrue%20env%3Aproduction%20notification%3Aopsgenie-{id}',total]
                         ]
                body = {
                        'values': values,
                        'majorDimension': 'ROWS'
                       }
                result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,valueInputOption='RAW', body=body)
                result.execute()
                sleep(1)
            except opsgenie_sdk.rest.ApiException as e:
                print(f'Got error while executing {opsgenie_id}, detail {e}')

if __name__ == '__main__':
    main()
