---
title: sites_builds
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
<tr><td><b>Name</b></td><td><code>netlify.build.sites_builds</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.build.sites_builds</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `sha` | `string` |  |
| `created_at` | `string` |  |
| `deploy_id` | `string` |  |
| `done` | `boolean` |  |
| `error` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listSiteBuilds` | `site_id` |  | SELECT |
| `createSiteBuild` | `site_id` |  | INSERT |
