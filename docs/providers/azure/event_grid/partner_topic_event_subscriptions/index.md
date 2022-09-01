---
title: partner_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topic_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>partner_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_topic_event_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `expirationTimeUtc` | `string` | Expiration time of the event subscription. |
| `retryPolicy` | `object` | Information about the retry policy for an event subscription. |
| `deliveryWithResourceIdentity` | `object` | Information about the delivery for an event subscription with resource identity. |
| `deadLetterWithResourceIdentity` | `object` | Information about the deadletter destination with resource identity. |
| `provisioningState` | `string` | Provisioning state of the event subscription. |
| `filter` | `object` | Filter for the Event Subscription. |
| `eventDeliverySchema` | `string` | The event delivery schema for the event subscription. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `destination` | `object` | Information about the destination for an event subscription. |
| `topic` | `string` | Name of the topic of the event subscription. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `labels` | `array` | List of user defined labels. |
| `deadLetterDestination` | `object` | Information about the dead letter destination for an event subscription. To configure a deadletter destination, do not directly instantiate an object of this class. Instead, instantiate an object of a derived class. Currently, StorageBlobDeadLetterDestination is the only class that derives from this class. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerTopicEventSubscriptions_ListByPartnerTopic` | `SELECT` | `partnerTopicName, resourceGroupName, subscriptionId` | List event subscriptions that belong to a specific partner topic. |
| `PartnerTopicEventSubscriptions_CreateOrUpdate` | `INSERT` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates or updates an event subscription of a partner topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| `PartnerTopicEventSubscriptions_Delete` | `DELETE` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Delete an existing event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_Get` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get properties of an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get all delivery attributes for an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_GetFullUrl` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Get the full endpoint URL for an event subscription of a partner topic. |
| `PartnerTopicEventSubscriptions_Update` | `EXEC` | `eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId` | Update an existing event subscription of a partner topic. |
