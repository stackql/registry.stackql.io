---
title: matters
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
<tr><td><b>Name</b></td><td><code>matters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vault.matters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `matters` | `array` | List of matters. |
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `matterId` | Gets the specified matter. |
| `list` | `SELECT` |  | Lists matters the requestor has access to. |
| `create` | `INSERT` |  | Creates a matter with the given name and description. The initial state is open, and the owner is the method caller. Returns the created matter with default view. |
| `delete` | `DELETE` | `matterId` | Deletes the specified matter. Returns the matter with updated state. |
| `addPermissions` | `EXEC` | `matterId` | Adds an account as a matter collaborator. |
| `close` | `EXEC` | `matterId` | Closes the specified matter. Returns the matter with updated state. |
| `count` | `EXEC` | `matterId` | Counts the accounts processed by the specified query. |
| `removePermissions` | `EXEC` | `matterId` | Removes an account as a matter collaborator. |
| `reopen` | `EXEC` | `matterId` | Reopens the specified matter. Returns the matter with updated state. |
| `undelete` | `EXEC` | `matterId` | Undeletes the specified matter. Returns the matter with updated state. |
| `update` | `EXEC` | `matterId` | Updates the specified matter. This updates only the name and description of the matter, identified by matter ID. Changes to any other fields are ignored. Returns the default view of the matter. |
