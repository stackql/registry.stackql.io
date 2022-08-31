---
title: partner_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_registrations
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
<tr><td><b>Name</b></td><td><code>partner_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `partnerRegistrationImmutableId` | `string` | The immutableId of the corresponding partner registration.<br />Note: This property is marked for deprecation and is not supported in any future GA API version |
| `provisioningState` | `string` | Provisioning state of the partner registration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerRegistrations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner registrations under a resource group. |
| `PartnerRegistrations_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner registrations under an Azure subscription. |
| `PartnerRegistrations_CreateOrUpdate` | `INSERT` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Creates a new partner registration with the specified parameters. |
| `PartnerRegistrations_Delete` | `DELETE` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Deletes a partner registration with the specified parameters. |
| `PartnerRegistrations_Get` | `EXEC` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Gets a partner registration with the specified parameters. |
| `PartnerRegistrations_Update` | `EXEC` | `partnerRegistrationName, resourceGroupName, subscriptionId` | Updates a partner registration with the specified parameters. |
