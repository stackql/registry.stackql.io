---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `requiresDuplicateDetection` | `boolean` | Value indicating if this topic requires duplicate detection. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
| `subscriptionCount` | `integer` | Number of subscriptions. |
| `status` | `string` | Entity status. |
| `maxSizeInMegabytes` | `integer` | Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024. |
| `autoDeleteOnIdle` | `string` | ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes. |
| `duplicateDetectionHistoryTimeWindow` | `string` | ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. |
| `supportOrdering` | `boolean` | Value that indicates whether the topic supports ordering. |
| `enableExpress` | `boolean` | Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage. |
| `createdAt` | `string` | Exact time the message was created. |
| `defaultMessageTimeToLive` | `string` | ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |
| `countDetails` | `object` | Message Count Details. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `enablePartitioning` | `boolean` | Value that indicates whether the topic to be partitioned across multiple message brokers is enabled. |
| `updatedAt` | `string` | The exact time the message was updated. |
| `enableBatchedOperations` | `boolean` | Value that indicates whether server-side batched operations are enabled. |
| `sizeInBytes` | `integer` | Size of the topic, in bytes. |
| `maxMessageSizeInKilobytes` | `integer` | Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024. |
| `accessedAt` | `string` | Last time the message was sent, or a request was received, for this topic. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Topics_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the topics in a namespace. |
| `Topics_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Creates a topic in the specified namespace. |
| `Topics_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Deletes a topic from the specified namespace and resource group. |
| `Topics_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName` | Creates an authorization rule for the specified topic. |
| `Topics_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName` | Deletes a topic authorization rule. |
| `Topics_Get` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Returns a description for the specified topic. |
| `Topics_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName` | Returns the specified authorization rule. |
| `Topics_ListAuthorizationRules` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, topicName` | Gets authorization rules for a topic. |
| `Topics_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName` | Gets the primary and secondary connection strings for the topic. |
| `Topics_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName, data__keyType` | Regenerates primary or secondary connection strings for the topic. |
