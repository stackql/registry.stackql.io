---
title: lots
hide_title: false
hide_table_of_contents: false
keywords:
  - lots
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
<tr><td><b>Name</b></td><td><code>lots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.lots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `creditCurrency` | `string` | The currency of the lot. |
| `source` | `string` | The source of the lot. |
| `poNumber` | `string` | The po number of the invoice on which the lot was added. This property is not available for ConsumptionCommitment lots. |
| `closedBalance` | `object` | The amount plus currency . |
| `type` | `string` | Resource type. |
| `closedBalanceInBillingCurrency` | `object` | The amount with exchange rate. |
| `expirationDate` | `string` | The expiration date of a lot. |
| `startDate` | `string` | The date when the lot became effective. |
| `reseller` | `object` | The reseller properties. |
| `originalAmountInBillingCurrency` | `object` | The amount with exchange rate. |
| `originalAmount` | `object` | The amount plus currency . |
| `status` | `string` | The status of the lot. |
| `purchasedDate` | `string` | The date when the lot was added. |
| `eTag` | `string` | The eTag for the resource. |
| `billingCurrency` | `string` | The billing currency of the lot. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Lots_ListByBillingAccount` | `SELECT` | `billingAccountId` | Lists all Microsoft Azure consumption commitments for a billing account. The API is only supported for Microsoft Customer Agreements (MCA) and Direct Enterprise Agreement (EA)  billing accounts. |
| `Lots_ListByBillingProfile` | `SELECT` | `billingAccountId, billingProfileId` | Lists all Azure credits for a billing account or a billing profile. The API is only supported for Microsoft Customer Agreements (MCA) billing accounts. |
| `Lots_ListByCustomer` | `SELECT` | `billingAccountId, customerId` | Lists all Azure credits for a customer. The API is only supported for Microsoft Partner  Agreements (MPA) billing accounts. |