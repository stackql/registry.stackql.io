---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `description` | `string` | The description of the event. |
| `billingProfileId` | `string` | The ID that uniquely identifies the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement.  |
| `adjustmentsInBillingCurrency` | `object` | The amount with exchange rate. |
| `creditExpired` | `object` | The amount plus currency . |
| `adjustments` | `object` | The amount plus currency . |
| `lotId` | `string` | The ID that uniquely identifies the lot for which the event happened. |
| `billingCurrency` | `string` | The billing currency of the event. |
| `canceledCredit` | `object` | The amount plus currency . |
| `eTag` | `string` | The eTag for the resource. |
| `reseller` | `object` | The reseller properties. |
| `transactionDate` | `string` | The date of the event. |
| `type` | `string` | Resource type. |
| `newCreditInBillingCurrency` | `object` | The amount with exchange rate. |
| `charges` | `object` | The amount plus currency . |
| `newCredit` | `object` | The amount plus currency . |
| `invoiceNumber` | `string` | The number which uniquely identifies the invoice on which the event was billed. This will be empty for unbilled events. |
| `closedBalance` | `object` | The amount plus currency . |
| `chargesInBillingCurrency` | `object` | The amount with exchange rate. |
| `billingProfileDisplayName` | `string` | The display name of the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement. |
| `lotSource` | `string` | Identifies the source of the lot for which the event happened.  |
| `creditCurrency` | `string` | The credit currency of the event. |
| `closedBalanceInBillingCurrency` | `object` | The amount with exchange rate. |
| `eventType` | `string` | Identifies the type of the event. |
| `creditExpiredInBillingCurrency` | `object` | The amount with exchange rate. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Events_ListByBillingAccount` | `SELECT` | `billingAccountId` |
| `Events_ListByBillingProfile` | `SELECT` | `billingAccountId, billingProfileId, endDate, startDate` |