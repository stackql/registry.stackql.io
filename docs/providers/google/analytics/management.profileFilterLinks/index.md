---
title: management.profileFilterLinks
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
<tr><td><b>Name</b></td><td><code>management.profileFilterLinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.profileFilterLinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Profile filter link ID. |
| `profileRef` | `object` | JSON template for a linked view (profile). |
| `rank` | `integer` | The rank of this profile filter link relative to the other filters linked to the same profile.<br />For readonly (i.e., list and get) operations, the rank always starts at 1.<br />For write (i.e., create, update, or delete) operations, you may specify a value between 0 and 255 inclusively, [0, 255]. In order to insert a link at the end of the list, either don't specify a rank or set a rank to a number greater than the largest rank in the list. In order to insert a link to the beginning of the list specify a rank that is less than or equal to 1. The new link will move all existing filters with the same or lower rank down the list. After the link is inserted/updated/deleted all profile filter links will be renumbered starting at 1. |
| `selfLink` | `string` | Link for this profile filter link. |
| `filterRef` | `object` | JSON template for a profile filter link. |
| `kind` | `string` | Resource type for Analytics filter. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, linkId, profileId, webPropertyId` | Returns a single profile filter link. |
| `list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists all profile filter links for a profile. |
| `insert` | `INSERT` | `accountId, profileId, webPropertyId` | Create a new profile filter link. |
| `delete` | `DELETE` | `accountId, linkId, profileId, webPropertyId` | Delete a profile filter link. |
| `patch` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Update an existing profile filter link. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Update an existing profile filter link. |
