---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - billing
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
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the reservation. |
| `name` | `string` | The name of the reservation. |
| `effectiveDateTime` | `string` | The effective date time of the reservation |
| `location` | `string` | The location of the reservation. |
| `provisioningState` | `string` | The provisioning state of the reservation, e.g. Succeeded |
| `userFriendlyAppliedScopeType` | `string` | The applied scope type of the reservation for display, e.g. Shared |
| `utilization` | `object` | Reservation utilization |
| `renewSource` | `string` | The renew source of the reservation |
| `renew` | `boolean` | The renew state of the reservation |
| `expiryDate` | `string` | The expiry date of the reservation |
| `displayProvisioningState` | `string` | The provisioning state of the reservation for display, e.g. Succeeded |
| `provisioningSubState` | `string` | The provisioning state of the reservation, e.g. Succeeded |
| `type` | `string` | The type of the reservation. |
| `appliedScopes` | `array` | The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope |
| `quantity` | `number` | The number of the reservation. |
| `appliedScopeType` | `string` | The applied scope type of the reservation. |
| `userFriendlyRenewState` | `string` | The renew state of the reservation for display, e.g. On |
| `displayName` | `string` | The display name of the reservation |
| `reservedResourceType` | `string` | The reserved source type of the reservation, e.g. virtual machine. |
| `sku` | `object` | The property of reservation sku object. |
| `skuDescription` | `string` | The sku description of the reservation |
| `term` | `string` | The term of the reservation, e.g. P1Y |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Reservations_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the reservations for a billing account and the roll up counts of reservations group by provisioning states. |
| `Reservations_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state. |
