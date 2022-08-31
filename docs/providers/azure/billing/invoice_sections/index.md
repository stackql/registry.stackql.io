---
title: invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - invoice_sections
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
<tr><td><b>Name</b></td><td><code>invoice_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.invoice_sections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `targetCloud` | `string` | Possible cloud environments. |
| `type` | `string` | Resource type. |
| `displayName` | `string` | The name of the invoice section. |
| `labels` | `object` | Dictionary of metadata associated with the invoice section. |
| `systemId` | `string` | The system generated unique identifier for an invoice section. |
| `tags` | `object` | Dictionary of metadata associated with the invoice section. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? / |
| `state` | `string` | Identifies the state of an invoice section. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InvoiceSections_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `InvoiceSections_CreateOrUpdate` | `INSERT` | `billingAccountName, billingProfileName, invoiceSectionName` | Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `InvoiceSections_Get` | `EXEC` | `billingAccountName, billingProfileName, invoiceSectionName` | Gets an invoice section by its ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
