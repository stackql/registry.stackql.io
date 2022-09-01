---
title: partner_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topics
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
<tr><td><b>Name</b></td><td><code>partner_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `partnerRegistrationImmutableId` | `string` | The immutableId of the corresponding partner registration. |
| `source` | `string` | Source associated with this partner topic. This represents a unique partner resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `expirationTimeIfNotActivatedUtc` | `string` | Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,<br />the partner topic and corresponding event channel are deleted. |
| `partnerTopicFriendlyDescription` | `string` | Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.<br />This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer. |
| `identity` | `object` | The identity information for the resource. |
| `eventTypeInfo` | `object` | The event type information for Channels. |
| `location` | `string` | The geo-location where the resource lives |
| `provisioningState` | `string` | Provisioning state of the partner topic. |
| `tags` | `object` | Resource tags. |
| `messageForActivation` | `string` | Context or helpful message that can be used during the approval process by the subscriber. |
| `activationState` | `string` | Activation state of the partner topic. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerTopics_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner topics under a resource group. |
| `PartnerTopics_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner topics under an Azure subscription. |
| `PartnerTopics_CreateOrUpdate` | `INSERT` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner topic with the specified parameters. |
| `PartnerTopics_Delete` | `DELETE` | `partnerTopicName, resourceGroupName, subscriptionId` | Delete existing partner topic. |
| `PartnerTopics_Activate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Activate a newly created partner topic. |
| `PartnerTopics_Deactivate` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Deactivate specific partner topic. |
| `PartnerTopics_Get` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Get properties of a partner topic. |
| `PartnerTopics_Update` | `EXEC` | `partnerTopicName, resourceGroupName, subscriptionId` | Asynchronously updates a partner topic with the specified parameters. |
