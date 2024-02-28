import argparse
import sys
from googleapiclient.discovery import build
from google.oauth2 import service_account
from package.datadog_utils import get_muted_alerts
from package.opsgenie_utils import create_alert_payload


def main():
    parser = argparse.ArgumentParser(
        description="Process muted alerts from Datadog and update a Google Sheets document"
    )
    parser.add_argument(
        "--datadog-api-key", dest="datadog_api_key", help="Datadog API key"
    )
    parser.add_argument(
        "--datadog-app-key", dest="datadog_app_key", help="Datadog app key"
    )
    parser.add_argument(
        "--team-name", dest="team_name", help="Team name for Datadog alerts"
    )
    parser.add_argument(
        "--opsgenie-api-key", dest="opsgenie_api_key", help="Opsgenie API key"
    )
    parser.add_argument(
        "--gcp-sa", dest="gcp_sa", help="Path to Google Cloud service account JSON file"
    )
    parser.add_argument(
        "--spreadsheet-id", dest="spreadsheet_id", help="Google Sheets spreadsheet ID"
    )
    parser.add_argument(
        "--range-name", dest="range_name", help="Google Sheets range name"
    )
    args = parser.parse_args()

    # Check if required arguments are provided
    if not all(
        [
            args.datadog_api_key,
            args.datadog_app_key,
            args.team_name,
            args.opsgenie_api_key,
            args.gcp_sa,
            args.spreadsheet_id,
            args.range_name,
        ]
    ):
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Retrieve command-line arguments
    api_key = args.datadog_api_key
    app_key = args.datadog_app_key
    team_name = args.team_name
    opsgenie_api_key = args.opsgenie_api_key
    sa_path = args.gcp_sa
    spreadsheet_id = args.spreadsheet_id
    range_name = args.range_name

    # Retrieve muted alerts from Datadog
    muted_alerts = get_muted_alerts(api_key, app_key, team_name)

    # Initialize Google Sheets service
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = service_account.Credentials.from_service_account_file(
        sa_path, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    # Update Google Sheets with muted alerts
    values = [[muted_alerts]]
    body = {"values": values, "majorDimension": "ROWS"}
    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body,
    )
    result.execute()

    # Process muted alerts
    if not muted_alerts:
        print("There are no muted alerts in production")
        sys.exit(0)
    else:
        for notification, monitor_ids in muted_alerts.items():
            print(notification, monitor_ids)
            id = notification.replace("priority ", "")
            alert_payload = create_alert_payload(id, monitor_ids)
            try:
                # Code for Opsgenie API integration
                pass
            except Exception as e:
                print(f"Error occurred while creating alert for {id}: {e}")

    # Clear the spreadsheet
    clear_body = {}
    request = sheet.values().clear(
        spreadsheetId=spreadsheet_id, range=range_name, body=clear_body
    )
    request.execute()


if __name__ == "__main__":
    main()
