---
title: idps
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
<tr><td><b>Name</b></td><td><code>okta.inlinehook.idps</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.inlinehook.idps</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `lastUpdated` | `string` |  |
| `version` | `string` |  |
| `channel` | `object` |  |
| `status` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `inlineHookId` | Gets an inline hook by ID | SELECT |
| `list` | `` | Success | SELECT |
| `insert` | `` | Success | INSERT |
| `delete` | `inlineHookId` | Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion. | DELETE |
| `activate` | `inlineHookId` | Activates the Inline Hook matching the provided id | EXEC |
| `deactivate` | `inlineHookId` | Deactivates the Inline Hook matching the provided id | EXEC |
| `execute` | `inlineHookId` | Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes. | EXEC |
| `update` | `inlineHookId` | Updates an inline hook by ID | EXEC |
