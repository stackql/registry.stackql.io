---
title: schema_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_registry
  - event_hub
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
<tr><td><b>Name</b></td><td><code>schema_registry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.schema_registry</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SchemaRegistry_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the Schema Groups in a Namespace. |
| `SchemaRegistry_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, schemaGroupName, subscriptionId` |  |
| `SchemaRegistry_Delete` | `DELETE` | `namespaceName, resourceGroupName, schemaGroupName, subscriptionId` |  |
| `SchemaRegistry_Get` | `EXEC` | `namespaceName, resourceGroupName, schemaGroupName, subscriptionId` |  |