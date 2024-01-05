Project Overview
====

This project encompasses a straightforward web application designed to showcase user profiles and real estate listings. Users can conveniently view and interact with these components through the application's user interface. Additionally, the system supports data editing functionalities accessible via the site's administrative interface.

Key Features
----

1. **User Profiles:**

   - Represents user profiles within the platform.

2. **Real Estate Listings (Lettings):**

   - Contains detailed information about available real estate listings.
   - Facilitates the display of properties available for rent.
   - Linked with corresponding address details for comprehensive property information.

Technology Stack
----

- **Framework:** Implemented using the Django web framework.

- **Containerization:** Utilizes Docker for containerization, ensuring consistent and reproducible deployment across various environments.

- **CI/CD Pipeline:**

  - Establishes a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions.
  - Automates testing procedures, Docker image creation, and deployment processes.
  - Ensures efficient and reliable development workflows.

See more details :doc:`here <technologies>`

Deployment Workflow
----

1. **Testing:** GitHub Actions executes various tests to verify the correctness of the codebase.

2. **Docker Image Creation:** Upon successful testing, GitHub Actions builds a Docker image encapsulating the entire application.

3. **Docker Hub Upload:** The Docker image is uploaded to Docker Hub, providing a centralized repository for container images.

4. **Automated Deployment on Render:**
   - Leveraging Render, the site is automatically deployed based on changes pushed to the repository.

See more details :doc:`here <deploy>`
