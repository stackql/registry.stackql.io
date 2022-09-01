---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inboundIpRules` | `array` | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled. |
| `endpoint` | `string` | Endpoint for the topic. |
| `metricResourceId` | `string` | Metric resource id for the topic. |
| `dataResidencyBoundary` | `string` | Data Residency Boundary of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `publicNetworkAccess` | `string` | This determines if traffic is allowed over public network. By default it is enabled. <br />You can further restrict to specific IPs by configuring &lt;seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" /&gt; |
| `inputSchemaMapping` | `object` | By default, Event Grid expects events to be in the Event Grid event schema. Specifying an input schema mapping enables publishing to Event Grid using a custom input schema. Currently, the only supported type of InputSchemaMapping is 'JsonInputSchemaMapping'. |
| `inputSchema` | `string` | This determines the format that Event Grid should expect for incoming events published to the topic. |
| `disableLocalAuth` | `boolean` | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the topic. |
| `identity` | `object` | The identity information for the resource. |
| `provisioningState` | `string` | Provisioning state of the topic. |
| `location` | `string` | The geo-location where the resource lives |
| `tags` | `object` | Resource tags. |
| `privateEndpointConnections` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Topics_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the topics under a resource group. |
| `Topics_ListBySubscription` | `SELECT` | `subscriptionId` | List all the topics under an Azure subscription. |
| `Topics_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, topicName` | Asynchronously creates a new topic with the specified parameters. |
| `Topics_Delete` | `DELETE` | `resourceGroupName, subscriptionId, topicName` | Delete existing topic. |
| `Topics_Get` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | Get properties of a topic. |
| `Topics_ListEventTypes` | `EXEC` | `providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId` | List event types for a topic. |
| `Topics_ListSharedAccessKeys` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | List the two keys used to publish to a topic. |
| `Topics_RegenerateKey` | `EXEC` | `resourceGroupName, subscriptionId, topicName, data__keyName` | Regenerate a shared access key for a topic. |
| `Topics_Update` | `EXEC` | `resourceGroupName, subscriptionId, topicName` | Asynchronously updates a topic with the specified parameters. |
