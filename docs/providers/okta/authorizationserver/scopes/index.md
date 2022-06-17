---
title: scopes
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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.scopes</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.scopes</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `system` | `boolean` |  |
| `consent` | `string` |  |
| `default` | `boolean` |  |
| `displayName` | `string` |  |
| `metadataPublish` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `authServerId, scopeId` | Success | SELECT |
| `list` | `authServerId` | Success | SELECT |
| `insert` | `authServerId` | Success | INSERT |
| `delete` | `authServerId, scopeId` | Success | DELETE |
| `update` | `authServerId, scopeId` | Success | EXEC |
