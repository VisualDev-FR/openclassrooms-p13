Technologies
====

Django
----
    `Django <https://www.djangoproject.com/>`_ is a web framework for building web applications using the
    Python programming language. It promotes rapid development and clean, maintainable code through
    its model-view-controller (MVC) architecture. Django includes an integrated Object-Relational Mapping (ORM)
    for simplified database operations.

    Django was chosen for its ease of use, robustness, and well-integrated ecosystem. It simplifies
    the creation of web applications and provides features such as automatic admin interfaces,
    form handling, and user/session management.

Whitenoise
----
    `Whitenoise <http://whitenoise.evans.io/en/stable/>`_ is a Python library used to serve static files for
    Python web applications. It's often employed with frameworks like Django to serve CSS, JavaScript,
    and other static files directly from the web application.

    It was chosen to simplifie the serving of static files directly from the web application,
    eliminating the need for an external web server like Nginx or Apache.

SQLite
----
    `SQLite <https://www.sqlite.org/>`_ is a lightweight, self-contained relational database management system.
    It is serverless and widely used in embedded systems and small to medium-sized web applications.

    SQLite is chosen for its simplicity and ease of integration. A full-fledged database server would have been
    overkill for this project, and a lightweight solution was preferred.

Github Actions
----
    `GitHub Actions <https://docs.github.com/en/actions>`_ is used for setting up continuous integration
    and continuous deployment (CI/CD) workflows for a project directly within a GitHub repository.

    It automates software development workflows, making it easier to build,
    test, and deploy code directly from GitHub. It provides a seamless integration with a
    repository and offers a wide range of pre-built actions.

Docker
----
    `Docker <https://www.docker.com/why-docker/>`_ is used for containerization, creating reproducible environments for applications.

    Docker was chosen to simplifies deployment by encapsulating application and its dependencies into containers.
    This ensures consistency across different environments and makes it easier to scale applications.

Sphinx
----
    `Sphinx <https://www.sphinx-doc.org/>`_ is used for creating documentation for this application.

    it's a powerful tool for generating documentation from source code.
    It supports multiple output formats, including HTML and PDF, making it easy
    to maintain and share comprehensive documentation.