---
title: deployments
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.deployments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the deployment |
| `description` | `string` |  |
| `updated_at` | `string` |  |
| `sha` | `string` |  |
| `environment` | `string` | Name for the target deployment environment. |
| `repository_url` | `string` |  |
| `node_id` | `string` |  |
| `statuses_url` | `string` |  |
| `transient_environment` | `boolean` | Specifies if the given environment is will no longer exist at some point in the future. Default: false. |
| `production_environment` | `boolean` | Specifies if the given environment is one that end-users directly interact with. Default: false. |
| `created_at` | `string` |  |
| `task` | `string` | Parameter to specify a task to execute |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `creator` | `object` | Simple User |
| `ref` | `string` | The ref to deploy. This can be a branch, tag, or sha. |
| `url` | `string` |  |
| `original_environment` | `string` |  |
| `payload` | `` |  |
## Methods
