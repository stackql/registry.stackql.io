---
title: credential_authorizations
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
<tr><td><b>Name</b></td><td><code>credential_authorizations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.credential_authorizations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `scopes` | `array` | List of oauth scopes the token has been granted. |
| `token_last_eight` | `string` | Last eight characters of the credential. Only included in responses with credential_type of personal access token. |
| `authorized_credential_id` | `integer` |  |
| `credential_authorized_at` | `string` | Date when the credential was authorized for use. |
| `authorized_credential_title` | `string` | The title given to the ssh key. This will only be present when the credential is an ssh key. |
| `credential_id` | `integer` | Unique identifier for the credential. |
| `login` | `string` | User login that owns the underlying credential. |
| `authorized_credential_note` | `string` | The note given to the token. This will only be present when the credential is a token. |
| `fingerprint` | `string` | Unique string to distinguish the credential. Only included in responses with credential_type of SSH Key. |
| `authorized_credential_expires_at` | `string` | The expiry for the token. This will only be present when the credential is a token. |
| `credential_accessed_at` | `string` | Date when the credential was last accessed. May be null if it was never accessed |
| `credential_type` | `string` | Human-readable description of the credential type. |
## Methods
