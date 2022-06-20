---
title: contactGroups
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
<tr><td><b>Name</b></td><td><code>contactGroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.people.contactGroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contactGroups` | `array` | The list of contact groups. Members of the contact groups are not populated. |
| `nextPageToken` | `string` | The token that can be used to retrieve the next page of results. |
| `nextSyncToken` | `string` | The token that can be used to retrieve changes since the last request. |
| `totalItems` | `integer` | The total number of items in the list without pagination. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactGroupsId` | Provides information about a person by specifying a resource name. Use `people/me` to indicate the authenticated user. The request returns a 400 error if 'personFields' is not specified. |
| `list` | `SELECT` |  | List all contact groups owned by the authenticated user. Members of the contact groups are not populated. |
| `create` | `INSERT` |  | Create a new contact group owned by the authenticated user. Created contact group names must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. |
| `delete` | `DELETE` | `contactGroupsId` | Delete an existing contact group owned by the authenticated user by specifying a contact group resource name. |
| `batchGet` | `EXEC` |  | Get a list of contact groups owned by the authenticated user by specifying a list of contact group resource names. |
| `update` | `EXEC` | `contactGroupsId` | Update the name of an existing contact group owned by the authenticated user. Updated contact group names must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. |
