---
title: external_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - external_security_solutions
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
<tr><td><b>Name</b></td><td><code>external_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.external_security_solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The URI to fetch the next page. |
| `value` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExternalSecuritySolutions_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of external security solutions for the subscription. |
| `ExternalSecuritySolutions_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets a list of external Security Solutions for the subscription and location. |
| `ExternalSecuritySolutions_Get` | `EXEC` | `api-version, ascLocation, externalSecuritySolutionsName, resourceGroupName, subscriptionId` | Gets a specific external Security Solution. |
