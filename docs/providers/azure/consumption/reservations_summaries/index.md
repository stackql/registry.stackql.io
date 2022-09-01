---
title: reservations_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_summaries
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
<tr><td><b>Name</b></td><td><code>reservations_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservations_summaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `purchasedQuantity` | `number` | This is the purchased quantity for the reservationId. |
| `kind` | `string` | The reservation kind. |
| `skuName` | `string` | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. |
| `etag` | `string` | The etag for the resource. |
| `usedHours` | `number` | Total used hours by the reservation |
| `remainingQuantity` | `number` | This is the remaining quantity for the reservationId. |
| `usageDate` | `string` | Data corresponding to the utilization record. If the grain of data is monthly, it will be first day of month. |
| `avgUtilizationPercentage` | `number` | This is average utilization for the entire time range. (day or month depending on the grain) |
| `utilizedPercentage` | `number` | This is the utilized percentage for the reservation Id. |
| `minUtilizationPercentage` | `number` | This is the minimum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 10%, this field will return 10% for that day |
| `reservedHours` | `number` | This is the total hours reserved. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days |
| `type` | `string` | Resource type. |
| `tags` | `object` | Resource tags. |
| `totalReservedQuantity` | `number` | This is the total count of instances that are reserved for the reservationId. |
| `reservationId` | `string` | The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to. |
| `reservationOrderId` | `string` | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. |
| `usedQuantity` | `number` | This is the used quantity for the reservationId. |
| `maxUtilizationPercentage` | `number` | This is the maximum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 100%, this field will return 100% for that day. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationsSummaries_List` | `SELECT` | `grain, resourceScope` | Lists the reservations summaries for the defined scope daily or monthly grain. |
| `ReservationsSummaries_ListByReservationOrder` | `SELECT` | `grain, reservationOrderId` | Lists the reservations summaries for daily or monthly grain. |
| `ReservationsSummaries_ListByReservationOrderAndReservation` | `SELECT` | `grain, reservationId, reservationOrderId` | Lists the reservations summaries for daily or monthly grain. |
