---
title: domain_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_event_subscriptions
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
<tr><td><b>Name</b></td><td><code>domain_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domain_event_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `labels` | `array` | List of user defined labels. |
| `eventDeliverySchema` | `string` | The event delivery schema for the event subscription. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `deadLetterWithResourceIdentity` | `object` | Information about the deadletter destination with resource identity. |
| `destination` | `object` | Information about the destination for an event subscription. |
| `deliveryWithResourceIdentity` | `object` | Information about the delivery for an event subscription with resource identity. |
| `retryPolicy` | `object` | Information about the retry policy for an event subscription. |
| `deadLetterDestination` | `object` | Information about the dead letter destination for an event subscription. To configure a deadletter destination, do not directly instantiate an object of this class. Instead, instantiate an object of a derived class. Currently, StorageBlobDeadLetterDestination is the only class that derives from this class. |
| `filter` | `object` | Filter for the Event Subscription. |
| `topic` | `string` | Name of the topic of the event subscription. |
| `expirationTimeUtc` | `string` | Expiration time of the event subscription. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `provisioningState` | `string` | Provisioning state of the event subscription. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DomainEventSubscriptions_List` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | List all event subscriptions that have been created for a specific topic. |
| `DomainEventSubscriptions_CreateOrUpdate` | `INSERT` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Asynchronously creates a new event subscription or updates an existing event subscription. |
| `DomainEventSubscriptions_Delete` | `DELETE` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Delete an existing event subscription for a domain. |
| `DomainEventSubscriptions_Get` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get properties of an event subscription of a domain. |
| `DomainEventSubscriptions_GetDeliveryAttributes` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get all delivery attributes for an event subscription for domain. |
| `DomainEventSubscriptions_GetFullUrl` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Get the full endpoint URL for an event subscription for domain. |
| `DomainEventSubscriptions_Update` | `EXEC` | `domainName, eventSubscriptionName, resourceGroupName, subscriptionId` | Update an existing event subscription for a topic. |
