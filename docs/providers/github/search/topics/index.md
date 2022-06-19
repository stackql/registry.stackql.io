---
title: topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `name` | `string` |
| `description` | `string` |
| `created_by` | `string` |
| `released` | `string` |
| `featured` | `boolean` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `aliases` | `array` |
| `display_name` | `string` |
| `repository_count` | `integer` |
| `short_description` | `string` |
| `related` | `array` |
| `score` | `number` |
| `text_matches` | `array` |
| `curated` | `boolean` |
| `logo_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `topics` | `SELECT` | `q` |
