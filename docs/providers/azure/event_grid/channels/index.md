---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `expirationTimeIfNotActivatedUtc` | `string` | Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated,<br />the channel and corresponding partner topic are deleted. |
| `partnerTopicInfo` | `object` | Properties of the corresponding partner topic of a Channel. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `channelType` | `string` | The type of the event channel which represents the direction flow of events. |
| `readinessState` | `string` | The readiness state of the corresponding partner topic. |
| `provisioningState` | `string` | Provisioning state of the channel. |
| `messageForActivation` | `string` | Context or helpful message that can be used during the approval process by the subscriber. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Channels_ListByPartnerNamespace` | `SELECT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List all the channels in a partner namespace. |
| `Channels_CreateOrUpdate` | `INSERT` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously creates or updates a new channel with the specified parameters. |
| `Channels_Delete` | `DELETE` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Delete an existing channel. |
| `Channels_Get` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a channel. |
| `Channels_GetFullUrl` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Get the full endpoint URL of a partner destination channel. |
| `Channels_Update` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously updates a channel with the specified parameters. |
