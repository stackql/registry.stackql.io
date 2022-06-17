---
title: webhooks
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
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.webhooks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the webhook. |
| `name` | `string` | The name of a valid service, use 'web' for a webhook. |
| `config` | `object` |  |
| `created_at` | `string` |  |
| `ping_url` | `string` |  |
| `type` | `string` |  |
| `deliveries_url` | `string` |  |
| `updated_at` | `string` |  |
| `test_url` | `string` |  |
| `active` | `boolean` | Determines whether the hook is actually triggered on pushes. |
| `last_response` | `object` |  |
| `events` | `array` | Determines what events the hook is triggered for. Default: ['push']. |
| `url` | `string` |  |
## Methods
