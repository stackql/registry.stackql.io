---
title: sites_traffic_splits
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
<tr><td><b>Name</b></td><td><code>netlify.split_test.sites_traffic_splits</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.split_test.sites_traffic_splits</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `unpublished_at` | `string` |  |
| `created_at` | `string` |  |
| `site_id` | `string` |  |
| `path` | `string` |  |
| `updated_at` | `string` |  |
| `active` | `boolean` |  |
| `branches` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSplitTest` | `site_id, split_test_id` |  | SELECT |
| `getSplitTests` | `site_id` |  | SELECT |
| `createSplitTest` | `site_id` |  | INSERT |
| `updateSplitTest` | `site_id, split_test_id` |  | EXEC |
