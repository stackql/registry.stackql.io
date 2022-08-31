---
title: verified_partners
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_partners
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
<tr><td><b>Name</b></td><td><code>verified_partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.verified_partners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `partnerDisplayName` | `string` | Display name of the verified partner. |
| `partnerTopicDetails` | `object` | Information about the partner. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `organizationName` | `string` | Official name of the Partner. |
| `partnerRegistrationImmutableId` | `string` | ImmutableId of the corresponding partner registration. |
| `provisioningState` | `string` | Provisioning state of the verified partner. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VerifiedPartners_List` | `SELECT` |  | Get a list of all verified partners. |
| `VerifiedPartners_Get` | `EXEC` | `verifiedPartnerName` | Get properties of a verified partner. |
