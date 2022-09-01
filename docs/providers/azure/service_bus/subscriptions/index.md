---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `defaultMessageTimeToLive` | `string` | ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |
| `location` | `string` | The geo-location where the resource lives |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `autoDeleteOnIdle` | `string` | ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes. |
| `forwardTo` | `string` | Queue/Topic name to forward the messages |
| `requiresSession` | `boolean` | Value indicating if a subscription supports the concept of sessions. |
| `countDetails` | `object` | Message Count Details. |
| `status` | `string` | Entity status. |
| `updatedAt` | `string` | The exact time the message was updated. |
| `createdAt` | `string` | Exact time the message was created. |
| `messageCount` | `integer` | Number of messages. |
| `clientAffineProperties` | `object` | Properties specific to client affine subscriptions. |
| `duplicateDetectionHistoryTimeWindow` | `string` | ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. |
| `enableBatchedOperations` | `boolean` | Value that indicates whether server-side batched operations are enabled. |
| `isClientAffine` | `boolean` | Value that indicates whether the subscription has an affinity to the client id. |
| `forwardDeadLetteredMessagesTo` | `string` | Queue/Topic name to forward the Dead Letter message |
| `lockDuration` | `string` | ISO 8061 lock duration timespan for the subscription. The default value is 1 minute. |
| `accessedAt` | `string` | Last time there was a receive request to this subscription. |
| `maxDeliveryCount` | `integer` | Number of maximum deliveries. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `deadLetteringOnFilterEvaluationExceptions` | `boolean` | Value that indicates whether a subscription has dead letter support on filter evaluation exceptions. |
| `deadLetteringOnMessageExpiration` | `boolean` | Value that indicates whether a subscription has dead letter support when a message expires. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscriptions_ListByTopic` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | List all the subscriptions under a specified topic. |
| `Subscriptions_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Creates a topic subscription. |
| `Subscriptions_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Deletes a subscription from the specified topic. |
| `Subscriptions_Get` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName` | Returns a subscription description for the specified topic. |
