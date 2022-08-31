---
title: solutions_reference_data
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions_reference_data
  - security
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
<tr><td><b>Name</b></td><td><code>solutions_reference_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.solutions_reference_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `template` | `string` | The security solutions' template |
| `alertVendorName` | `string` | The security solutions' vendor name |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Location where the resource is stored |
| `packageInfoUrl` | `string` | The security solutions' package info url |
| `securityFamily` | `string` | The security family of the security solution |
| `productName` | `string` | The security solutions' product name |
| `publisherDisplayName` | `string` | The security solutions' publisher display name |
| `publisher` | `string` | The security solutions' publisher |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecuritySolutionsReferenceData_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets list of all supported Security Solutions for subscription and location. |
| `securitySolutionsReferenceData_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of all supported Security Solutions for the subscription. |
