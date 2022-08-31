---
title: extended_database_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_database_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>extended_database_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.extended_database_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `retentionDays` | `integer` | Specifies the number of days to keep in the audit logs in the storage account. |
| `storageEndpoint` | `string` | Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required. |
| `auditActionsAndGroups` | `array` | Specifies the Actions-Groups and Actions to audit.
<br />
<br />The recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins:
<br />
<br />BATCH_COMPLETED_GROUP,
<br />SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,
<br />FAILED_DATABASE_AUTHENTICATION_GROUP.
<br />
<br />This above combination is also the set that is configured by default when enabling auditing from the Azure portal.
<br />
<br />The supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records):
<br />
<br />APPLICATION_ROLE_CHANGE_PASSWORD_GROUP
<br />BACKUP_RESTORE_GROUP
<br />DATABASE_LOGOUT_GROUP
<br />DATABASE_OBJECT_CHANGE_GROUP
<br />DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP
<br />DATABASE_OBJECT_PERMISSION_CHANGE_GROUP
<br />DATABASE_OPERATION_GROUP
<br />DATABASE_PERMISSION_CHANGE_GROUP
<br />DATABASE_PRINCIPAL_CHANGE_GROUP
<br />DATABASE_PRINCIPAL_IMPERSONATION_GROUP
<br />DATABASE_ROLE_MEMBER_CHANGE_GROUP
<br />FAILED_DATABASE_AUTHENTICATION_GROUP
<br />SCHEMA_OBJECT_ACCESS_GROUP
<br />SCHEMA_OBJECT_CHANGE_GROUP
<br />SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP
<br />SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP
<br />SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP
<br />USER_CHANGE_PASSWORD_GROUP
<br />BATCH_STARTED_GROUP
<br />BATCH_COMPLETED_GROUP
<br />DBCC_GROUP
<br />DATABASE_OWNERSHIP_CHANGE_GROUP
<br />DATABASE_CHANGE_GROUP
<br />LEDGER_OPERATION_GROUP
<br />
<br />These are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs.
<br />
<br />For more information, see [Database-Level Audit Action Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).
<br />
<br />For Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are:
<br />SELECT
<br />UPDATE
<br />INSERT
<br />DELETE
<br />EXECUTE
<br />RECEIVE
<br />REFERENCES
<br />
<br />The general form for defining an action to be audited is:
<br />`{action} ON {object} BY {principal}`
<br />
<br />Note that &lt;object&gt; in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms `DATABASE::{db_name}` and `SCHEMA::{schema_name}` are used, respectively.
<br />
<br />For example:
<br />SELECT on dbo.myTable by public
<br />SELECT on DATABASE::myDatabase by public
<br />SELECT on SCHEMA::mySchema by public
<br />
<br />For more information, see [Database-Level Audit Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions) |
| `storageAccountSubscriptionId` | `string` | Specifies the blob storage subscription Id. |
| `isManagedIdentityInUse` | `boolean` | Specifies whether Managed Identity is used to access blob storage |
| `isAzureMonitorTargetEnabled` | `boolean` | Specifies whether audit events are sent to Azure Monitor. 
<br />In order to send the events to Azure Monitor, specify 'State' as 'Enabled' and 'IsAzureMonitorTargetEnabled' as true.
<br />
<br />When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created.
<br />Note that for server level audit you should use the 'master' database as {databaseName}.
<br />
<br />Diagnostic Settings URI format:
<br />PUT `https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview`
<br />
<br />For more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)
<br />or [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)
<br /> |
| `isStorageSecondaryKeyInUse` | `boolean` | Specifies whether storageAccountAccessKey value is the storage's secondary key. |
| `queueDelayMs` | `integer` | Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed.
<br />The default minimum value is 1000 (1 second). The maximum is 2,147,483,647. |
| `state` | `string` | Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. |
| `storageAccountAccessKey` | `string` | Specifies the identifier key of the auditing storage account. 
<br />If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage.
<br />Prerequisites for using managed identity authentication:
<br />1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD).
<br />2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity.
<br />For more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355) |
| `predicateExpression` | `string` | Specifies condition of where clause when creating an audit. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExtendedDatabaseBlobAuditingPolicies_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists extended auditing settings of a database. |
| `ExtendedDatabaseBlobAuditingPolicies_CreateOrUpdate` | `INSERT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates an extended database's blob auditing policy. |
| `ExtendedDatabaseBlobAuditingPolicies_Get` | `EXEC` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets an extended database's blob auditing policy. |
