---
title: accounts.clients.invitations
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
<tr><td><b>Name</b></td><td><code>accounts.clients.invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adexchangebuyer2.accounts.clients.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `invitations` | `array` | The returned list of client users. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListClientUserInvitationsRequest.pageToken field in the subsequent call to the clients.invitations.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, clientAccountId, invitationId` | Retrieves an existing client user invitation. |
| `list` | `SELECT` | `accountId, clientAccountId` | Lists all the client users invitations for a client with a given account ID. |
| `create` | `INSERT` | `accountId, clientAccountId` | Creates and sends out an email invitation to access an Ad Exchange client buyer account. |
