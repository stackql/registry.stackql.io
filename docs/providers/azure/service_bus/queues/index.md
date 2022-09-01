---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.queues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `autoDeleteOnIdle` | `string` | ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes. |
| `createdAt` | `string` | The exact time the message was created. |
| `enablePartitioning` | `boolean` | A value that indicates whether the queue is to be partitioned across multiple message brokers. |
| `forwardDeadLetteredMessagesTo` | `string` | Queue/Topic name to forward the Dead Letter message |
| `requiresDuplicateDetection` | `boolean` | A value indicating if this queue requires duplicate detection. |
| `deadLetteringOnMessageExpiration` | `boolean` | A value that indicates whether this queue has dead letter support when a message expires. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `defaultMessageTimeToLive` | `string` | ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |
| `lockDuration` | `string` | ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `accessedAt` | `string` | Last time a message was sent, or the last time there was a receive request to this queue. |
| `updatedAt` | `string` | The exact time the message was updated. |
| `location` | `string` | The geo-location where the resource lives |
| `requiresSession` | `boolean` | A value that indicates whether the queue supports the concept of sessions. |
| `forwardTo` | `string` | Queue/Topic name to forward the messages |
| `status` | `string` | Entity status. |
| `maxDeliveryCount` | `integer` | The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10. |
| `enableExpress` | `boolean` | A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage. |
| `messageCount` | `integer` | The number of messages in the queue. |
| `maxSizeInMegabytes` | `integer` | The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024. |
| `enableBatchedOperations` | `boolean` | Value that indicates whether server-side batched operations are enabled. |
| `duplicateDetectionHistoryTimeWindow` | `string` | ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. |
| `countDetails` | `object` | Message Count Details. |
| `maxMessageSizeInKilobytes` | `integer` | Maximum size (in KB) of the message payload that can be accepted by the queue. This property is only used in Premium today and default is 1024. |
| `sizeInBytes` | `integer` | The size of the queue, in bytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Queues_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets the queues within a namespace. |
| `Queues_CreateOrUpdate` | `INSERT` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Creates or updates a Service Bus queue. This operation is idempotent. |
| `Queues_Delete` | `DELETE` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Deletes a queue from the specified namespace in a resource group. |
| `Queues_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId` | Creates an authorization rule for a queue. |
| `Queues_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId` | Deletes a queue authorization rule. |
| `Queues_Get` | `EXEC` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Returns a description for the specified queue. |
| `Queues_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId` | Gets an authorization rule for a queue by rule name. |
| `Queues_ListAuthorizationRules` | `EXEC` | `namespaceName, queueName, resourceGroupName, subscriptionId` | Gets all authorization rules for a queue. |
| `Queues_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId` | Primary and secondary connection strings to the queue. |
| `Queues_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, queueName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the queue. |
