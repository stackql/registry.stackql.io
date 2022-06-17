---
title: sites_files
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
<tr><td><b>Name</b></td><td><code>netlify.file.sites_files</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.file.sites_files</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `path` | `string` |  |
| `sha` | `string` |  |
| `size` | `integer` |  |
| `mime_type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSiteFileByPathName` | `file_path, site_id` |  | SELECT |
| `listSiteFiles` | `site_id` |  | SELECT |
