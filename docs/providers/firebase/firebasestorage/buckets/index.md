---
title: buckets
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
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebasestorage.buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the bucket. |
| `reconciling` | `boolean` | Output only. Represents whether a bucket is being moved to a new location, in which case reconciling is set to true. |
| `location` | `string` | Output only. Location of the storage bucket. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_buckets_get` | `SELECT` | `name` | Gets a single linked storage bucket. |
| `projects_buckets_list` | `SELECT` | `parent` | Lists the linked storage buckets for a project. |
