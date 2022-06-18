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
| `state` | `string` |
| `plan` | `string` |
| `deploy_url` | `string` |
| `git_provider` | `string` |
| `published_deploy` | `object` |
| `build_settings` | `object` |
| `default_hooks_data` | `object` |
| `url` | `string` |
| `notification_email` | `string` |
| `build_image` | `string` |
| `capabilities` | `object` |
| `password` | `string` |
| `domain_aliases` | `array` |
| `admin_url` | `string` |
| `account_name` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `managed_dns` | `boolean` |
| `prerender` | `string` |
| `session_id` | `string` |
| `id_domain` | `string` |
| `ssl_url` | `string` |
| `force_ssl` | `boolean` |
| `account_slug` | `string` |
| `deploy_hook` | `string` |
| `processing_settings` | `object` |
| `user_id` | `string` |
| `screenshot_url` | `string` |
| `custom_domain` | `string` |
| `ssl` | `boolean` |
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
