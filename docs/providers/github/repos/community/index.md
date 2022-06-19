---
title: community
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
<tr><td><b>Name</b></td><td><code>community</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.community</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `description` | `string` |
| `documentation` | `string` |
| `files` | `object` |
| `health_percentage` | `integer` |
| `updated_at` | `string` |
| `content_reports_enabled` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_community_profile_metrics` | `SELECT` | `owner, repo` |
