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
<tr><td><b>Name</b></td><td><code>okta.log.logs</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.log.logs</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `debugContext` | `object` |  |
| `request` | `object` |  |
| `version` | `string` |  |
| `outcome` | `object` |  |
| `client` | `object` |  |
| `displayMessage` | `string` |  |
| `severity` | `string` |  |
| `securityContext` | `object` |  |
| `eventType` | `string` |  |
| `legacyEventType` | `string` |  |
| `actor` | `object` |  |
| `transaction` | `object` |  |
| `published` | `string` |  |
| `authenticationContext` | `object` |  |
| `target` | `array` |  |
| `uuid` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `` | The Okta System Log API provides read access to your organizationâ€™s system log. This API provides more functionality than the Events API | SELECT |
