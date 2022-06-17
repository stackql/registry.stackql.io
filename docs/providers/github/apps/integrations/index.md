---
title: integrations
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
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.integrations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the GitHub app |
| `name` | `string` | The name of the GitHub app |
| `description` | `string` |  |
| `pem` | `string` |  |
| `created_at` | `string` |  |
| `slug` | `string` | The slug name of the GitHub app |
| `installations_count` | `integer` | The number of installations associated with the GitHub app |
| `updated_at` | `string` |  |
| `events` | `array` | The list of events for the GitHub app |
| `webhook_secret` | `string` |  |
| `client_id` | `string` |  |
| `html_url` | `string` |  |
| `permissions` | `object` | The set of permissions for the GitHub app |
| `owner` | `object` | Simple User |
| `external_url` | `string` |  |
| `node_id` | `string` |  |
| `client_secret` | `string` |  |
## Methods
