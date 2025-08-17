
# Azure Monitor + Grafana Integration
from azure.monitor.query import LogsQueryClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

# Query Azure Monitor for empire metrics
def get_empire_metrics():
    query = '''
    AppInsights
    | where TimeGenerated > ago(1h)
    | summarize
        RequestCount = count(),
        AvgDuration = avg(DurationMs),
        SuccessRate = countif(Success == true) * 100.0 / count()
    by bin(TimeGenerated, 5m)
    '''

    response = client.query_workspace(
        workspace_id="YOUR_WORKSPACE_ID",
        query=query,
        timespan=timedelta(hours=1)
    )

    return response.tables[0].rows
            