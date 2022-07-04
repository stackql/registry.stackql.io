---
title: relyingparty
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty
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
<tr><td><b>Name</b></td><td><code>relyingparty</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `relyingparty_downloadAccount` | `EXEC` |  | Batch download user accounts. |
| `relyingparty_emailLinkSignin` | `EXEC` |  | Reset password for a user. |
| `relyingparty_resetPassword` | `EXEC` |  | Reset password for a user. |
| `relyingparty_sendVerificationCode` | `EXEC` |  | Send SMS verification code. |
| `relyingparty_setAccountInfo` | `EXEC` |  | Set account info for a user. |
| `relyingparty_setProjectConfig` | `EXEC` |  | Set project configuration. |
| `relyingparty_signOutUser` | `EXEC` |  | Sign out user. |
| `relyingparty_signupNewUser` | `EXEC` |  | Signup new user. |
| `relyingparty_uploadAccount` | `EXEC` |  | Batch upload existing user accounts. |
| `relyingparty_verifyAssertion` | `EXEC` |  | Verifies the assertion returned by the IdP. |
| `relyingparty_verifyCustomToken` | `EXEC` |  | Verifies the developer asserted ID token. |
| `relyingparty_verifyPassword` | `EXEC` |  | Verifies the user entered password. |
| `relyingparty_verifyPhoneNumber` | `EXEC` |  | Verifies ownership of a phone number and creates/updates the user account accordingly. |
