---
title: managed_database_security_events
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_security_events
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
<tr><td><b>Name</b></td><td><code>managed_database_security_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_security_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `securityEventType` | `string` | The type of the security event. |
| `server` | `string` | The server name |
| `eventTime` | `string` | The time when the security event occurred. |
| `securityEventSqlInjectionAdditionalProperties` | `object` | The properties of a security event sql injection additional properties. |
| `subscription` | `string` | The subscription name |
| `database` | `string` | The database name |
| `clientIp` | `string` | The IP address of the client who executed the statement. |
| `applicationName` | `string` | The application used to execute the statement. |
| `principalName` | `string` | The principal user who executed the statement |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ManagedDatabaseSecurityEvents_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` |
