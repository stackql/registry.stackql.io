---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `description` | `string` | Description of the query. |
| `timeModified` | `string` | Last modified date of the Log Analytics Query, in ISO 8601 format. |
| `displayName` | `string` | Unique display name for your query within the Query Pack. |
| `related` | `object` | The related metadata items for the function. |
| `author` | `string` | Object Id of user creating the query. |
| `tags` | `object` | Tags associated with the query. |
| `timeCreated` | `string` | Creation Date for the Log Analytics Query, in ISO 8601 format. |
| `properties` | `object` | Additional properties that can be set for the query. |
| `systemData` | `object` | Read only system data |
| `type` | `string` | Azure resource type |
| `body` | `string` | Body of the query. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Queries_List` | `SELECT` | `queryPackName, resourceGroupName, subscriptionId` | Gets a list of Queries defined within a Log Analytics QueryPack. |
| `Queries_Delete` | `DELETE` | `id, queryPackName, resourceGroupName, subscriptionId` | Deletes a specific Query defined within an Log Analytics QueryPack. |
| `Queries_Get` | `EXEC` | `id, queryPackName, resourceGroupName, subscriptionId` | Gets a specific Log Analytics Query defined within a Log Analytics QueryPack. |
| `Queries_Put` | `EXEC` | `id, queryPackName, resourceGroupName, subscriptionId` | Adds or Updates a specific Query within a Log Analytics QueryPack. |
| `Queries_Search` | `EXEC` | `queryPackName, resourceGroupName, subscriptionId` | Search a list of Queries defined within a Log Analytics QueryPack according to given search properties. |
| `Queries_Update` | `EXEC` | `id, queryPackName, resourceGroupName, subscriptionId` | Adds or Updates a specific Query within a Log Analytics QueryPack. |
