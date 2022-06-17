---
title: dns_zones_dns_records
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
<tr><td><b>Name</b></td><td><code>dns_zones_dns_records</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones_dns_records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `dns_zone_id` | `string` |
| `tag` | `string` |
| `type` | `string` |
| `flag` | `integer` |
| `hostname` | `string` |
| `site_id` | `string` |
| `value` | `string` |
| `ttl` | `integer` |
| `managed` | `boolean` |
| `priority` | `integer` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDnsRecords` | `SELECT` | `zone_id` |
| `getIndividualDnsRecord` | `SELECT` | `dns_record_id, zone_id` |
| `createDnsRecord` | `INSERT` | `zone_id` |
| `deleteDnsRecord` | `DELETE` | `dns_record_id, zone_id` |
