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
| `displayName` | `string` | Friendly name for user to easily identified the reservation. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `createdDateTime` | `string` | This is the DateTime when the reservation was created. |
| `etag` | `integer` |  |
| `originalQuantity` | `integer` | Total Quantity of the SKUs purchased in the Reservation. |
| `term` | `string` | Represent the term of Reservation. |
| `reservations` | `array` |  |
| `requestDateTime` | `string` | This is the DateTime when the reservation was initially requested for purchase. |
| `benefitStartTime` | `string` | This is the DateTime when the reservation benefit started. |
| `billingPlan` | `string` | Represent the billing plans. |
| `provisioningState` | `string` | Represent the current state of the Reservation. |
| `expiryDate` | `string` | This is the date when the Reservation will expire. |
| `type` | `string` | Type of resource. "Microsoft.Capacity/reservations" |
| `planInformation` | `object` | Information describing the type of billing plan for this reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationOrder_List` | `SELECT` |  | List of all the `ReservationOrder`s that the user has access to in the current tenant. |
| `ReservationOrder_Calculate` | `EXEC` |  | Calculate price for placing a `ReservationOrder`. |
| `ReservationOrder_ChangeDirectory` | `EXEC` | `reservationOrderId` | Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id |
| `ReservationOrder_Get` | `EXEC` | `reservationOrderId` | Get the details of the `ReservationOrder`. |
| `ReservationOrder_Purchase` | `EXEC` | `reservationOrderId` | Purchase `ReservationOrder` and create resource under the specified URI. |
