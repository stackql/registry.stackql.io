---
title: server_dev_ops_audit_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dev_ops_audit_settings
  - sql
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
<tr><td><b>Name</b></td><td><code>server_dev_ops_audit_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_dev_ops_audit_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `isAzureMonitorTargetEnabled` | `boolean` | Specifies whether DevOps audit events are sent to Azure Monitor. 
<br />In order to send the events to Azure Monitor, specify 'State' as 'Enabled' and 'IsAzureMonitorTargetEnabled' as true.
<br />
<br />When using REST API to configure DevOps audit, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should be also created.
<br />
<br />Diagnostic Settings URI format:
<br />PUT https://management.azure.com/subscriptions/\{subscriptionId\}/resourceGroups/\{resourceGroup\}/providers/Microsoft.Sql/servers/\{serverName\}/databases/master/providers/microsoft.insights/diagnosticSettings/\{settingsName\}?api-version=2017-05-01-preview
<br />
<br />For more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)
<br />or [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)
<br /> |
| `state` | `string` | Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. |
| `storageAccountAccessKey` | `string` | Specifies the identifier key of the auditing storage account. 
<br />If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage.
<br />Prerequisites for using managed identity authentication:
<br />1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD).
<br />2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity.
<br />For more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355) |
| `storageAccountSubscriptionId` | `string` | Specifies the blob storage subscription Id. |
| `storageEndpoint` | `string` | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerDevOpsAuditSettings_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists DevOps audit settings of a server. |
| `ServerDevOpsAuditSettings_CreateOrUpdate` | `INSERT` | `devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId` | Creates or updates a server's DevOps audit settings. |
| `ServerDevOpsAuditSettings_Get` | `EXEC` | `devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId` | Gets a server's DevOps audit settings. |
