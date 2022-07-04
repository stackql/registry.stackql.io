---
title: dest_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dest_groups
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
<tr><td><b>Name</b></td><td><code>dest_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.dest_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Immutable. Identifier for the TunnelDestGroup. Must be unique within the project and contain only lower case letters (a-z) and dashes (-). |
| `cidrs` | `array` | null List of CIDRs that this group applies to. |
| `fqdns` | `array` | null List of FQDNs that this group applies to. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_iap_tunnel_locations_destGroups_get` | `SELECT` | `name` | Retrieves an existing TunnelDestGroup. |
| `projects_iap_tunnel_locations_destGroups_list` | `SELECT` | `parent` | Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups` |
| `projects_iap_tunnel_locations_destGroups_create` | `INSERT` | `parent` | Creates a new TunnelDestGroup. |
| `projects_iap_tunnel_locations_destGroups_delete` | `DELETE` | `name` | Deletes a TunnelDestGroup. |
| `projects_iap_tunnel_locations_destGroups_patch` | `EXEC` | `name` | Updates a TunnelDestGroup. |