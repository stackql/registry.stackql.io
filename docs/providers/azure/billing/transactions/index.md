---
title: transactions
hide_title: false
hide_table_of_contents: false
keywords:
  - transactions
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
<tr><td><b>Name</b></td><td><code>transactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.transactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `productTypeId` | `string` | The ID of the product type for which the transaction took place. |
| `azureCreditApplied` | `object` | The amount. |
| `unitOfMeasure` | `string` | The unit of measure used to bill for the product. For example, compute services are billed per hour. |
| `type` | `string` | Resource type. |
| `pricingCurrency` | `string` | The ISO 4217 code for the currency in which the product is priced. |
| `billingProfileDisplayName` | `string` | The name of the billing profile which will be billed for the transaction. |
| `kind` | `string` | The kind of transaction. Options are all or reservation. |
| `invoiceId` | `string` | The ID of the invoice on which the transaction was billed. This field is only applicable for transactions which are billed. |
| `subscriptionId` | `string` | The ID of the subscription that was used for the transaction. The field is only applicable for transaction of kind reservation. |
| `servicePeriodStartDate` | `string` | The date of the purchase of the product, or the start date of the month in which usage started. |
| `productType` | `string` | The type of the product for which the transaction took place. |
| `transactionAmount` | `object` | The amount. |
| `orderName` | `string` | The name of the reservation order. The field is only applicable for transactions of kind reservation. |
| `azurePlan` | `string` | The type of azure plan of the subscription that was used for the transaction. |
| `billingProfileId` | `string` | The ID of the billing profile which will be billed for the transaction. |
| `transactionType` | `string` | The type of transaction. |
| `effectivePrice` | `object` | The amount. |
| `customerId` | `string` | The ID of the customer for which the transaction took place. The field is applicable only for Microsoft Partner Agreement billing account. |
| `tax` | `object` | The amount. |
| `discount` | `number` | The percentage discount, if any, applied to this transaction. |
| `marketPrice` | `object` | The amount. |
| `customerDisplayName` | `string` | The name of the customer for which the transaction took place. The field is applicable only for Microsoft Partner Agreement billing account. |
| `invoice` | `string` | Invoice on which the transaction was billed or 'pending' if the transaction is not billed. |
| `servicePeriodEndDate` | `string` | The end date of the product term, or the end date of the month in which usage ended. |
| `productDescription` | `string` | The description of the product for which the transaction took place. |
| `subTotal` | `object` | The amount. |
| `productFamily` | `string` | The family of the product for which the transaction took place. |
| `date` | `string` | The date of transaction. |
| `unitType` | `string` | The description for the unit of measure for a given product. |
| `billingCurrency` | `string` | The ISO 4217 code for the currency in which this transaction is billed. |
| `orderId` | `string` | The order ID of the reservation. The field is only applicable for transaction of kind reservation. |
| `subscriptionName` | `string` | The name of the subscription that was used for the transaction. The field is only applicable for transaction of kind reservation. |
| `invoiceSectionId` | `string` | The ID of the invoice section which will be billed for the transaction. |
| `quantity` | `integer` | The quantity purchased in the transaction. |
| `exchangeRate` | `number` | The exchange rate used to convert charged amount to billing currency, if applicable. |
| `invoiceSectionDisplayName` | `string` | The name of the invoice section which will be billed for the transaction. |
| `units` | `number` | The number of units used for a given product. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Transactions_ListByInvoice` | `SELECT` | `billingAccountName, invoiceName` |
