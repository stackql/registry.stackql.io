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
| `displayName` | `string` | The display name of the reservation |
| `type` | `string` | The type of the reservation. |
| `skuDescription` | `string` | The sku description of the reservation |
| `appliedScopes` | `array` | The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope |
| `provisioningSubState` | `string` | The provisioning state of the reservation, e.g. Succeeded |
| `location` | `string` | The location of the reservation. |
| `reservedResourceType` | `string` | The reserved source type of the reservation, e.g. virtual machine. |
| `renewSource` | `string` | The renew source of the reservation |
| `appliedScopeType` | `string` | The applied scope type of the reservation. |
| `displayProvisioningState` | `string` | The provisioning state of the reservation for display, e.g. Succeeded |
| `provisioningState` | `string` | The provisioning state of the reservation, e.g. Succeeded |
| `effectiveDateTime` | `string` | The effective date time of the reservation |
| `quantity` | `number` | The number of the reservation. |
| `utilization` | `object` | Reservation utilization |
| `userFriendlyRenewState` | `string` | The renew state of the reservation for display, e.g. On |
| `expiryDate` | `string` | The expiry date of the reservation |
| `sku` | `object` | The property of reservation sku object. |
| `term` | `string` | The term of the reservation, e.g. P1Y |
| `renew` | `boolean` | The renew state of the reservation |
| `userFriendlyAppliedScopeType` | `string` | The applied scope type of the reservation for display, e.g. Shared |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Reservations_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the reservations for a billing account and the roll up counts of reservations group by provisioning states. |
| `Reservations_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state. |
