---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - service_bus
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `action` | `object` | Represents the filter actions which are allowed for the transformation of a message that have been matched by a filter expression. |
| `sqlFilter` | `object` | Represents a filter which is a composition of an expression and an action that is executed in the pub/sub pipeline. |
| `location` | `string` | The geo-location where the resource lives |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `filterType` | `string` | Rule filter types |
| `correlationFilter` | `object` | Represents the correlation filter expression. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Rules_ListBySubscriptions` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | List all the rules within given topic-subscription |
| `Rules_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName` | Creates a new rule and updates an existing rule |
| `Rules_Delete` | `DELETE` | `namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName` | Deletes an existing rule. |
| `Rules_Get` | `EXEC` | `namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName` | Retrieves the description for the specified rule. |
