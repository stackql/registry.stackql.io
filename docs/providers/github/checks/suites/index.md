---
title: suites
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suites</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.suites</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `runs_rerequestable` | `boolean` |  |
| `status` | `string` |  |
| `updated_at` | `string` |  |
| `after` | `string` |  |
| `url` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `conclusion` | `string` |  |
| `head_branch` | `string` |  |
| `app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `check_runs_url` | `string` |  |
| `rerequestable` | `boolean` |  |
| `pull_requests` | `array` |  |
| `latest_check_runs_count` | `integer` |  |
| `head_commit` | `object` | Simple Commit |
| `node_id` | `string` |  |
| `head_sha` | `string` | The SHA of the head commit that is being checked. |
| `created_at` | `string` |  |
| `before` | `string` |  |
## Methods
