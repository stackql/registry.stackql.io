---
title: i18nLanguages
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
<tr><td><b>Name</b></td><td><code>i18nLanguages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.youtube.i18nLanguages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the i18n language. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#i18nLanguage". |
| `snippet` | `object` | Basic details about an i18n language, such as language code and human-readable name. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `part` |
