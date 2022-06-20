---
title: defaultObjectAccessControls
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
<tr><td><b>Name</b></td><td><code>defaultObjectAccessControls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.defaultObjectAccessControls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the access-control entry. |
| `entityId` | `string` | The ID for the entity, if any. |
| `projectTeam` | `object` | The project team associated with the entity, if any. |
| `generation` | `string` | The content generation of the object, if applied to an object. |
| `object` | `string` | The name of the object, if applied to an object. |
| `role` | `string` | The access permission for the entity. |
| `selfLink` | `string` | The link to this access-control entry. |
| `email` | `string` | The email address associated with the entity, if any. |
| `etag` | `string` | HTTP 1.1 Entity tag for the access-control entry. |
| `bucket` | `string` | The name of the bucket. |
| `domain` | `string` | The domain associated with the entity, if any. |
| `entity` | `string` | The entity holding the permission, in one of the following forms: <br />- user-userId <br />- user-email <br />- group-groupId <br />- group-email <br />- domain-domain <br />- project-team-projectId <br />- allUsers <br />- allAuthenticatedUsers Examples: <br />- The user liz@example.com would be user-liz@example.com. <br />- The group example@googlegroups.com would be group-example@googlegroups.com. <br />- To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |
| `kind` | `string` | The kind of item this is. For object access control entries, this is always storage#objectAccessControl. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucket, entity` | Returns the default object ACL entry for the specified entity on the specified bucket. |
| `list` | `SELECT` | `bucket` | Retrieves default object ACL entries on the specified bucket. |
| `insert` | `INSERT` | `bucket` | Creates a new default object ACL entry on the specified bucket. |
| `delete` | `DELETE` | `bucket, entity` | Permanently deletes the default object ACL entry for the specified entity on the specified bucket. |
| `patch` | `EXEC` | `bucket, entity` | Patches a default object ACL entry on the specified bucket. |
| `update` | `EXEC` | `bucket, entity` | Updates a default object ACL entry on the specified bucket. |