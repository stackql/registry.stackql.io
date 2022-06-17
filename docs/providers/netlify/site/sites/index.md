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
| `session_id` | `string` |
| `default_hooks_data` | `object` |
| `state` | `string` |
| `admin_url` | `string` |
| `git_provider` | `string` |
| `password` | `string` |
| `account_slug` | `string` |
| `published_deploy` | `object` |
| `prerender` | `string` |
| `ssl_url` | `string` |
| `deploy_hook` | `string` |
| `build_image` | `string` |
| `domain_aliases` | `array` |
| `id_domain` | `string` |
| `notification_email` | `string` |
| `user_id` | `string` |
| `updated_at` | `string` |
| `url` | `string` |
| `capabilities` | `object` |
| `created_at` | `string` |
| `processing_settings` | `object` |
| `deploy_url` | `string` |
| `account_name` | `string` |
| `build_settings` | `object` |
| `plan` | `string` |
| `ssl` | `boolean` |
| `custom_domain` | `string` |
| `screenshot_url` | `string` |
| `force_ssl` | `boolean` |
| `managed_dns` | `boolean` |
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
