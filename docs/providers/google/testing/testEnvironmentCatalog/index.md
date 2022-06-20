---
title: testEnvironmentCatalog
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
<tr><td><b>Name</b></td><td><code>testEnvironmentCatalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.testing.testEnvironmentCatalog</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `iosDeviceCatalog` | `object` | The currently supported iOS devices. |
| `networkConfigurationCatalog` | `object` |  |
| `softwareCatalog` | `object` | The currently provided software environment on the devices under test. |
| `androidDeviceCatalog` | `object` | The currently supported Android devices. |
| `deviceIpBlockCatalog` | `object` | List of IP blocks used by the Firebase Test Lab |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `environmentType` |
