---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
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
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.customers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `resellers` | `array` | The list of resellers for which an Azure plan is enabled for the customer. |
| `type` | `string` | Resource type. |
| `billingProfileDisplayName` | `string` | The name of the billing profile for the invoice section. |
| `billingProfileId` | `string` | The ID of the billing profile for the invoice section. |
| `displayName` | `string` | The name of the customer. |
| `enabledAzurePlans` | `array` | Azure plans enabled for the customer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Customers_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the customers that are billed to a billing account. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `Customers_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the customers that are billed to a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `Customers_Get` | `EXEC` | `billingAccountName, customerName` | Gets a customer by its ID. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
