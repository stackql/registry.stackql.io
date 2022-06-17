---
title: sessions
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
<tr><td><b>Name</b></td><td><code>okta.session.sessions</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.session.sessions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `userId` | `string` |  |
| `status` | `string` |  |
| `expiresAt` | `string` |  |
| `idp` | `object` |  |
| `createdAt` | `string` |  |
| `lastPasswordVerification` | `string` |  |
| `_links` | `object` |  |
| `lastFactorVerification` | `string` |  |
| `login` | `string` |  |
| `amr` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `sessionId` | Get details about a session. | SELECT |
| `insert` | `` | Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL. | INSERT |
| `delete` | `sessionId` |  | DELETE |
| `refresh` | `sessionId` |  | EXEC |
