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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.site.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `screenshot_url` | `string` |
| `git_provider` | `string` |
| `domain_aliases` | `array` |
| `ssl_url` | `string` |
| `deploy_hook` | `string` |
| `password` | `string` |
| `user_id` | `string` |
| `managed_dns` | `boolean` |
| `prerender` | `string` |
| `account_slug` | `string` |
| `account_name` | `string` |
| `build_image` | `string` |
| `admin_url` | `string` |
| `custom_domain` | `string` |
| `default_hooks_data` | `object` |
| `url` | `string` |
| `ssl` | `boolean` |
| `notification_email` | `string` |
| `capabilities` | `object` |
| `processing_settings` | `object` |
| `created_at` | `string` |
| `session_id` | `string` |
| `build_settings` | `object` |
| `plan` | `string` |
| `id_domain` | `string` |
| `force_ssl` | `boolean` |
| `published_deploy` | `object` |
| `updated_at` | `string` |
| `state` | `string` |
| `deploy_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSite` | `SELECT` | `site_id` |
| `listSites` | `SELECT` |  |
| `listSitesForAccount` | `SELECT` | `account_slug` |
| `createSite` | `INSERT` |  |
| `createSiteInTeam` | `INSERT` | `account_slug` |
| `deleteSite` | `DELETE` | `site_id` |
| `updateSite` | `EXEC` | `site_id` |
