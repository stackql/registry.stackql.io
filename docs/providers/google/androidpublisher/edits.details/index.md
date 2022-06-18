---
title: edits.details
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
<tr><td><b>Name</b></td><td><code>edits.details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.edits.details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `contactPhone` | `string` | The user-visible support telephone number for this app. |
| `contactWebsite` | `string` | The user-visible website for this app. |
| `defaultLanguage` | `string` | Default language code, in BCP 47 format (eg "en-US"). |
| `contactEmail` | `string` | The user-visible support email for this app. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `editId, packageName` | Gets details of an app. |
| `patch` | `EXEC` | `editId, packageName` | Patches details of an app. |
| `update` | `EXEC` | `editId, packageName` | Updates details of an app. |
