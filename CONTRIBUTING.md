# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

If the change is only an addition of new courses, there's no need to discuss it.

Please note we have a [code of conduct](https://github.com/danilolmoura/awesome-free-courses/blob/master/CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## How to add new courses

First, create a new branch

    git branch -b <branch_name>

Add the course information to the (courses.json file)[https://github.com/danilolmoura/awesome-free-courses/blob/master/courses.json], you can add more than one course at a time

    {
        "course_name": "<course_name>",
        "course_link": "<course_url>",
        "channel_name": "<channel_name>",
        "channel_link": "<channel_url>",
        "language": "<Language>"
    }

Run the script to update README.md

    python create_readme.py

Check if the course has been added to README.md

    git diff README.md

Commit changes

    git add README.md
    git commit -m"Add <course_name>"
    git pull origin master
    git push origin <branch_name>

And finally, create the pull request

## Example

![Example part one](/images/part1.gif)

![Example part one](/images/part2.gif)

![Example part one](/images/part3.gif)
