---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
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
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `category` | `string` | The category of the agreement signed by a customer. |
| `type` | `string` | Resource type. |
| `expirationDate` | `string` | The date when the agreement expires. |
| `acceptanceMode` | `string` | The mode of acceptance for an agreement. |
| `status` | `string` | The current status of the agreement. |
| `effectiveDate` | `string` | The date from which the agreement is effective. |
| `agreementLink` | `string` | The URL to download the agreement. |
| `billingProfileInfo` | `object` | Details about billing profile associated with agreement and available only for specific agreements. |
| `participants` | `array` | The list of participants that participates in acceptance of an agreement. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Agreements_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the agreements for a billing account. |
| `Agreements_Get` | `EXEC` | `agreementName, billingAccountName` | Gets an agreement by ID. |
