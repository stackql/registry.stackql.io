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
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] Textual description of the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `availableCpuPlatforms` | `array` | [Output Only] Available cpu/platform selections for the zone. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#zone for zones. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `region` | `string` | [Output Only] Full URL reference to the region which hosts the zone. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `status` | `string` | [Output Only] Status of the zone, either UP or DOWN. |
| `supportsPzs` | `boolean` | [Output Only] Reserved for future use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, zone` | Returns the specified Zone resource. Gets a list of available zones by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of Zone resources available to the specified project. |