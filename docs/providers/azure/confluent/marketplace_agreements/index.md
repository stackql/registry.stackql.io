---
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - confluent
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
<tr><td><b>Name</b></td><td><code>marketplace_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confluent.marketplace_agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM id of the resource. |
| `name` | `string` | The name of the agreement. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `publisher` | `string` | Publisher identifier string. |
| `product` | `string` | Product identifier string. |
| `licenseTextLink` | `string` | Link to HTML with Microsoft and Publisher terms. |
| `plan` | `string` | Plan identifier string. |
| `type` | `string` | The type of the agreement. |
| `privacyPolicyLink` | `string` | Link to the privacy policy of the publisher. |
| `retrieveDatetime` | `string` | Date and time in UTC of when the terms were accepted. This is empty if Accepted is false. |
| `signature` | `string` | Terms signature. |
| `accepted` | `boolean` | If any version of the terms have been accepted, otherwise false. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MarketplaceAgreements_List` | `SELECT` | `subscriptionId` |
| `MarketplaceAgreements_Create` | `INSERT` | `subscriptionId` |
