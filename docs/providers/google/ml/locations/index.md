---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `capabilities` | `array` | Capabilities available in the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_get` | `SELECT` | `name` | Get the complete list of CMLE capabilities in a location, along with their location-specific properties. |
| `projects_locations_list` | `SELECT` | `parent` | List all locations that provides at least one type of CMLE capability. |
