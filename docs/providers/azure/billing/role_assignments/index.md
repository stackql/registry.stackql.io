---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
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
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.role_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `createdByPrincipalTenantId` | `string` | The tenant Id of the user who created the role assignment. |
| `userAuthenticationType` | `string` | The authentication type. |
| `createdByPrincipalId` | `string` | The principal Id of the user who created the role assignment. |
| `roleDefinitionId` | `string` | The ID of the role definition. |
| `scope` | `string` | The scope at which the role was assigned. |
| `type` | `string` | Resource type. |
| `createdByUserEmailAddress` | `string` | The email address of the user who created the role assignment. |
| `userEmailAddress` | `string` | The email address of the user. |
| `principalId` | `string` | The principal id of the user to whom the role was assigned. |
| `createdOn` | `string` | The date the role assignment was created. |
| `principalTenantId` | `string` | The principal tenant id of the user to whom the role was assigned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingRoleAssignments_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleAssignments_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingRoleAssignments_ListByInvoiceSection` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingRoleAssignments_DeleteByBillingAccount` | `DELETE` | `billingAccountName, billingRoleAssignmentName` | Deletes a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleAssignments_DeleteByBillingProfile` | `DELETE` | `billingAccountName, billingProfileName, billingRoleAssignmentName` | Deletes a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleAssignments_DeleteByInvoiceSection` | `DELETE` | `billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName` | Deletes a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingRoleAssignments_GetByBillingAccount` | `EXEC` | `billingAccountName, billingRoleAssignmentName` | Gets a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleAssignments_GetByBillingProfile` | `EXEC` | `billingAccountName, billingProfileName, billingRoleAssignmentName` | Gets a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleAssignments_GetByInvoiceSection` | `EXEC` | `billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName` | Gets a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |