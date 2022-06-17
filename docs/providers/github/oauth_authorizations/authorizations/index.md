---
title: authorizations
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
<tr><td><b>Name</b></td><td><code>authorizations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.oauth_authorizations.authorizations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `installation` | `object` |  |
| `url` | `string` |  |
| `hashed_token` | `string` |  |
| `token_last_eight` | `string` |  |
| `token` | `string` |  |
| `fingerprint` | `string` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `app` | `object` |  |
| `note_url` | `string` |  |
| `scopes` | `array` | A list of scopes that this authorization is in. |
| `expires_at` | `string` |  |
| `note` | `string` |  |
| `user` | `object` | Simple User |
## Methods
