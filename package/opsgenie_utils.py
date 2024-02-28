import opsgenie_sdk


def create_alert_payload(id, monitor_ids):
    count = 0
    total = sum(count == 0 for value in monitor_ids)

    return opsgenie_sdk.CreateAlertPayload(
        message=f"[P3] [Datadog-Checker] Muted monitor in production is {total} alert(s)",
        description=f"Datadog alerting in production for {id} is muted. Please check your list muted monitor below and unmute it, or close this alert if this is expected : \n- https://app.datadoghq.com/monitors/manage?q=muted%3Atrue%20env%3Aproduction%20notification%3Aopsgenie-{id}",
        responders=[{"name": f"{id}", "type": "team"}],
        visible_to=[{"name": f"{id}", "type": "team"}],
        note="This alert generate by me",
        user="zackzonexx",
        priority="P3",
        source="Datadog Muted Alert Checker Tools",
    )
