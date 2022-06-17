---
title: commits
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
<tr><td><b>Name</b></td><td><code>github.search.commits</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.commits</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `parents` | `array` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `sha` | `string` |  |
| `author` | `object` | Simple User |
| `html_url` | `string` |  |
| `committer` | `object` | Metaproperties for Git author/committer information. |
| `text_matches` | `array` |  |
| `score` | `number` |  |
| `node_id` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `commit` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `commits` | `q` | Find commits via various criteria on the default branch (usually `master`). This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination).<br /><br />When searching for commits, you can get text match metadata for the **message** field when you provide the `text-match` media type. For more details about how to receive highlighted search results, see [Text match<br />metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you want to find commits related to CSS in the [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your query would look something like this:<br /><br />`q=repo:octocat/Spoon-Knife+css` | SELECT |
