
def get_courses():
    return [
        "Python Programming",
        "Database Management Systems",
        "Web Development"
    ]


if __name__ == "__main__":
    print("Available LMS Courses:")
    for course in get_courses():
        print(course)
