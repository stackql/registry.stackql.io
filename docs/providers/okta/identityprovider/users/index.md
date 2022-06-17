---
title: users
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
<tr><td><b>Name</b></td><td><code>okta.identityprovider.users</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `_embedded` | `object` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `externalId` | `string` |  |
| `lastUpdated` | `string` |  |
| `profile` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `idpId, userId` | Fetches a linked IdP user by ID | SELECT |
| `list` | `idpId` | Find all the users linked to an identity provider | SELECT |
| `insert` | `idpId, userId` | Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type | INSERT |
| `delete` | `idpId, userId` | Removes the link between the Okta user and the IdP user. | DELETE |
