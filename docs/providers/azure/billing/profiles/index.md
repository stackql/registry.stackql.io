---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `enabledAzurePlans` | `array` | Information about the enabled azure plans. |
| `billingRelationshipType` | `string` | Identifies which services and purchases are paid by a billing profile. |
| `invoiceDay` | `integer` | The day of the month when the invoice for the billing profile is generated. |
| `statusReasonCode` | `string` | Reason for the specified billing profile status. |
| `billTo` | `object` | Address details. |
| `targetClouds` | `array` | Identifies the cloud environments that are associated with a billing profile. This is a system managed optional field and gets updated as the billing profile gets associated with accounts in various clouds. |
| `invoiceEmailOptIn` | `boolean` | Flag controlling whether the invoices for the billing profile are sent through email. |
| `status` | `string` | The status of the billing profile. |
| `poNumber` | `string` | The purchase order name that will appear on the invoices generated for the billing profile. |
| `spendingLimit` | `string` | The billing profile spending limit. |
| `hasReadAccess` | `boolean` | Indicates whether user has read access to the billing profile. |
| `systemId` | `string` | The system generated unique identifier for a billing profile. |
| `type` | `string` | Resource type. |
| `displayName` | `string` | The name of the billing profile. |
| `invoiceSections` | `object` | The invoice sections associated to the billing profile. By default this is not populated, unless it's specified in $expand. |
| `indirectRelationshipInfo` | `object` | The billing profile details of the partner of the customer for an indirect motion. |
| `currency` | `string` | The currency in which the charges for the billing profile are billed. |
| `tags` | `object` | Tags of billing profiles. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingProfiles_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `BillingProfiles_CreateOrUpdate` | `INSERT` | `billingAccountName, billingProfileName` | Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `BillingProfiles_Get` | `EXEC` | `billingAccountName, billingProfileName` | Gets a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
