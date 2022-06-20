---
title: users.settings
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
<tr><td><b>Name</b></td><td><code>users.settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getAutoForwarding` | `EXEC` | `userId` | Gets the auto-forwarding setting for the specified account. |
| `getImap` | `EXEC` | `userId` | Gets IMAP settings. |
| `getLanguage` | `EXEC` | `userId` | Gets language settings. |
| `getPop` | `EXEC` | `userId` | Gets POP settings. |
| `getVacation` | `EXEC` | `userId` | Gets vacation responder settings. |
| `updateAutoForwarding` | `EXEC` | `userId` | Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled. This method is only available to service account clients that have been delegated domain-wide authority. |
| `updateImap` | `EXEC` | `userId` | Updates IMAP settings. |
| `updateLanguage` | `EXEC` | `userId` | Updates language settings. If successful, the return object contains the `displayLanguage` that was saved for the user, which may differ from the value passed into the request. This is because the requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is, and so the variant may be chosen and saved instead. |
| `updatePop` | `EXEC` | `userId` | Updates POP settings. |
| `updateVacation` | `EXEC` | `userId` | Updates vacation responder settings. |
