---
title: management.customDataSources
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
<tr><td><b>Name</b></td><td><code>management.customDataSources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.customDataSources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Custom data source ID. |
| `name` | `string` | Name of this custom data source. |
| `description` | `string` | Description of custom data source. |
| `schema` | `array` | Collection of schema headers of the custom data source. |
| `childLink` | `object` |  |
| `created` | `string` | Time this custom data source was created. |
| `parentLink` | `object` | Parent link for this custom data source. Points to the web property to which this custom data source belongs. |
| `updated` | `string` | Time this custom data source was last modified. |
| `profilesLinked` | `array` | IDs of views (profiles) linked to the custom data source. |
| `selfLink` | `string` | Link for this Analytics custom data source. |
| `importBehavior` | `string` |  |
| `accountId` | `string` | Account ID to which this custom data source belongs. |
| `uploadType` | `string` | Upload type of the custom data source. |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this custom data source belongs. |
| `kind` | `string` | Resource type for Analytics custom data source. |
| `type` | `string` | Type of the custom data source. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountId, webPropertyId` |
