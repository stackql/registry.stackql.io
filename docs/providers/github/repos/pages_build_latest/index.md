---
title: pages_build_latest
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
<tr><td><b>Name</b></td><td><code>pages_build_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages_build_latest</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `commit` | `string` |  |
| `created_at` | `string` |  |
| `duration` | `integer` |  |
| `error` | `object` |  |
| `pusher` | `object` | Simple User |
| `status` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_latest_pages_build` | `SELECT` | `owner, repo` |
