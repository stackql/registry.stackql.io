---
title: deployment_statuses
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
<tr><td><b>Name</b></td><td><code>deployment_statuses</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.deployment_statuses</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `description` | `string` | A short description of the status. |
| `target_url` | `string` | Deprecated: the URL to associate with this status. |
| `creator` | `object` | Simple User |
| `state` | `string` | The state of the status. |
| `created_at` | `string` |  |
| `environment` | `string` | The environment of the deployment that the status is for. |
| `log_url` | `string` | The URL to associate with this status. |
| `deployment_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `repository_url` | `string` |  |
| `updated_at` | `string` |  |
| `environment_url` | `string` | The URL for accessing your environment. |
## Methods
