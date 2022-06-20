---
title: management.profileUserLinks
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
<tr><td><b>Name</b></td><td><code>management.profileUserLinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.profileUserLinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Entity user link ID |
| `entity` | `object` | Entity for this link. It can be an account, a web property, or a view (profile). |
| `kind` | `string` | Resource type for entity user link. |
| `permissions` | `object` | Permissions the user has for this entity. |
| `selfLink` | `string` | Self link for this resource. |
| `userRef` | `object` | JSON template for a user reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists profile-user links for a given view (profile). |
| `insert` | `INSERT` | `accountId, profileId, webPropertyId` | Adds a new user to the given view (profile). |
| `delete` | `DELETE` | `accountId, linkId, profileId, webPropertyId` | Removes a user from the given view (profile). |
| `update` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Updates permissions for an existing user on the given view (profile). |
