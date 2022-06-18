---
title: statistics_commit_activity
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
<tr><td><b>Name</b></td><td><code>statistics_commit_activity</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.statistics_commit_activity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `days` | `array` |
| `total` | `integer` |
| `week` | `integer` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_commit_activity_stats` | `SELECT` | `owner, repo` |
