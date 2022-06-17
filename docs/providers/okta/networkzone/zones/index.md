---
title: zones
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
<tr><td><b>Name</b></td><td><code>okta.networkzone.zones</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.networkzone.zones</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `system` | `boolean` |  |
| `created` | `string` |  |
| `status` | `string` |  |
| `proxies` | `array` |  |
| `locations` | `array` |  |
| `gateways` | `array` |  |
| `proxyType` | `string` |  |
| `_links` | `object` |  |
| `asns` | `array` |  |
| `lastUpdated` | `string` |  |
| `usage` | `string` |  |
| `type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `zoneId` | Fetches a network zone from your Okta organization by `id`. | SELECT |
| `list` | `` | Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query. | SELECT |
| `insert` | `` | Adds a new network zone to your Okta organization. | INSERT |
| `delete` | `zoneId` | Removes network zone. | DELETE |
| `activate` | `zoneId` | Activate Network Zone | EXEC |
| `deactivate` | `zoneId` | Deactivates a network zone. | EXEC |
| `update` | `zoneId` | Updates a network zone in your organization. | EXEC |
