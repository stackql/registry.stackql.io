---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership`. Shall be of the form `groups/{group}/memberships/{membership}`. |
| `preferredMemberKey` | `object` | A unique identifier for an entity in the Cloud Identity Groups API. An entity can represent either a group with an optional `namespace` or a user without a `namespace`. The combination of `id` and `namespace` must be unique; however, the same `id` can be used with different `namespace`s. |
| `roles` | `array` | The `MembershipRole`s that apply to the `Membership`. If unspecified, defaults to a single `MembershipRole` with `name` `MEMBER`. Must not contain duplicate `MembershipRole`s with the same `name`. |
| `type` | `string` | Output only. The type of the membership. |
| `updateTime` | `string` | Output only. The time when the `Membership` was last updated. |
| `createTime` | `string` | Output only. The time when the `Membership` was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `groups_memberships_get` | `SELECT` | `name` | Retrieves a `Membership`. |
| `groups_memberships_list` | `SELECT` | `parent` | Lists the `Membership`s within a `Group`. |
| `groups_memberships_create` | `INSERT` | `parent` | Creates a `Membership`. |
| `groups_memberships_delete` | `DELETE` | `name` | Deletes a `Membership`. |
| `groups_memberships_checkTransitiveMembership` | `EXEC` | `parent` | Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group. |
| `groups_memberships_lookup` | `EXEC` | `parent` | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`. |
| `groups_memberships_modifyMembershipRoles` | `EXEC` | `name` | Modifies the `MembershipRole`s of a `Membership`. |
| `groups_memberships_searchTransitiveGroups` | `EXEC` | `parent` | Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups. |
| `groups_memberships_searchTransitiveMemberships` | `EXEC` | `parent` | Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the group is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships. |
