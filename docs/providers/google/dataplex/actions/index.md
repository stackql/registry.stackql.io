---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `actions` | `array` | Actions under the given parent lake/zone/asset. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_actions_list` | `SELECT` | `parent` | Lists action resources in a lake. |
| `projects_locations_lakes_zones_actions_list` | `SELECT` | `parent` | Lists action resources in a zone. |
| `projects_locations_lakes_zones_assets_actions_list` | `SELECT` | `parent` | Lists action resources in an asset. |
