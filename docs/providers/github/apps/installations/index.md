---
title: installations
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
<tr><td><b>Name</b></td><td><code>installations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.installations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the installation. |
| `app_slug` | `string` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `target_type` | `string` |  |
| `suspended_by` | `object` | Simple User |
| `events` | `array` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `has_multiple_single_files` | `boolean` |  |
| `updated_at` | `string` |  |
| `html_url` | `string` |  |
| `app_id` | `integer` |  |
| `repositories_url` | `string` |  |
| `created_at` | `string` |  |
| `single_file_paths` | `array` |  |
| `access_tokens_url` | `string` |  |
| `suspended_at` | `string` |  |
| `account` | `` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `single_file_name` | `string` |  |
| `contact_email` | `string` |  |
## Methods
