---
title: cse
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
<tr><td><b>Name</b></td><td><code>cse</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.customsearch.cse</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `displayLink` | `string` | An abridged version of this search result’s URL, e.g. www.example.com. |
| `fileFormat` | `string` | The file format of the search result. |
| `htmlSnippet` | `string` | The snippet of the search result, in HTML. |
| `htmlTitle` | `string` | The title of the search result, in HTML. |
| `mime` | `string` | The MIME type of the search result. |
| `image` | `object` | Image belonging to a custom search result. |
| `title` | `string` | The title of the search result, in plain text. |
| `snippet` | `string` | The snippet of the search result, in plain text. |
| `cacheId` | `string` | Indicates the ID of Google's cached version of the search result. |
| `pagemap` | `object` | Contains [PageMap](https://developers.google.com/custom-search/docs/structured_data#pagemaps) information for this search result. |
| `htmlFormattedUrl` | `string` | The HTML-formatted URL displayed after the snippet for each search result. |
| `formattedUrl` | `string` | The URL displayed after the snippet for each search result. |
| `labels` | `array` | Encapsulates all information about refinement labels. |
| `kind` | `string` | A unique identifier for the type of current object. For this API, it is `customsearch#result.` |
| `link` | `string` | The full URL to which the search result is pointing, e.g. http://www.example.com/foo/bar. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |