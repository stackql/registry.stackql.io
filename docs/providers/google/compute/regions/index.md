---
title: regions
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
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] Textual description of the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `quotas` | `array` | [Output Only] Quotas assigned to this region. |
| `status` | `string` | [Output Only] Status of the region, either UP or DOWN. |
| `zones` | `array` | [Output Only] A list of zones available in this region, in the form of resource URLs. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#region for regions. |
| `supportsPzs` | `boolean` | [Output Only] Reserved for future use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, region` | Returns the specified Region resource. Gets a list of available regions by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of region resources available to the specified project. |
