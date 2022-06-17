---
title: branch_protection
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
<tr><td><b>Name</b></td><td><code>branch_protection</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branch_protection</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `allow_deletions` | `object` |  |
| `required_pull_request_reviews` | `object` | Protected Branch Pull Request Review |
| `protection_url` | `string` |  |
| `required_conversation_resolution` | `object` |  |
| `allow_force_pushes` | `object` |  |
| `required_status_checks` | `object` | Protected Branch Required Status Check |
| `enabled` | `boolean` |  |
| `enforce_admins` | `object` | Protected Branch Admin Enforced |
| `required_linear_history` | `object` |  |
| `required_signatures` | `object` |  |
| `restrictions` | `object` | Branch Restriction Policy |
| `url` | `string` |  |
## Methods
