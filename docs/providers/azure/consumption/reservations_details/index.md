---
title: reservations_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_details
  - consumption
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
<tr><td><b>Name</b></td><td><code>reservations_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservations_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `usageDate` | `string` | The date on which consumption occurred. |
| `etag` | `string` | The etag for the resource. |
| `reservationOrderId` | `string` | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. |
| `instanceId` | `string` | This identifier is the name of the resource or the fully qualified Resource ID. |
| `tags` | `object` | Resource tags. |
| `reservedHours` | `number` | This is the total hours reserved for the day. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days. |
| `usedHours` | `number` | This is the total hours used by the instance. |
| `kind` | `string` | The reservation kind. |
| `instanceFlexibilityRatio` | `string` | The instance Flexibility Ratio. |
| `instanceFlexibilityGroup` | `string` | The instance Flexibility Group. |
| `type` | `string` | Resource type. |
| `skuName` | `string` | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. |
| `reservationId` | `string` | The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to. |
| `totalReservedQuantity` | `number` | This is the total count of instances that are reserved for the reservationId. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationsDetails_List` | `SELECT` | `resourceScope` | Lists the reservations details for the defined scope and provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| `ReservationsDetails_ListByReservationOrder` | `SELECT` | `$filter, reservationOrderId` | Lists the reservations details for provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
| `ReservationsDetails_ListByReservationOrderAndReservation` | `SELECT` | `$filter, reservationId, reservationOrderId` | Lists the reservations details for provided date range. Note: ARM has a payload size limit of 12MB, so currently callers get 502 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges. |
