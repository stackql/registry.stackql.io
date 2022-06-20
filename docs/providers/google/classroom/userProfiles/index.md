---
title: userProfiles
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
<tr><td><b>Name</b></td><td><code>userProfiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.classroom.userProfiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the user. Read-only. |
| `name` | `object` | Details of the user's name. |
| `emailAddress` | `string` | Email address of the user. Read-only. |
| `permissions` | `array` | Global permissions of the user. Read-only. |
| `photoUrl` | `string` | URL of user's profile photo. Read-only. |
| `verifiedTeacher` | `boolean` | Represents whether a G Suite for Education user's domain administrator has explicitly verified them as being a teacher. If the user is not a member of a G Suite for Education domain, than this field is always false. Read-only |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `userId` |
