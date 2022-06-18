---
title: sites_dns
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
<tr><td><b>Name</b></td><td><code>sites_dns</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `user_id` | `string` |
| `records` | `array` |
| `ipv6_enabled` | `boolean` |
| `account_id` | `string` |
| `account_name` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `site_id` | `string` |
| `dedicated` | `boolean` |
| `dns_servers` | `array` |
| `supported_record_types` | `array` |
| `account_slug` | `string` |
| `errors` | `array` |
| `domain` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDNSForSite` | `SELECT` | `site_id` |
| `configureDNSForSite` | `EXEC` | `site_id` |
