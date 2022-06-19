---
title: dns_zones
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `supported_record_types` | `array` |
| `errors` | `array` |
| `created_at` | `string` |
| `account_id` | `string` |
| `dns_servers` | `array` |
| `dedicated` | `boolean` |
| `site_id` | `string` |
| `updated_at` | `string` |
| `domain` | `string` |
| `account_name` | `string` |
| `user_id` | `string` |
| `records` | `array` |
| `ipv6_enabled` | `boolean` |
| `account_slug` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDnsZone` | `SELECT` | `zone_id` |
| `getDnsZones` | `SELECT` |  |
| `createDnsZone` | `INSERT` |  |
| `deleteDnsZone` | `DELETE` | `zone_id` |
