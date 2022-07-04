---
title: iap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - iap_settings
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
<tr><td><b>Name</b></td><td><code>iap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.iap_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the IAP protected resource. |
| `accessSettings` | `object` | Access related settings for IAP protected apps. |
| `applicationSettings` | `object` | Wrapper over application specific settings for IAP. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getIapSettings` | `SELECT` | `name` |
