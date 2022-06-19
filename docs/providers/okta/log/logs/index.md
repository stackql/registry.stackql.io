---
title: logs
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
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.log.logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `debugContext` | `object` |
| `actor` | `object` |
| `eventType` | `string` |
| `version` | `string` |
| `authenticationContext` | `object` |
| `target` | `array` |
| `client` | `object` |
| `securityContext` | `object` |
| `published` | `string` |
| `uuid` | `string` |
| `displayMessage` | `string` |
| `request` | `object` |
| `legacyEventType` | `string` |
| `severity` | `string` |
| `transaction` | `object` |
| `outcome` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` |  |
