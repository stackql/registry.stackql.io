---
title: buckets_firebase
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_firebase
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
<tr><td><b>Name</b></td><td><code>buckets_firebase</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebasestorage.buckets_firebase</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_buckets_addFirebase` | `EXEC` | `bucket` | Links a Google Cloud Storage bucket to a Firebase project. |
| `projects_buckets_removeFirebase` | `EXEC` | `bucket` | Unlinks a linked Google Cloud Storage bucket from a Firebase project. |
