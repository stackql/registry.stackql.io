---
title: runs
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.runs</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The id of the check. |
| `name` | `string` | The name of the check. |
| `node_id` | `string` |  |
| `head_sha` | `string` | The SHA of the commit that is being checked. |
| `url` | `string` |  |
| `deployment` | `object` | A deployment created as the result of an Actions check run from a workflow that references an environment |
| `app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `html_url` | `string` |  |
| `completed_at` | `string` |  |
| `pull_requests` | `array` |  |
| `status` | `string` | The phase of the lifecycle that the check is currently in. |
| `check_suite` | `object` |  |
| `output` | `object` |  |
| `started_at` | `string` |  |
| `details_url` | `string` |  |
| `conclusion` | `string` |  |
| `external_id` | `string` |  |
## Methods
