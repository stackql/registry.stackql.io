---
title: sites
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
<tr><td><b>Name</b></td><td><code>netlify.site.sites</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.site.sites</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `admin_url` | `string` |  |
| `capabilities` | `object` |  |
| `session_id` | `string` |  |
| `deploy_hook` | `string` |  |
| `prerender` | `string` |  |
| `user_id` | `string` |  |
| `git_provider` | `string` |  |
| `password` | `string` |  |
| `custom_domain` | `string` |  |
| `managed_dns` | `boolean` |  |
| `processing_settings` | `object` |  |
| `account_slug` | `string` |  |
| `state` | `string` |  |
| `ssl_url` | `string` |  |
| `account_name` | `string` |  |
| `screenshot_url` | `string` |  |
| `deploy_url` | `string` |  |
| `url` | `string` |  |
| `published_deploy` | `object` |  |
| `notification_email` | `string` |  |
| `plan` | `string` |  |
| `build_settings` | `object` |  |
| `updated_at` | `string` |  |
| `build_image` | `string` |  |
| `force_ssl` | `boolean` |  |
| `id_domain` | `string` |  |
| `ssl` | `boolean` |  |
| `domain_aliases` | `array` |  |
| `default_hooks_data` | `object` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSite` | `site_id` |  | SELECT |
| `listSites` | `` |  | SELECT |
| `listSitesForAccount` | `account_slug` |  | SELECT |
| `createSite` | `` |  | INSERT |
| `createSiteInTeam` | `account_slug` |  | INSERT |
| `deleteSite` | `site_id` |  | DELETE |
| `updateSite` | `site_id` |  | EXEC |
