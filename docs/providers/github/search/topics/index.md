---
title: topics
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
<tr><td><b>Name</b></td><td><code>github.search.topics</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.topics</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `description` | `string` |  |
| `text_matches` | `array` |  |
| `aliases` | `array` |  |
| `created_by` | `string` |  |
| `repository_count` | `integer` |  |
| `released` | `string` |  |
| `curated` | `boolean` |  |
| `logo_url` | `string` |  |
| `short_description` | `string` |  |
| `featured` | `boolean` |  |
| `updated_at` | `string` |  |
| `related` | `array` |  |
| `score` | `number` |  |
| `created_at` | `string` |  |
| `display_name` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `topics` | `q` | Find topics via various criteria. Results are sorted by best match. This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination). See "[Searching topics](https://docs.github.com/articles/searching-topics/)" for a detailed list of qualifiers.<br /><br />When searching for topics, you can get text match metadata for the topic's **short\_description**, **description**, **name**, or **display\_name** field when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you want to search for topics related to Ruby that are featured on https://github.com/topics. Your query might look like this:<br /><br />`q=ruby+is:featured`<br /><br />This query searches for topics with the keyword `ruby` and limits the results to find only topics that are featured. The topics that are the best match for the query appear first in the search results. | SELECT |
