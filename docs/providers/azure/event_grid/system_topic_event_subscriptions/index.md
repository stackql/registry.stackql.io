---
title: system_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - system_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>system_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.system_topic_event_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `retryPolicy` | `object` | Information about the retry policy for an event subscription. |
| `deadLetterDestination` | `object` | Information about the dead letter destination for an event subscription. To configure a deadletter destination, do not directly instantiate an object of this class. Instead, instantiate an object of a derived class. Currently, StorageBlobDeadLetterDestination is the only class that derives from this class. |
| `topic` | `string` | Name of the topic of the event subscription. |
| `provisioningState` | `string` | Provisioning state of the event subscription. |
| `deadLetterWithResourceIdentity` | `object` | Information about the deadletter destination with resource identity. |
| `destination` | `object` | Information about the destination for an event subscription. |
| `deliveryWithResourceIdentity` | `object` | Information about the delivery for an event subscription with resource identity. |
| `expirationTimeUtc` | `string` | Expiration time of the event subscription. |
| `filter` | `object` | Filter for the Event Subscription. |
| `eventDeliverySchema` | `string` | The event delivery schema for the event subscription. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `labels` | `array` | List of user defined labels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SystemTopicEventSubscriptions_ListBySystemTopic` | `SELECT` | `resourceGroupName, subscriptionId, systemTopicName` | List event subscriptions that belong to a specific system topic. |
| `SystemTopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Asynchronously creates or updates an event subscription with the specified parameters. Existing event subscriptions will be updated with this API. |
| `SystemTopicEventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Delete an existing event subscription of a system topic. |
| `SystemTopicEventSubscriptions_Get` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get an event subscription. |
| `SystemTopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get all delivery attributes for an event subscription. |
| `SystemTopicEventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Get the full endpoint URL for an event subscription of a system topic. |
| `SystemTopicEventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, resourceGroupName, subscriptionId, systemTopicName` | Update an existing event subscription of a system topic. |
