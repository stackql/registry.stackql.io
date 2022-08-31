---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `endDate` | `string` | The date when the product will be renewed or canceled. |
| `skuId` | `string` | The sku ID of the product. |
| `tenantId` | `string` | The id of the tenant in which the product is used. |
| `productType` | `string` | The description of the type of product. |
| `autoRenew` | `string` | Indicates whether auto renewal is turned on or off for a product. |
| `productTypeId` | `string` | The ID of the type of product. |
| `invoiceSectionDisplayName` | `string` | The name of the invoice section to which the product is billed. |
| `lastChargeDate` | `string` | The date of the last charge. |
| `customerId` | `string` | The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account. |
| `reseller` | `object` | Details of the reseller. |
| `quantity` | `number` | The quantity purchased for the product. |
| `billingProfileId` | `string` | The ID of the billing profile to which the product is billed. |
| `availabilityId` | `string` | The availability of the product. |
| `invoiceSectionId` | `string` | The ID of the invoice section to which the product is billed. |
| `billingFrequency` | `string` | The frequency at which the product will be billed. |
| `purchaseDate` | `string` | The date when the product was purchased. |
| `status` | `string` | The current status of the product. |
| `billingProfileDisplayName` | `string` | The name of the billing profile to which the product is billed. |
| `skuDescription` | `string` | The sku description of the product. |
| `type` | `string` | Resource type. |
| `customerDisplayName` | `string` | The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account. |
| `lastCharge` | `object` | The amount. |
| `displayName` | `string` | The display name of the product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Products_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `Products_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `Products_ListByCustomer` | `SELECT` | `billingAccountName, customerName` | Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `Products_ListByInvoiceSection` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the products for an invoice section. These don't include products billed based on usage. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_Get` | `EXEC` | `billingAccountName, productName` | Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_Move` | `EXEC` | `billingAccountName, productName` | Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_Update` | `EXEC` | `billingAccountName, productName` | Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_ValidateMove` | `EXEC` | `billingAccountName, productName` | Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
