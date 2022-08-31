---
title: restorable_gremlin_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_gremlin_databases
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
<tr><td><b>Name</b></td><td><code>restorable_gremlin_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.restorable_gremlin_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource Identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `type` | `string` | The type of Azure resource. |
| `resource` | `object` | The resource of an Azure Cosmos DB Gremlin database event |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RestorableGremlinDatabases_List` | `SELECT` | `instanceId, location, subscriptionId` |