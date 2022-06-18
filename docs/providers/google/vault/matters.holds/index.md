---
title: matters.holds
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
<tr><td><b>Name</b></td><td><code>matters.holds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vault.matters.holds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `holds` | `array` | The list of holds. |
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. If this is empty, then there are no more holds to list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `holdId, matterId` | Gets the specified hold. |
| `list` | `SELECT` | `matterId` | Lists the holds in a matter. |
| `create` | `INSERT` | `matterId` | Creates a hold in the specified matter. |
| `delete` | `DELETE` | `holdId, matterId` | Removes the specified hold and releases the accounts or organizational unit covered by the hold. If the data is not preserved by another hold or retention rule, it might be purged. |
| `addHeldAccounts` | `EXEC` | `holdId, matterId` | Adds accounts to a hold. Returns a list of accounts that have been successfully added. Accounts can be added only to an existing account-based hold. |
| `removeHeldAccounts` | `EXEC` | `holdId, matterId` | Removes the specified accounts from a hold. Returns a list of statuses in the same order as the request. |
| `update` | `EXEC` | `holdId, matterId` | Updates the scope (organizational unit or accounts) and query parameters of a hold. You cannot add accounts to a hold that covers an organizational unit, nor can you add organizational units to a hold that covers individual accounts. If you try, the unsupported values are ignored. |
