---
title: sites_build_hooks
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
<tr><td><b>Name</b></td><td><code>netlify.build_hook.sites_build_hooks</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.build_hook.sites_build_hooks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `site_id` | `string` |  |
| `title` | `string` |  |
| `url` | `string` |  |
| `branch` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSiteBuildHook` | `id, site_id` |  | SELECT |
| `listSiteBuildHooks` | `site_id` |  | SELECT |
| `createSiteBuildHook` | `site_id` |  | INSERT |
| `deleteSiteBuildHook` | `id, site_id` |  | DELETE |
| `updateSiteBuildHook` | `id, site_id` |  | EXEC |
