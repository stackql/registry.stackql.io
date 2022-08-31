---
title: reservation_transactions
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_transactions
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
<tr><td><b>Name</b></td><td><code>reservation_transactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservation_transactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `description` | `string` | The description of the transaction. |
| `invoice` | `string` | Invoice Number |
| `invoiceSectionId` | `string` | Invoice Section Id |
| `currency` | `string` | The ISO currency in which the transaction is charged, for example, USD. |
| `purchasingSubscriptionGuid` | `string` | The subscription guid that makes the transaction. |
| `billingProfileId` | `string` | Billing profile Id. |
| `billingFrequency` | `string` | The billing frequency, which can be either one-time or recurring. |
| `invoiceSectionName` | `string` | Invoice Section Name. |
| `reservationOrderId` | `string` | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. |
| `billingProfileName` | `string` | Billing profile name. |
| `invoiceId` | `string` | Invoice Id as on the invoice where the specific transaction appears. |
| `amount` | `number` | The charge of the transaction. |
| `armSkuName` | `string` | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. |
| `tags` | `array` | Resource tags. |
| `eventDate` | `string` | The date of the transaction |
| `reservationOrderName` | `string` | The name of the reservation order. |
| `region` | `string` | The region of the transaction. |
| `eventType` | `string` | The type of the transaction (Purchase, Cancel or Refund). |
| `quantity` | `number` | The quantity of the transaction. |
| `term` | `string` | This is the term of the transaction. |
| `purchasingSubscriptionName` | `string` | The subscription name that makes the transaction. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReservationTransactions_List` | `SELECT` | `billingAccountId` | List of transactions for reserved instances on billing account scope. Note: The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. |
| `ReservationTransactions_ListByBillingProfile` | `SELECT` | `billingAccountId, billingProfileId` | List of transactions for reserved instances on billing profile scope. The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. |
