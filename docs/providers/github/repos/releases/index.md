---
title: releases
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
<tr><td><b>Name</b></td><td><code>github.repos.releases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.releases</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `author` | `object` | Simple User |
| `mentions_count` | `integer` |  |
| `tag_name` | `string` | The name of the tag. |
| `reactions` | `object` |  |
| `published_at` | `string` |  |
| `tarball_url` | `string` |  |
| `assets` | `array` |  |
| `node_id` | `string` |  |
| `body_text` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `url` | `string` |  |
| `assets_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `discussion_url` | `string` | The URL of the release discussion. |
| `html_url` | `string` |  |
| `upload_url` | `string` |  |
| `body` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `body_html` | `string` |  |
| `created_at` | `string` |  |
| `zipball_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_release` | `owner, release_id, repo` | **Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia). | SELECT |
| `get_release_by_tag` | `owner, repo, tag` | Get a published release with the specified tag. | SELECT |
| `list_releases` | `owner, repo` | This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/rest/reference/repos#list-repository-tags).<br /><br />Information about published releases are available to everyone. Only users with push access will receive listings for draft releases. | SELECT |
| `create_release` | `owner, repo, data__tag_name` | Users with push access to the repository can create a release.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. | INSERT |
| `delete_release` | `owner, release_id, repo` | Users with push access to the repository can delete a release. | DELETE |
| `generate_release_notes` | `owner, repo, data__tag_name` | Generate a name and body describing a [release](https://docs.github.com/rest/reference/repos#releases). The body content will be markdown formatted and contain information like the changes since last release and users who contributed. The generated release notes are not saved anywhere. They are intended to be generated and used when creating a new release. | EXEC |
| `update_release` | `owner, release_id, repo` | Users with push access to the repository can edit a release. | EXEC |
