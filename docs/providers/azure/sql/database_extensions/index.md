---
title: database_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_extensions
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
<tr><td><b>Name</b></td><td><code>database_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `databaseName` | `string` | Database name. |
| `errorMessage` | `string` | Error message. |
| `lastModifiedTime` | `string` | Last modified time. |
| `requestId` | `string` | Request Id. |
| `requestType` | `string` | Request type. |
| `serverName` | `string` | Server name. |
| `status` | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseExtensions_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | List database extension. This will return an empty list as it is not supported. |
| `DatabaseExtensions_CreateOrUpdate` | `INSERT` | `databaseName, extensionName, resourceGroupName, serverName, subscriptionId` | Perform a database extension operation, like polybase import |
| `DatabaseExtensions_Get` | `EXEC` | `databaseName, extensionName, resourceGroupName, serverName, subscriptionId` | Gets a database extension. This will return resource not found as it is not supported. |