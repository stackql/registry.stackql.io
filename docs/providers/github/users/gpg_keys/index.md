---
title: gpg_keys
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
<tr><td><b>Name</b></td><td><code>gpg_keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.gpg_keys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `key_id` | `string` |  |
| `can_sign` | `boolean` |  |
| `can_encrypt_storage` | `boolean` |  |
| `created_at` | `string` |  |
| `raw_key` | `string` |  |
| `subkeys` | `array` |  |
| `can_certify` | `boolean` |  |
| `can_encrypt_comms` | `boolean` |  |
| `emails` | `array` |  |
| `public_key` | `string` |  |
| `expires_at` | `string` |  |
| `primary_key_id` | `integer` |  |
## Methods
