---
title: relyingparty
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
<tr><td><b>Name</b></td><td><code>relyingparty</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `createAuthUri` | `EXEC` |  | Creates the URI used by the IdP to authenticate the user. |
| `deleteAccount` | `EXEC` |  | Delete user account. |
| `downloadAccount` | `EXEC` |  | Batch download user accounts. |
| `emailLinkSignin` | `EXEC` |  | Reset password for a user. |
| `getAccountInfo` | `EXEC` |  | Returns the account info. |
| `getOobConfirmationCode` | `EXEC` |  | Get a code for user action confirmation. |
| `getProjectConfig` | `EXEC` |  | Get project configuration. |
| `getPublicKeys` | `EXEC` |  | Get token signing public key. |
| `getRecaptchaParam` | `EXEC` |  | Get recaptcha secure param. |
| `resetPassword` | `EXEC` |  | Reset password for a user. |
| `sendVerificationCode` | `EXEC` |  | Send SMS verification code. |
| `setAccountInfo` | `EXEC` |  | Set account info for a user. |
| `setProjectConfig` | `EXEC` |  | Set project configuration. |
| `signOutUser` | `EXEC` |  | Sign out user. |
| `signupNewUser` | `EXEC` |  | Signup new user. |
| `uploadAccount` | `EXEC` |  | Batch upload existing user accounts. |
| `verifyAssertion` | `EXEC` |  | Verifies the assertion returned by the IdP. |
| `verifyCustomToken` | `EXEC` |  | Verifies the developer asserted ID token. |
| `verifyPassword` | `EXEC` |  | Verifies the user entered password. |
| `verifyPhoneNumber` | `EXEC` |  | Verifies ownership of a phone number and creates/updates the user account accordingly. |