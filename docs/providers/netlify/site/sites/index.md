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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.site.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `git_provider` | `string` |
| `url` | `string` |
| `force_ssl` | `boolean` |
| `published_deploy` | `object` |
| `capabilities` | `object` |
| `screenshot_url` | `string` |
| `id_domain` | `string` |
| `account_slug` | `string` |
| `plan` | `string` |
| `account_name` | `string` |
| `admin_url` | `string` |
| `deploy_hook` | `string` |
| `default_hooks_data` | `object` |
| `prerender` | `string` |
| `password` | `string` |
| `user_id` | `string` |
| `processing_settings` | `object` |
| `notification_email` | `string` |
| `ssl` | `boolean` |
| `managed_dns` | `boolean` |
| `session_id` | `string` |
| `deploy_url` | `string` |
| `build_image` | `string` |
| `build_settings` | `object` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `state` | `string` |
| `custom_domain` | `string` |
| `domain_aliases` | `array` |
| `ssl_url` | `string` |
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
