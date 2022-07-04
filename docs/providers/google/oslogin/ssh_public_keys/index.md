---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.oslogin.ssh_public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The canonical resource name. |
| `key` | `string` | Public key text in SSH format, defined by RFC4253 section 6.6. |
| `expirationTimeUsec` | `string` | An expiration time in microseconds since epoch. |
| `fingerprint` | `string` | Output only. The SHA-256 fingerprint of the SSH public key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_sshPublicKeys_get` | `SELECT` | `name` | Retrieves an SSH public key. |
| `users_sshPublicKeys_create` | `INSERT` | `parent` | Create an SSH public key |
| `users_sshPublicKeys_delete` | `DELETE` | `name` | Deletes an SSH public key. |
| `users_sshPublicKeys_patch` | `EXEC` | `name` | Updates an SSH public key and returns the profile information. This method supports patch semantics. |
