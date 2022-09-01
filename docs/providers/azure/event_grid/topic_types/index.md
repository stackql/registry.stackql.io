---
title: topic_types
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_types
  - event_grid
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
<tr><td><b>Name</b></td><td><code>topic_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.topic_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `description` | `string` | Description of the topic type. |
| `supportedLocations` | `array` | List of locations supported by this topic type. |
| `sourceResourceFormat` | `string` | Source resource format. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `provisioningState` | `string` | Provisioning state of the topic type |
| `displayName` | `string` | Display Name for the topic type. |
| `resourceRegionType` | `string` | Region type of the resource. |
| `provider` | `string` | Namespace of the provider of the topic type. |
| `supportedScopesForSource` | `array` | Supported source scopes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TopicTypes_List` | `SELECT` |  | List all registered topic types. |
| `TopicTypes_Get` | `EXEC` | `topicTypeName` | Get information about a topic type. |
| `TopicTypes_ListEventTypes` | `EXEC` | `topicTypeName` | List event types for a topic type. |
