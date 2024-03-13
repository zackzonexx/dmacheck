import datadog


def get_muted_alerts(api_key, app_key, team_name):
    # Initialize connection to Datadog API
    datadog.initialize(api_key=api_key, app_key=app_key)

    # Query Datadog API to get muted alerts
    query = f"notification:opsgenie-{team_name}"
    muted_alerts = datadog.api.Monitor.search(query=query, per_page=1000, page=2)

    # Process the response and extract relevant information
    result = {}
    for monitor in muted_alerts["monitors"]:
        name = monitor["name"]
        for notification in monitor["name"]:
            if not notification.startswith("priority"):
                continue
            elif notification not in result:
                result[notification] = []
            result[notification]

    return result
