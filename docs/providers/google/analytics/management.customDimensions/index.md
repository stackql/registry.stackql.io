---
title: management.customDimensions
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
<tr><td><b>Name</b></td><td><code>management.customDimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.customDimensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Custom dimension ID. |
| `name` | `string` | Name of the custom dimension. |
| `created` | `string` | Time the custom dimension was created. |
| `index` | `integer` | Index of the custom dimension. |
| `parentLink` | `object` | Parent link for the custom dimension. Points to the property to which the custom dimension belongs. |
| `updated` | `string` | Time the custom dimension was last modified. |
| `kind` | `string` | Kind value for a custom dimension. Set to "analytics#customDimension". It is a read-only field. |
| `webPropertyId` | `string` | Property ID. |
| `accountId` | `string` | Account ID. |
| `active` | `boolean` | Boolean indicating whether the custom dimension is active. |
| `scope` | `string` | Scope of the custom dimension: HIT, SESSION, USER or PRODUCT. |
| `selfLink` | `string` | Link for the custom dimension |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, customDimensionId, webPropertyId` | Get a custom dimension to which the user has access. |
| `list` | `SELECT` | `accountId, webPropertyId` | Lists custom dimensions to which the user has access. |
| `insert` | `INSERT` | `accountId, webPropertyId` | Create a new custom dimension. |
| `patch` | `EXEC` | `accountId, customDimensionId, webPropertyId` | Updates an existing custom dimension. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, customDimensionId, webPropertyId` | Updates an existing custom dimension. |
