---
title: code
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
<tr><td><b>Name</b></td><td><code>github.search.code</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.code</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `sha` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `path` | `string` |  |
| `html_url` | `string` |  |
| `language` | `string` |  |
| `score` | `number` |  |
| `text_matches` | `array` |  |
| `file_size` | `integer` |  |
| `line_numbers` | `array` |  |
| `url` | `string` |  |
| `last_modified_at` | `string` |  |
| `git_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `code` | `q` | Searches for query terms inside of a file. This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination).<br /><br />When searching for code, you can get text match metadata for the file **content** and file **path** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you want to find the definition of the `addClass` function inside [jQuery](https://github.com/jquery/jquery) repository, your query would look something like this:<br /><br />`q=addClass+in:file+language:js+repo:jquery/jquery`<br /><br />This query searches for the keyword `addClass` within a file's contents. The query limits the search to files where the language is JavaScript in the `jquery/jquery` repository.<br /><br />#### Considerations for code search<br /><br />Due to the complexity of searching code, there are a few restrictions on how searches are performed:<br /><br />*   Only the _default branch_ is considered. In most cases, this will be the `master` branch.<br />*   Only files smaller than 384 KB are searchable.<br />*   You must always include at least one search term when searching source code. For example, searching for [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ago&type=Code) is not valid, while [`amazing<br />language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ago&type=Code) is. | SELECT |
