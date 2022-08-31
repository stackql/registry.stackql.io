---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
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
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.budgets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `timePeriod` | `object` | The start and end date for a budget. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| `notifications` | `object` | Dictionary of notifications associated with the budget. Budget can have up to five notifications. |
| `category` | `string` | The category of the budget, whether the budget tracks cost or usage. |
| `type` | `string` | Resource type. |
| `timeGrain` | `string` | The time covered by a budget. Tracking of the amount will be reset based on the time grain. BillingMonth, BillingQuarter, and BillingAnnual are only supported by WD customers |
| `currentSpend` | `object` | The current amount of cost which is being tracked for a budget. |
| `amount` | `number` | The total amount of cost to track with the budget |
| `filter` | `object` | May be used to filter budgets by resource group, resource, or meter. |
| `forecastSpend` | `object` | The forecasted cost which is being tracked for a budget. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Budgets_List` | `SELECT` | `scope` | Lists all budgets for the defined scope. |
| `Budgets_CreateOrUpdate` | `INSERT` | `budgetName, scope` | The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation. |
| `Budgets_Delete` | `DELETE` | `budgetName, scope` | The operation to delete a budget. |
| `Budgets_Get` | `EXEC` | `budgetName, scope` | Gets the budget for the scope by budget name. |
