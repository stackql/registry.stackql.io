---
title: userinfo.v2.me
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
<tr><td><b>Name</b></td><td><code>userinfo.v2.me</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.oauth2.userinfo.v2.me</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The obfuscated ID of the user. |
| `name` | `string` | The user's full name. |
| `verified_email` | `boolean` | Boolean flag which is true if the email address is verified. Always verified because we only return the user's primary email address. |
| `family_name` | `string` | The user's last name. |
| `gender` | `string` | The user's gender. |
| `given_name` | `string` | The user's first name. |
| `email` | `string` | The user's email address. |
| `locale` | `string` | The user's preferred locale. |
| `picture` | `string` | URL of the user's picture image. |
| `link` | `string` | URL of the profile page. |
| `hd` | `string` | The hosted domain e.g. example.com if the user is Google apps user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |