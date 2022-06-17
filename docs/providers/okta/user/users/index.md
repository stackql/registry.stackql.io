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
<tr><td><b>Name</b></td><td><code>okta.user.users</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `passwordChanged` | `string` |  |
| `activated` | `string` |  |
| `type` | `object` |  |
| `lastLogin` | `string` |  |
| `profile` | `object` |  |
| `statusChanged` | `string` |  |
| `status` | `string` |  |
| `lastUpdated` | `string` |  |
| `_embedded` | `object` |  |
| `credentials` | `object` |  |
| `transitioningToStatus` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `userId` | Fetches a user from your Okta organization. | SELECT |
| `list` | `` | Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria. | SELECT |
| `insert` | `` | Creates a new user in your Okta organization with or without credentials. | INSERT |
| `delete` | `userId` | Deletes a user permanently.  This operation can only be performed on users that have a `DEPROVISIONED` status.  **This action cannot be recovered!** | DELETE |
| `activate` | `sendEmail, userId` | Activates a user.  This operation can only be performed on users with a `STAGED` status.  Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `ACTIVE` when the activation process is complete. | EXEC |
| `changePassword` | `userId` | Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid password credential | EXEC |
| `changeRecoveryQuestion` | `userId` | Changes a user's recovery question & answer credential by validating the user's current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid password credential | EXEC |
| `deactivate` | `userId` | Deactivates a user.  This operation can only be performed on users that do not have a `DEPROVISIONED` status.  Deactivation of a user is an asynchronous operation.  The user will have the `transitioningToStatus` property with a value of `DEPROVISIONED` during deactivation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `DEPROVISIONED` when the deactivation process is complete. | EXEC |
| `expirePassword` | `userId` | This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login. | EXEC |
| `expirePasswordTemp` | `userId` | This operation transitions the user to the status of `PASSWORD_EXPIRED` and the user's password is reset to a temporary password that is returned. | EXEC |
| `forgotPassword` | `userId` |  | EXEC |
| `reactivate` | `userId` | Reactivates a user.  This operation can only be performed on users with a `PROVISIONED` status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](#activate-user). | EXEC |
| `resetFactors` | `userId` | This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors. | EXEC |
| `resetPassword` | `sendEmail, userId` | Generates a one-time token (OTT) that can be used to reset a user's password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow. | EXEC |
| `suspend` | `userId` | Suspends a user.  This operation can only be performed on users with an `ACTIVE` status.  The user will have a status of `SUSPENDED` when the process is complete. | EXEC |
| `unlock` | `userId` | Unlocks a user with a `LOCKED_OUT` status and returns them to `ACTIVE` status.  Users will be able to login with their current password. | EXEC |
| `unsuspend` | `userId` | Unsuspends a user and returns them to the `ACTIVE` state.  This operation can only be performed on users that have a `SUSPENDED` status. | EXEC |
| `update` | `userId` | Update a user's profile and/or credentials using strict-update semantics. | EXEC |