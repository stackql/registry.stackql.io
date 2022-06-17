---
title: domains
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>okta.domain.domains</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.domain.domains</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `domainId` | Fetches a Domain by `id`. | SELECT |
| `list` | `` | List all verified custom Domains for the org. | SELECT |
| `insert` | `` | Creates your domain. | INSERT |
| `delete` | `domainId` | Deletes a Domain by `id`. | DELETE |
| `verify` | `domainId` | Verifies the Domain by `id`. | EXEC |