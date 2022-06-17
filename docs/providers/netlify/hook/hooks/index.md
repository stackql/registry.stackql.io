---
title: hooks
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
<tr><td><b>Name</b></td><td><code>netlify.hook.hooks</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.hook.hooks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `site_id` | `string` |  |
| `type` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `data` | `object` |  |
| `disabled` | `boolean` |  |
| `event` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getHook` | `hook_id` |  | SELECT |
| `listHooksBySiteId` | `site_id` |  | SELECT |
| `createHookBySiteId` | `site_id` |  | INSERT |
| `deleteHook` | `hook_id` |  | DELETE |
| `updateHook` | `hook_id` |  | EXEC |
