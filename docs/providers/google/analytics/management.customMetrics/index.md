---
title: management.customMetrics
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
<tr><td><b>Name</b></td><td><code>management.customMetrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.customMetrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Custom metric ID. |
| `name` | `string` | Name of the custom metric. |
| `index` | `integer` | Index of the custom metric. |
| `parentLink` | `object` | Parent link for the custom metric. Points to the property to which the custom metric belongs. |
| `min_value` | `string` | Min value of custom metric. |
| `webPropertyId` | `string` | Property ID. |
| `kind` | `string` | Kind value for a custom metric. Set to "analytics#customMetric". It is a read-only field. |
| `accountId` | `string` | Account ID. |
| `scope` | `string` | Scope of the custom metric: HIT or PRODUCT. |
| `updated` | `string` | Time the custom metric was last modified. |
| `type` | `string` | Data type of custom metric. |
| `selfLink` | `string` | Link for the custom metric |
| `max_value` | `string` | Max value of custom metric. |
| `active` | `boolean` | Boolean indicating whether the custom metric is active. |
| `created` | `string` | Time the custom metric was created. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, customMetricId, webPropertyId` | Get a custom metric to which the user has access. |
| `list` | `SELECT` | `accountId, webPropertyId` | Lists custom metrics to which the user has access. |
| `insert` | `INSERT` | `accountId, webPropertyId` | Create a new custom metric. |
| `patch` | `EXEC` | `accountId, customMetricId, webPropertyId` | Updates an existing custom metric. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, customMetricId, webPropertyId` | Updates an existing custom metric. |
