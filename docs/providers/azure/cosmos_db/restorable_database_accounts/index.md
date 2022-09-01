---
title: restorable_database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_database_accounts
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>restorable_database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.restorable_database_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `oldestRestorableTime` | `string` | The least recent time at which the database account can be restored to (ISO-8601 format). |
| `deletionTime` | `string` | The time at which the restorable database account has been deleted (ISO-8601 format). |
| `type` | `string` | The type of Azure resource. |
| `accountName` | `string` | The name of the global database account |
| `restorableLocations` | `array` | List of regions where the of the database account can be restored from. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
| `apiType` | `string` | Enum to indicate the API type of the restorable database account. |
| `creationTime` | `string` | The creation time of the restorable database account (ISO-8601 format). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorableDatabaseAccounts_List` | `SELECT` | `subscriptionId` | Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| `RestorableDatabaseAccounts_ListByLocation` | `SELECT` | `location, subscriptionId` | Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| `RestorableDatabaseAccounts_GetByLocation` | `EXEC` | `instanceId, location, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB restorable database account.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission. |
