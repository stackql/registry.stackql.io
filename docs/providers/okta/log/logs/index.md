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
|:-----|:---------|
| `securityContext` | `object` |
| `version` | `string` |
| `published` | `string` |
| `eventType` | `string` |
| `actor` | `object` |
| `legacyEventType` | `string` |
| `displayMessage` | `string` |
| `outcome` | `object` |
| `debugContext` | `object` |
| `severity` | `string` |
| `request` | `object` |
| `transaction` | `object` |
| `authenticationContext` | `object` |
| `uuid` | `string` |
| `target` | `array` |
| `client` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
