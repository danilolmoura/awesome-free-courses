import json

NEW_LINE = '\n'
HEADER = '#'

TABLE_HEADER = '| Name | Language| Channel|\n|------|---------|--------|\n'
TABLE_LINE = '| [{}]({}) | {} | [{}]({}) '

TABLE_OF_CONTENTS_INDENT = '  '
TABLE_OF_CONTENTS_FORMAT = '{}* [{}](#{})\n'

def count_courses(json_file):
    total_courses = 0

    for key in json_file.keys():
        if key == 'id':
            continue

        if key == 'courses':
            total_courses += len(json_file[key])
            continue

        total_courses += count_courses(json_file[key])

    return total_courses


def write_header(readme_file, total_courses):
    readme_file.write('# awesome-free-courses\n')
    readme_file.write('A collection of all amazing free courses\n\n')
    readme_file.write(' [![license](https://img.shields.io/github/license/danilolmoura/awesome-free-courses.svg)](/LICENSE)')
    readme_file.write(' [![GitHub contributors](https://img.shields.io/github/contributors/danilolmoura/awesome-free-courses.svg)](https://github.com/danilolmoura/awesome-free-courses/graphs/contributors)')
    readme_file.write(' ![Total Courses contributors](https://img.shields.io/badge/total--courses-{}-blue)'.format(total_courses))
    readme_file.write('\n\n')
    readme_file.write('See [how to contribute](/CONTRIBUTING.md)')

def write_footer(readme_file):
    readme_file.write('# Thanks to all the contributors ❤️')
    readme_file.write('<a href = "https://github.com/danilolmoura/awesome-free-courses/graphs/contributors">')
    readme_file.write(' <img src = "https://contrib.rocks/image?repo=danilolmoura/awesome-free-courses"/>')
    readme_file.write('</a>')

def write_table_of_contents(json_file, level, readme_file, category_name=None):
    if level == 0:
        readme_file.write(NEW_LINE)
        readme_file.write('# Table of contents\n')

    if category_name:
        if category_name == 'courses':
            return
        
        if category_name == 'id':
            return

        readme_file.write(TABLE_OF_CONTENTS_FORMAT.format(
                TABLE_OF_CONTENTS_INDENT * level,
                category_name,
                json_file['id']
            )
        )

    for key in json_file.keys():
        write_table_of_contents(json_file[key], level + 1, readme_file, category_name=key)

def write_courses(courses, readme_file):
    readme_file.write(TABLE_HEADER)
    for course in courses:
        readme_file.writelines(TABLE_LINE.format(
            course['course_name'],
            course['course_link'],
            course['language'],
            course['channel_name'],
            course['channel_link']) + NEW_LINE)

def write_readme(json_file, level, readme_file):
    readme_file.write(NEW_LINE)
    for key in json_file.keys():
        if key == 'id':
            continue

        if key == 'courses':
            write_courses(json_file['courses'], readme_file)
            continue

        readme_file.write('\n\n' + (HEADER * (level + 1)) + ' ' + key)

        write_readme(json_file[key], level + 1, readme_file)

if __name__ == '__main__':
    level = 0
    j = open('courses.json', 'r')
    json_file = json.loads(j.read())
    readme_file = open('README.md', 'w')

    total_courses = count_courses(json_file)

    write_header(readme_file, total_courses)
    readme_file.write(NEW_LINE)
    write_table_of_contents(json_file, level, readme_file)
    write_readme(json_file, level, readme_file)
    readme_file.write(NEW_LINE)
    write_footer(readme_file)

    j.close()
    readme_file.close()