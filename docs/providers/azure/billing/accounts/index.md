---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `soldTo` | `object` | Address details. |
| `billingProfiles` | `object` | The billing profiles associated with the billing account. By default this is not populated, unless it's specified in $expand. |
| `hasReadAccess` | `boolean` | Indicates whether user has read access to the billing account. |
| `enrollmentAccounts` | `array` | The accounts associated to the enrollment. |
| `notificationEmailAddress` | `string` | Notification email address, only for legacy accounts |
| `type` | `string` | Resource type. |
| `enrollmentDetails` | `object` | The properties of an enrollment. |
| `displayName` | `string` | The billing account name. |
| `accountType` | `string` | The type of customer. |
| `agreementType` | `string` | The type of agreement. |
| `departments` | `array` | The departments associated to the enrollment. |
| `accountStatus` | `string` | The current status of the billing account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingAccounts_List` | `SELECT` |  | Lists the billing accounts that a user has access to. |
| `BillingAccounts_Get` | `EXEC` | `billingAccountName` | Gets a billing account by its ID. |
| `BillingAccounts_ListInvoiceSectionsByCreateSubscriptionPermission` | `EXEC` | `billingAccountName` | Lists the invoice sections for which the user has permission to create Azure subscriptions. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingAccounts_Update` | `EXEC` | `billingAccountName` | Updates the properties of a billing account. Currently, displayName and address can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
