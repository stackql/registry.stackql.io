---
title: environments_public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_public_key
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
<tr><td><b>Name</b></td><td><code>environments_public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudshell.environments_public_key</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_environments_addPublicKey` | `INSERT` | `environment` | Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS. |
| `users_environments_removePublicKey` | `DELETE` | `environment` | Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND. |