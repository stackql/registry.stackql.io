---
title: gpg_keys
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
<tr><td><b>Name</b></td><td><code>github.users.gpg_keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.gpg_keys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `can_encrypt_comms` | `boolean` |  |
| `primary_key_id` | `integer` |  |
| `expires_at` | `string` |  |
| `subkeys` | `array` |  |
| `raw_key` | `string` |  |
| `can_sign` | `boolean` |  |
| `emails` | `array` |  |
| `can_certify` | `boolean` |  |
| `key_id` | `string` |  |
| `public_key` | `string` |  |
| `created_at` | `string` |  |
| `can_encrypt_storage` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_gpg_key_for_authenticated_user` | `gpg_key_id` | View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). | SELECT |
| `list_gpg_keys_for_authenticated_user` | `` | Lists the current user's GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). | SELECT |
| `list_gpg_keys_for_user` | `username` | Lists the GPG keys for a user. This information is accessible by anyone. | SELECT |
| `create_gpg_key_for_authenticated_user` | `data__armored_public_key` | Adds a GPG key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). | INSERT |
| `delete_gpg_key_for_authenticated_user` | `gpg_key_id` | Removes a GPG key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). | DELETE |
