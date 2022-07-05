---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the Key in the format "projects/{project}/keys/{key}". |
| `testingOptions` | `object` | Options for user acceptance testing. |
| `webSettings` | `object` | Settings specific to keys that can be used by websites. |
| `androidSettings` | `object` | Settings specific to keys that can be used by Android apps. |
| `displayName` | `string` | Human-readable display name of this key. Modifiable by user. |
| `labels` | `object` | See Creating and managing labels. |
| `wafSettings` | `object` | Settings specific to keys that can be used for WAF (Web Application Firewall). |
| `createTime` | `string` | The timestamp corresponding to the creation of this Key. |
| `iosSettings` | `object` | Settings specific to keys that can be used by iOS apps. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_keys_get` | `SELECT` | `name` | Returns the specified key. |
| `projects_keys_list` | `SELECT` | `parent` | Returns the list of all keys that belong to a project. |
| `projects_keys_create` | `INSERT` | `parent` | Creates a new reCAPTCHA Enterprise key. |
| `projects_keys_delete` | `DELETE` | `name` | Deletes the specified key. |
| `projects_keys_migrate` | `EXEC` | `name` | Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Site Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project. |
| `projects_keys_patch` | `EXEC` | `name` | Updates the specified key. |
