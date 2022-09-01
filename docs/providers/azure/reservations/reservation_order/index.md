---
title: reservation_order
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_order
  - reservations
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
<tr><td><b>Name</b></td><td><code>reservation_order</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.reservations.reservation_order</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the reservation |
| `name` | `string` | Name of the reservation |
| `type` | `string` | Type of resource. "Microsoft.Capacity/reservations" |
| `displayName` | `string` | Friendly name for user to easily identified the reservation. |
| `etag` | `integer` |  |
| `provisioningState` | `string` | Represent the current state of the Reservation. |
| `billingPlan` | `string` | Represent the billing plans. |
| `createdDateTime` | `string` | This is the DateTime when the reservation was created. |
| `originalQuantity` | `integer` | Total Quantity of the SKUs purchased in the Reservation. |
| `benefitStartTime` | `string` | This is the DateTime when the reservation benefit started. |
| `expiryDate` | `string` | This is the date when the Reservation will expire. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `requestDateTime` | `string` | This is the DateTime when the reservation was initially requested for purchase. |
| `term` | `string` | Represent the term of Reservation. |
| `reservations` | `array` |  |
| `planInformation` | `object` | Information describing the type of billing plan for this reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationOrder_List` | `SELECT` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| `ReservationOrder_Calculate` | `EXEC` |  | Calculate price for placing a `ReservationOrder`. |
| `ReservationOrder_ChangeDirectory` | `EXEC` | `reservationOrderId` | Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id |
| `ReservationOrder_Get` | `EXEC` | `reservationOrderId` | Get the details of the `ReservationOrder`. |
| `ReservationOrder_Purchase` | `EXEC` | `reservationOrderId` | Purchase `ReservationOrder` and create resource under the specified URI. |
