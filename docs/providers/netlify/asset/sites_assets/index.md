---
title: sites_assets
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
<tr><td><b>Name</b></td><td><code>netlify.asset.sites_assets</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.asset.sites_assets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `state` | `string` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `visibility` | `string` |  |
| `content_type` | `string` |  |
| `creator_id` | `string` |  |
| `size` | `integer` |  |
| `key` | `string` |  |
| `site_id` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSiteAssetInfo` | `asset_id, site_id` |  | SELECT |
| `listSiteAssets` | `site_id` |  | SELECT |
| `createSiteAsset` | `site_id` |  | INSERT |
| `deleteSiteAsset` | `asset_id, site_id` |  | DELETE |
| `updateSiteAsset` | `asset_id, site_id` |  | EXEC |
