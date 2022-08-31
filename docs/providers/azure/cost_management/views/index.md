---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - cost_management
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `metric` | `string` | Metric to use when displaying costs. |
| `pivots` | `array` | Configuration of 3 sub-views in the Cost Analysis UI. |
| `modifiedOn` | `string` | Date when the user last modified this view. |
| `currency` | `string` | Currency of the current view. |
| `chart` | `string` | Chart type of the main view in Cost Analysis. Required. |
| `dateRange` | `string` | Date range of the current view. |
| `query` | `object` | The definition of a report config. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| `scope` | `string` | Cost Management scope to save the view on. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope. |
| `createdOn` | `string` | Date the user created this view. |
| `kpis` | `array` | List of KPIs to show in Cost Analysis UI. |
| `accumulated` | `string` | Show costs accumulated over time. |
| `displayName` | `string` | User input name of the view. Required. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Views_List` | `SELECT` |  | Lists all views by tenant and object. |
| `Views_ListByScope` | `SELECT` | `scope` | Lists all views at the given scope. |
| `Views_CreateOrUpdate` | `INSERT` | `viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `Views_Delete` | `DELETE` | `viewName` | The operation to delete a view. |
| `Views_DeleteByScope` | `DELETE` | `scope, viewName` | The operation to delete a view. |
| `Views_CreateOrUpdateByScope` | `EXEC` | `scope, viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `Views_Get` | `EXEC` | `viewName` | Gets the view by view name. |
| `Views_GetByScope` | `EXEC` | `scope, viewName` | Gets the view for the defined scope by view name. |
