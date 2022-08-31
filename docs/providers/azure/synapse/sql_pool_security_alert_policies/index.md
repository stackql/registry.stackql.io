---
title: sql_pool_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_security_alert_policies
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
<tr><td><b>Name</b></td><td><code>sql_pool_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `storageEndpoint` | `string` | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. |
| `creationTime` | `string` | Specifies the UTC creation time of the policy. |
| `disabledAlerts` | `array` | Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action |
| `emailAccountAdmins` | `boolean` | Specifies that the alert is sent to the account administrators. |
| `emailAddresses` | `array` | Specifies an array of e-mail addresses to which the alert is sent. |
| `retentionDays` | `integer` | Specifies the number of days to keep in the Threat Detection audit logs. |
| `state` | `string` | Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific Sql pool. |
| `storageAccountAccessKey` | `string` | Specifies the identifier key of the Threat Detection audit storage account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolSecurityAlertPolicies_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get a list of Sql pool's security alert policies. |
| `SqlPoolSecurityAlertPolicies_CreateOrUpdate` | `INSERT` | `resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName` | Create or update a Sql pool's security alert policy. |
| `SqlPoolSecurityAlertPolicies_Get` | `EXEC` | `resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName` | Get a Sql pool's security alert policy. |
