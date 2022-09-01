---
title: instructions
hide_title: false
hide_table_of_contents: false
keywords:
  - instructions
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
<tr><td><b>Name</b></td><td><code>instructions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.instructions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `startDate` | `string` | The date this billing instruction goes into effect. |
| `type` | `string` | Resource type. |
| `amount` | `number` | The amount budgeted for this billing instruction. |
| `creationDate` | `string` | The date this billing instruction was created. |
| `endDate` | `string` | The date this billing instruction is no longer in effect. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Instructions_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the instructions by billing profile id. |
| `Instructions_Get` | `EXEC` | `billingAccountName, billingProfileName, instructionName` | Get the instruction by name. These are custom billing instructions and are only applicable for certain customers. |
| `Instructions_Put` | `EXEC` | `billingAccountName, billingProfileName, instructionName` | Creates or updates an instruction. These are custom billing instructions and are only applicable for certain customers. |
