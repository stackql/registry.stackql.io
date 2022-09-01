---
title: workspace_managed_sql_server_security_alert_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_security_alert_policy
  - synapse
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_security_alert_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_security_alert_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific server |
| `storageAccountAccessKey` | `string` | Specifies the identifier key of the Threat Detection audit storage account. |
| `storageEndpoint` | `string` | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. |
| `creationTime` | `string` | Specifies the UTC creation time of the policy. |
| `disabledAlerts` | `array` | Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action |
| `emailAccountAdmins` | `boolean` | Specifies that the alert is sent to the account administrators. |
| `emailAddresses` | `array` | Specifies an array of e-mail addresses to which the alert is sent. |
| `retentionDays` | `integer` | Specifies the number of days to keep in the Threat Detection audit logs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceManagedSqlServerSecurityAlertPolicy_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get workspace managed sql server's threat detection policies. |
| `WorkspaceManagedSqlServerSecurityAlertPolicy_CreateOrUpdate` | `INSERT` | `resourceGroupName, securityAlertPolicyName, subscriptionId, workspaceName` | Create or Update a workspace managed sql server's threat detection policy. |
| `WorkspaceManagedSqlServerSecurityAlertPolicy_Get` | `EXEC` | `resourceGroupName, securityAlertPolicyName, subscriptionId, workspaceName` | Get a workspace managed sql server's security alert policy. |
