---
title: management.filters
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management.filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Filter ID. |
| `name` | `string` | Name of this filter. |
| `accountId` | `string` | Account ID to which this filter belongs. |
| `parentLink` | `object` | Parent link for this filter. Points to the account to which this filter belongs. |
| `includeDetails` | `object` | JSON template for an Analytics filter expression. |
| `selfLink` | `string` | Link for this filter. |
| `type` | `string` | Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE, UPPERCASE, SEARCH_AND_REPLACE and ADVANCED. |
| `lowercaseDetails` | `object` | Details for the filter of the type LOWER. |
| `kind` | `string` | Resource type for Analytics filter. |
| `searchAndReplaceDetails` | `object` | Details for the filter of the type SEARCH_AND_REPLACE. |
| `created` | `string` | Time this filter was created. |
| `excludeDetails` | `object` | JSON template for an Analytics filter expression. |
| `uppercaseDetails` | `object` | Details for the filter of the type UPPER. |
| `updated` | `string` | Time this filter was last modified. |
| `advancedDetails` | `object` | Details for the filter of the type ADVANCED. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, filterId` | Returns filters to which the user has access. |
| `list` | `SELECT` | `accountId` | Lists all filters for an account |
| `insert` | `INSERT` | `accountId` | Create a new filter. |
| `delete` | `DELETE` | `accountId, filterId` | Delete a filter. |
| `patch` | `EXEC` | `accountId, filterId` | Updates an existing filter. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, filterId` | Updates an existing filter. |
