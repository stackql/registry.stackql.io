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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `account_name` | `string` |
| `supported_record_types` | `array` |
| `dedicated` | `boolean` |
| `records` | `array` |
| `errors` | `array` |
| `updated_at` | `string` |
| `dns_servers` | `array` |
| `account_id` | `string` |
| `account_slug` | `string` |
| `domain` | `string` |
| `ipv6_enabled` | `boolean` |
| `site_id` | `string` |
| `created_at` | `string` |
| `user_id` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDNSForSite` | `SELECT` | `site_id` |
| `configureDNSForSite` | `EXEC` | `site_id` |
