import argparse
import sys
import opsgenie_sdk
from dmacheck.datadog_utils import get_muted_alerts
from dmacheck.opsgenie_utils import create_alert_payload


# Check if argument is declared or not
def get_arg_value(arg_value, arg_name):
    if arg_value:
        return arg_value
    print(f'ERROR: argument "{arg_name}" is needed')
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Process muted alerts from Datadog and create alerts in Opsgenie"
    )
    parser.add_argument(
        "--datadog-api-key", dest="datadog_api_key", help="Datadog API key"
    )
    parser.add_argument(
        "--datadog-app-key", dest="datadog_app_key", help="Datadog app key"
    )
    parser.add_argument(
        "--team-name", dest="team_name", help="Team name for Datadog alert"
    )
    parser.add_argument(
        "--opsgenie-api-key", dest="opsgenie_api_key", help="Opsgenie API key"
    )
    args = parser.parse_args()

    # Retrieve command-line arguments
    api_key = get_arg_value(args.datadog_api_key, "--datadog-api-key")
    app_key = get_arg_value(args.datadog_app_key, "--datadog-app-key")
    team_name = get_arg_value(args.team_name, "--team-name")
    opsgenie_api_key = get_arg_value(args.opsgenie_api_key, "--opsgenie-api-key")

    # Retrieve muted alerts from Datadog
    muted_alerts = get_muted_alerts(api_key, app_key, team_name)

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
                # Create an Opsgenie API client
                config = opsgenie_sdk.configuration.Configuration()
                config.api_key["Authorization"] = opsgenie_api_key
                client = opsgenie_sdk.AlertApi(opsgenie_sdk.ApiClient(config))

                # Create an alert using Opsgenie SDK
                response = client.create_alert(alert_payload)
                print("Alert created successfully:", response)
            except opsgenie_sdk.ApiException as e:
                print(f"Error occurred while creating alert for {id}: {e}")


if __name__ == "__main__":
    main()
